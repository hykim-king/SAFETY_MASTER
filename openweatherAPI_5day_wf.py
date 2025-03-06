import traceback

import oracledb
import requests

import kst
from openweatherAPI_wc import connect_oracle_safety_master, select_gu_info


def get_weather_forecast_fromapi(gu_info):
    """
    OpenWeatherMap API로 부터 자치구별 날씨예보를 가져오는 메서드
    :param gu_info: 자치구별 구코드, 위도, 경도 정보가 담겨 있는 튜플이 담긴 리스트
    :return: weather_forecast (딕셔너리가 담겨져 있는 리스트)
    """

    # 모든 자치구의 날씨예보 정보를 담을 리스트
    weather_forecast = []

    appid = 'cb8af55639b6799776fe6d104fa3b416'
    units = 'metric'
    lang = 'kr'

    # 모든 자치구 정보가 담긴 리스트를 순회
    for gu in gu_info:

        gu_cd = gu[0]
        lat = gu[1]
        lon = gu[2]

        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={appid}&units={units}&lang={lang}"

        try:

            data = requests.get(url).json()

            # 응답 데이터가 없으면 반복문 건너뛰기
            if not data:
                continue

            else:

                # 응답 결과 값이 200(성공) 아니거나 1보다 작으면 반복문 건너뛰기
                if data['cod'] != '200' or data['cnt'] < 1:
                    continue

                else:

                    for elem in data['list']:
                        # 각 자치구의 날씨예보 정보를 담을 딕셔너리
                        gu_forecast = {}

                        gu_forecast['fcst_id'] = gu_cd + kst.kst_serial_from_unix(elem['dt'])
                        gu_forecast['gu_cd'] = gu_cd
                        gu_forecast['fcst_dt'] = kst.kst_from_unix(elem['dt'])
                        gu_forecast['temp'] = elem['main']['temp']
                        gu_forecast['min_temp'] = elem['main']['temp_min']
                        gu_forecast['max_temp'] = elem['main']['temp_max']
                        gu_forecast['feels_like_temp'] = elem['main']['feels_like']
                        gu_forecast['weather_desc'] = elem['weather'][0]['description']
                        gu_forecast['weather_icon_id'] = elem['weather'][0]['icon']
                        gu_forecast['humidity'] = elem['main']['humidity']
                        gu_forecast['wind_speed'] = elem['wind']['speed']
                        gu_forecast['pop'] = elem['pop']
                        gu_forecast['cur_dt'] = kst.cur_time_kst()

                        weather_forecast.append(gu_forecast)

        except Exception:
            continue

    return weather_forecast

def insert_weather_forecast(conn, cursor, weather_forecast):
    '''
    API에서 가져온 날씨예보 정보를 DB에 INSERT 하는 메서드
    :param conn:
    :param cursor:
    :param weather_forecast: 자치구별 날씨예보 정보가 딕셔너리로 담겨져 있는 리스트)
    :return: 성공여부(True|False), message(예외 메시지)
    '''

    sql = """
    MERGE INTO WEATHER_FORECAST WF
    USING (SELECT :FCST_ID AS FCST_ID FROM DUAL) NEW_DATA
    ON (WF.FCST_ID = NEW_DATA.FCST_ID)
    WHEN MATCHED THEN
		UPDATE SET WF.FCST_DT = :fcst_dt, WF.TEMP = :temp, WF.MIN_TEMP = :min_temp, WF.MAX_TEMP = :max_temp, 
		           WF.FEELS_LIKE_TEMP = :feels_like_temp, WF.WEATHER_DESC = :weather_desc, WF.WEATHER_ICON_ID = :weather_icon_id, 
				   WF.HUMIDITY = :humidity, WF.WIND_SPEED = :wind_speed, WF.POP = :pop, WF.MOD_DT = :cur_dt
    WHEN NOT MATCHED THEN
        INSERT (FCST_ID, GU_CD, FCST_DT, TEMP, MIN_TEMP, MAX_TEMP, FEELS_LIKE_TEMP, 
                WEATHER_DESC, WEATHER_ICON_ID, HUMIDITY, WIND_SPEED, POP, CRT_DT) 
        VALUES (:fcst_id, :gu_cd, :fcst_dt, :temp, :min_temp, :max_temp, :feels_like_temp, :weather_desc, :weather_icon_id,
       	        :humidity, :wind_speed, :pop, :cur_dt)
    """

    try:
        cursor.executemany(sql, weather_forecast)
        conn.commit()
        return True, 'success'

    except Exception:
        conn.rollback()
        return False, traceback.format_exc()

def refresh_weather_forecast_data(user, password, host, port, sid):
    '''
    날씨예보 정보를 가져와 DB에 저장하는 주요 로직을 조정하는 메서드 \n
    * 자원 반납 수행
    :param user: 사용자 이름
    :param password: 비밀번호
    :param host: 호스트 이름
    :param port: 포트
    :param sid: 서비스 이름
    :return:
    '''

    try:

        conn, cursor = connect_oracle_safety_master(user, password, host, port, sid)
        # conn, cursor 가 None 일 경우(DB 연결 중 예외 발생 시) 예외 발생
        if conn is None or cursor is None:
            raise oracledb.Error('DB 접속 중 에러 발생')

        gu_info = select_gu_info(cursor)
        # gu_info 가 None 일 경우 예외 발생
        if len(gu_info) == 0:
            raise Exception('DB 조회 결과 gu_info 가 없습니다.')

        weather_forecast = get_weather_forecast_fromapi(gu_info)
        # weather_forecast 가 None 일 경우 예외 발생
        if len(weather_forecast) == 0:
            raise Exception('날씨 예보 API 응답 결과가 없습니다.')

        result, message = insert_weather_forecast(conn, cursor, weather_forecast)
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
        refresh_weather_forecast_data(user, password, host, port, sid)
        with open("./log/wf_success_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_weather_forecast_data 작업 완료')  # 성공 메시지 기록
            f.close()
    except Exception as e:
        with open("./log/wf_error_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_weather_forecast_data 작업중 오류 발생')  # 오류 메시지 기록
            f.write('\n' + traceback.format_exc())  # 오류 메시지 기록
            f.close()


if __name__ == '__main__':
    main()
