import traceback

import requests
import oracledb

import kst

def connect_oracle_safety_master(user, password, host, port, sid):
    '''
    Oracle SAFETY_MASTER DB 연결 메서드 \n
    * 예외 발생시 None 반환
    :param user: 사용자 이름
    :param password: 비밀번호
    :param host: 호스트 이름
    :param port: 포트
    :param sid: SID
    :return: conn, cursor
    '''

    try:
        conn = oracledb.connect(user=str(user), password=str(password), dsn=f"{host}:{port}/{sid}")
        cursor = conn.cursor()

        return conn, cursor

    except oracledb.Error as e:
        return None, None



def select_gu_info(cursor):
    '''
    GU_INFO 테이블에서 구코드, 위도, 경도 정보를 가져오는 쿼리 메서드
    :param cursor:
    :return: gu_info (튜플이 담겨져 있는 리스트)
    '''

    sql = "SELECT GU_CD, MS_LAT, MS_LON FROM GU_INFO"
    cursor.execute(sql)
    gu_info = cursor.fetchall()

    return gu_info

def get_weather_current_fromapi(gu_info):
    """
    OpenWeatherMap API로 부터 자치구별 현재 날씨를 가져오는 메서드
    :param gu_info: 자치구별 구코드, 위도, 경도 정보가 담겨 있는 튜플이 담긴 리스트
    :return: weather_current (딕셔너리가 담겨져 있는 리스트)
    """

    # 모든 자치구의 현재날씨 정보를 담을 리스트
    weather_current = []

    appid = 'cb8af55639b6799776fe6d104fa3b416'
    units = 'metric'
    lang = 'kr'

    # 모든 자치구 정보가 담긴 리스트를 순회
    for gu in gu_info:

        # 각 자치구의 현재날씨 정보를 담을 딕셔너리
        gu_weather = {}

        gu_cd = gu[0]
        lat = gu[1]
        lon = gu[2]

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}&units={units}&lang={lang}"

        try:

            data = requests.get(url).json()

            # 응답 데이터가 없으면 반복문 건너뛰기
            if not data:
                continue

            else :
                # 응답 결과 값이 200(성공) 이 아니면 반복문 건너뛰기
                if data['cod'] != 200:
                    continue

                else:

                    gu_weather['weather_id'] = gu_cd + kst.kst_serial_from_unix(data['dt'])
                    gu_weather['gu_cd'] = gu_cd
                    gu_weather['temp'] = data['main']['temp']
                    gu_weather['min_temp'] = data['main']['temp_min']
                    gu_weather['max_temp'] = data['main']['temp_max']
                    gu_weather['feels_like_temp'] = data['main']['feels_like']
                    gu_weather['weather_desc'] = data['weather'][0]['description']
                    gu_weather['weather_icon_id'] = data['weather'][0]['icon']
                    gu_weather['humidity'] = data['main']['humidity']
                    gu_weather['wind_speed'] = data['wind']['speed']
                    gu_weather['ms_dt'] = kst.kst_from_unix(data['dt'])
                    gu_weather['cur_dt'] = kst.cur_time_kst()

                    # 현재날씨 리스트에 딕셔너리로된 각 자치구의 현재날씨 정보추가
                    weather_current.append(gu_weather)

        except Exception:
            continue

    return weather_current

def insert_weather_current(conn, cursor, weather_current):
    '''
    API에서 가져온 현재 날씨 정보를 DB에 INSERT 하는 메서드
    :param conn:
    :param cursor:
    :param weather_current: 자치구별 현재날씨 정보가 딕셔너리로 담겨져 있는 리스트)
    :return: 성공여부(True|False), message(예외 메시지)
    '''

    sql = """
    MERGE INTO WEATHER_CURRENT WC
    USING (SELECT :weather_id AS WEATHER_ID FROM DUAL) NEW_DATA
    ON (WC.WEATHER_ID = NEW_DATA.WEATHER_ID)
    WHEN MATCHED THEN
		UPDATE SET WC.TEMP = :temp, WC.MIN_TEMP = :min_temp, WC.MAX_TEMP = :max_temp, WC.FEELS_LIKE_TEMP = :feels_like_temp,
		      	   WC.WEATHER_DESC = :weather_desc, WC.WEATHER_ICON_ID = :weather_icon_id, WC.HUMIDITY = :humidity, 
				   WC.WIND_SPEED = :wind_speed, WC.MS_DT = :ms_dt, WC.MOD_DT = :cur_dt
    WHEN NOT MATCHED THEN
        INSERT (WEATHER_ID, GU_CD, TEMP, MIN_TEMP, MAX_TEMP, FEELS_LIKE_TEMP, 
                WEATHER_DESC, WEATHER_ICON_ID, HUMIDITY, WIND_SPEED, MS_DT, CRT_DT) 
        VALUES (:weather_id, :gu_cd, :temp, :min_temp, :max_temp, :feels_like_temp, :weather_desc, :weather_icon_id,
       	        :humidity, :wind_speed, :ms_dt, :cur_dt)
    """

    try:
        cursor.executemany(sql, weather_current)
        conn.commit()
        return True, 'success'

    except Exception:
        conn.rollback()
        return False, traceback.format_exc()

def refresh_weather_current_data(user, password, host, port, sid):
    '''
    현재 날씨 정보를 가져와 DB에 저장하는 주요 로직을 조정하는 메서드 \n
    * 자원 반납 수행
    :param user: 사용자 이름
    :param password: 비밀번호
    :param host: 호스트 이름
    :param port: 포트
    :param sid: 서비스 이름
    :return:
    '''

    # 자원 반납을 위한 try-finally 문
    try:
        conn, cursor = connect_oracle_safety_master(user, password, host, port, sid)
        # conn, cursor 가 None 일 경우(DB 연결 중 예외 발생 시) 예외 발생
        if conn is None or cursor is None:
            raise oracledb.Error('DB 접속 중 에러 발생')

        gu_info = select_gu_info(cursor)
        # gu_info 가 None 일 경우 예외 발생
        if len(gu_info) == 0:
            raise Exception('DB 조회 결과 gu_info 가 없습니다.')

        weather_current = get_weather_current_fromapi(gu_info)
        # weather_current 가 None 일 경우 예외 발생
        if len(weather_current) == 0:
            raise Exception('현재 날씨 API 응답 결과가 없습니다.')


        result, message = insert_weather_current(conn, cursor, weather_current)
        # result 가 False 일 경우(예외 발생 시) 예외 발생
        if not result:
           raise Exception(message)

    finally:
        if cursor:
            cursor.close()
            cursor = None

        if conn:
            conn.close()
            conn = None

def main():

    user = "SAMA"
    password = "SAMA1234"
    host = '192.168.100.30'
    port = 1522
    sid = 'XE'

    try:
        refresh_weather_current_data(user, password, host, port, sid)
        with open("./log/wc_success_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_weather_current_data 작업 완료')  # 성공 메시지 기록
            f.close()
    except Exception as e:
        with open("./log/wc_error_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_weather_current_data 작업중 오류 발생')  # 오류 메시지 기록
            f.write('\n' + traceback.format_exc())  # 오류 메시지 기록
            f.close()

if __name__ == '__main__':
    main()
