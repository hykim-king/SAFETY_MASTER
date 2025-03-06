import traceback

import oracledb
import requests

import kst
from openweatherAPI_wc import select_gu_info, connect_oracle_safety_master


def get_airquality_current_fromapi(gu_info):
    """
    서울열린데이터광장 API로 부터 자치구별 대기질 현황을 가져오는 메서드
    :param gu_info: 자치구별 구코드, 위도, 경도 정보가 담겨 있는 튜플이 담긴 리스트
    :return: airquality_current (딕셔너리가 담겨져 있는 리스트)
    """

    # 모든 자치구의 대기질 현황 정보를 담을 리스트
    airquality_current = []

    appid = '75704a72737a657237325665674252'

    # 모든 자치구 정보가 담긴 리스트를 순회
    for gu in gu_info:

        # 각 자치구의 대기질 현황 정보를 담을 딕셔너리
        gu_airquality = {}

        gu_cd = gu[0]

        url = f"http://openAPI.seoul.go.kr:8088/{appid}/json/ListAirQualityByDistrictService/1/15/{gu_cd}"

        try:

            # 응답 데이터
            data_json = requests.get(url).json()

            # 응답 데이터가 없으면 반복문 건너뛰기
            if not data_json:
                continue

            else:

                if data_json['ListAirQualityByDistrictService']['RESULT']['CODE'] != 'INFO-000':
                    continue

                elif data_json['ListAirQualityByDistrictService']['list_total_count'] < 1:
                    continue

                else :

                    data = data_json['ListAirQualityByDistrictService']['row'][0]

                    # 결측치 처리
                    for key in data.keys():
                        if not data[key] or data[key].find('점검') != -1:
                            data[key] = '-1'

                    gu_airquality['aq_id'] = gu_cd + (data['MSRDATE'])
                    gu_airquality['gu_cd'] = gu_cd
                    gu_airquality['cai_grade'] = data['GRADE']
                    gu_airquality['cai'] = data['MAXINDEX']
                    gu_airquality['pm25_conc'] = data['PM25']
                    gu_airquality['pm10_conc'] = data['PM10']
                    gu_airquality['o3_conc'] = data['OZONE']
                    gu_airquality['ms_dt'] = kst.kst_from_serial_kst(data['MSRDATE'])
                    gu_airquality['cur_dt'] = kst.cur_time_kst()

                    # 대기질 현황 리스트에 딕셔너리로된 각 자치구의 대기질 현황 정보 추가
                    airquality_current.append(gu_airquality)

        except Exception:
            continue

    return airquality_current

def insert_airquality_current(conn, cursor, airquality_current):
    '''
    API에서 가져온 대기질 현황 정보를 DB에 INSERT 하는 메서드
    :param conn:
    :param cursor:
    :param airquality_current: 자치구별 대기질 현항 정보가 딕셔너리로 담겨져 있는 리스트)
    :return: 성공여부(True|False), message(예외 메시지)
    '''

    sql = """
    MERGE INTO AIR_QUALITY_CURRENT AQ
    USING (SELECT :aq_id AS AQ_ID FROM DUAL) NEW_DATA
    ON (AQ.AQ_ID = NEW_DATA.AQ_ID)
    WHEN MATCHED THEN
		UPDATE SET AQ.CAI_GRADE = :cai_grade, AQ.CAI = :cai, AQ.PM25_CONC = :pm25_conc, AQ.PM10_CONC = :pm10_conc,
		      	   AQ.O3_CONC = :o3_conc, AQ.MS_DT = :ms_dt, AQ.MOD_DT = :cur_dt
    WHEN NOT MATCHED THEN
        INSERT (AQ_ID, GU_CD, CAI_GRADE, CAI, PM25_CONC, PM10_CONC, O3_CONC, MS_DT, CRT_DT) 
        VALUES (:aq_id, :gu_cd, :cai_grade, :cai, :pm25_conc, :pm10_conc, :o3_conc, :ms_dt, :cur_dt)
    """

    try:
        cursor.executemany(sql, airquality_current)
        conn.commit()
        return True, 'success'

    except Exception:
        conn.rollback()
        return False, traceback.format_exc()

def refresh_airquality_current_data(user, password, host, port, sid):
    '''
    대기질 현황 정보를 가져와 DB에 저장하는 주요 로직을 조정하는 메서드 \n
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

        airquality_current = get_airquality_current_fromapi(gu_info)
        # airquality_current 가 None 일 경우 예외 발생
        if len(airquality_current) == 0:
            raise Exception('현재 대기질 API 응답 결과가 없습니다.')

        result, message = insert_airquality_current(conn, cursor, airquality_current)
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
        refresh_airquality_current_data(user, password, host, port, sid)
        with open("./log/aqc_success_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_airquality_current_data 작업 완료')  # 성공 메시지 기록
            f.close()
    except Exception as e:
        with open("./log/aqc_error_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_airquality_current_data 작업중 오류 발생')  # 오류 메시지 기록
            f.write('\n' + traceback.format_exc())  # 오류 메시지 기록
            f.close()

if __name__ == '__main__':
    main()
