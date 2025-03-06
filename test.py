import traceback

import requests
import oracledb

import kst
from openweatherAPI_wc import connect_oracle_safety_master, select_gu_info


def get_weather_forecast_fromapi():
    """
    OpenWeatherMap API로 부터 자치구별 날씨예를 가져오는 메서드
    :param gu_info: 자치구별 구코드, 위도, 경도 정보가 담겨 있는 튜플이 담긴 리스트
    :return: current_weather (딕셔너리가 담겨져 있는 리스트)
    """

    # 모든 자치구의 현재날씨 정보를 담을 리스트
    current_weather = []

    # 모든 자치구 정보가 담긴 리스트를 순회

    gu = ['111261', '37.517968161172', '127.047059839521']

    gu_cd = gu[0]
    lat = gu[1]
    lon = gu[2]

    appid = 'cb8af55639b6799776fe6d104fa3b416'
    units = 'metric'
    lang = 'kr'
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={appid}&units={units}&lang={lang}"

    data = requests.get(url).json()

    for wf in data['list']:
        # 각 자치구의 현재날씨 정보를 담을 딕셔너리
        gu_forecast = {}

        gu_forecast['fcst_id'] = gu_cd + kst.kst_serial_from_unix(wf['dt'])
        gu_forecast['gu_cd'] = gu_cd
        gu_forecast['fcst_dt'] = kst.kst_from_unix(wf['dt'])
        gu_forecast['temp'] = wf['main']['temp']
        gu_forecast['min_temp'] = wf['main']['temp_min']
        gu_forecast['max_temp'] = wf['main']['temp_max']
        gu_forecast['feels_like_temp'] = wf['main']['feels_like']
        gu_forecast['weather_desc'] = wf['weather'][0]['description']
        gu_forecast['weather_icon_id'] = wf['weather'][0]['icon']
        gu_forecast['humidity'] = wf['main']['humidity']
        gu_forecast['wind_speed'] = wf['wind']['speed']
        gu_forecast['pop'] = wf['pop']
        gu_forecast['crt_dt'] = kst.cur_time_kst()

        current_weather.append(gu_forecast)

    return current_weather

def insert_weather_current(conn, cursor, current_weather):
    '''
    API에서 가져온 현재 날씨 정보를 DB에 INSERT 하는 메서드
    :param conn:
    :param cursor:
    :param current_weather: 자치구별 현재날씨 정보가 딕셔너리로 담겨져 있는 리스트)
    :return:
    '''

    #for gu_cd in current_weather:
        # sql = """INSERT INTO WEATHER_CURRENT (WEATHER_ID, GU_CD, TEMP, MIN_TEMP, MAX_TEMP, FEELS_LIKE_TEMP,
        #                                       WEATHER_DESC, WEATHER_ICON_ID, HUMIDITY, WIND_SPEED, MS_DT, CRT_DT)
        #                               VALUES (:weather_id, :gu_cd, :temp, :min_temp, :max_temp, :feels_like_temp,
        #                                       :weather_desc, :weather_icon_id, :humidity, :wind_speed, :ms_dt, :crt_dt)"""

    sql = """
    MERGE INTO WEATHER_CURRENT WC
    USING (SELECT :weather_id AS WEATHER_ID FROM DUAL) NEW_DATA
    ON (WC.WEATHER_ID = NEW_DATA.WEATHER_ID)
    WHEN MATCHED THEN
		UPDATE SET WC.TEMP = :temp, WC.MIN_TEMP = :min_temp, WC.MAX_TEMP = :max_temp, WC.FEELS_LIKE_TEMP = :feels_like_temp,
		      	   WC.WEATHER_DESC = :weather_desc, WC.WEATHER_ICON_ID = :weather_icon_id, WC.HUMIDITY = :humidity, 
				   WC.WIND_SPEED = :wind_speed, WC.MS_DT = :ms_dt, WC.CRT_DT = :crt_dt
    WHEN NOT MATCHED THEN
        INSERT (WEATHER_ID, GU_CD, TEMP, MIN_TEMP, MAX_TEMP, FEELS_LIKE_TEMP, 
                WEATHER_DESC, WEATHER_ICON_ID, HUMIDITY, WIND_SPEED, MS_DT, CRT_DT) 
        VALUES (:weather_id, :gu_cd, :temp, :min_temp, :max_temp, :feels_like_temp, :weather_desc, :weather_icon_id,
       	        :humidity, :wind_speed, :ms_dt, :crt_dt)
    """

    cursor.executemany(sql, current_weather)
    conn.commit()

def refresh_weather_data(user, password, host, port, sid):
    '''
    현재 날씨 정보를 가져와 DB에 저장하는 주요 로직을 조정하는 메서드
    :param user: 사용자 이름
    :param password: 비밀번호
    :param host: 호스트 이름
    :param port: 포트
    :param sid: 서비스 이름
    :return:
    '''

    conn, cursor = connect_oracle_safety_master(user, password, host, port, sid)

    gu_info = select_gu_info(cursor)

    current_weather = get_current_weather_fromapi(gu_info)

    insert_weather_current(conn, cursor, current_weather)

    cursor.close()
    conn.close()
    print('연결해제')

def main():

    # user = "SAMA"
    # password = "SAMA1234"
    # host = '192.168.100.30'
    # port = 1522
    # sid = 'XE'
    #
    # try:
    #     refresh_weather_data(user, password, host, port, sid)
    #     with open("success_log.txt", "w", encoding="utf-8") as f:
    #         f.write(f'{kst.cur_time_kst()} refresh_weather_data 작업 완료')  # 성공 메시지 기록
    # except Exception as e:
    #     with open("error_log.txt", "w", encoding="utf-8") as f:
    #         f.write(traceback.format_exc())  # 오류 메시지 기록

    wf = get_weather_forecast_fromapi()

    for a in wf:
        print(a)



if __name__ == '__main__':
    main()
