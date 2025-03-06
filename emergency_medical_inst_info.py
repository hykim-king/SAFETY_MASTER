import traceback

import oracledb
import requests
import xmltodict

import gu_info
import kst
from openweatherAPI_wc import connect_oracle_safety_master


def get_emergency_medical_inst_info_fromapi(stage1):
    """
    공공데이터포털 API로 부터 서울권역의 응급의료기관 정보를 가져오는 메서드 \n
    * 예외 발생시 None 반환
    :param stage1: 주소(시도)
    :return: emergency_medical_inst_info (딕셔너리가 담겨져 있는 리스트), message (예외 메시지)
    """

    # 응급의료기관 정보를 담을 리스트
    emergency_medical_inst_info = []

    appid = 'JZERZAcyD%2FXIwOtiFrU%2Fu74Rn0O4K1hKx%2BhVqF2Td%2B6cFKaa6T1Kk13Hz%2B5P%2FnOtMbdmA2VFRmxNdJ9vL8KhbA%3D%3D'
    numofrows = 1000

    url = f"http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire?serviceKey={appid}&STAGE1={stage1}&pageNo=1&numOfRows={numofrows}"

    try:

        # 응답 데이터(xml 형식)
        data_xml = requests.get(url).text

        # 응답 데이터가 없으면 예외 발생
        if not data_xml:
            raise Exception('응답 데이터가 없습니다.')

        else :
            # xml -> json 파싱
            data_json = xmltodict.parse(data_xml)

            # 결과 코드
            result_code = data_json['response']['header']['resultCode']

            # 조회 건수
            total_cnt = data_json['response']['body']['totalCount']

            # 결과 코드가 성공이 아니거나 조회 건수가 0 이면 예외 발생
            if result_code != '00':
                raise Exception('결과 코드가 성공이 아닙니다.')

            elif total_cnt == '0':
                raise Exception('응답 건수가 0건 입니다.')

            else :

                data = data_json['response']['body']['items']['item']

                # 응급의료기관 기관코드를 담을 리스트
                hpid_list = []

                for elem in data:
                    hpid_list.append(elem['hpid'])

                for hpid in hpid_list:

                    em_inst = {}

                    url = f'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytBassInfoInqire?serviceKey={appid}&HPID={hpid}&pageNo=1&numOfRows=10'

                    data_xml = requests.get(url).text

                    # 응답 데이터가 없으면 현재 반복 건너뛰기
                    if not data_xml:
                        continue

                    data_json = xmltodict.parse(data_xml)

                    # 결과 코드
                    result_code = data_json['response']['header']['resultCode']

                    # 조회 건수
                    total_cnt = data_json['response']['body']['totalCount']

                    # 결과 코드가 성공이 아니거나 조회 건수가 0 이면 현재 반복 건너뛰기
                    if result_code != '00' or total_cnt == '0':
                        continue

                    else :
                        data = data_json['response']['body']['items']['item']

                        em_inst['hpid'] = data['hpid']
                        em_inst['gu_cd'] = gu_info.gu_cd_from_gu_nm(data['dutyAddr'].split(' ')[1])
                        em_inst['duty_nm'] = data['dutyName']
                        em_inst['duty_addr'] = data['dutyAddr']
                        em_inst['duty_tel'] = data['dutyTel1']
                        em_inst['er_tel'] = data['dutyTel3']
                        em_inst['cur_dt'] = kst.cur_time_kst()

                        emergency_medical_inst_info.append(em_inst)

    except Exception:
        return None, traceback.format_exc()

    return emergency_medical_inst_info, 'success'

def insert_emergency_medical_inst_info(conn, cursor, emergency_medical_inst_info):
    '''
    API에서 가져온 응급의료기관 정보들을 DB에 INSERT 하는 메서드 \n
    * 예외 발생시 False 반환 \n
    * 성공 시 커밋, 실패 시 롤백
    :param conn:
    :param cursor:
    :param emergency_medical_inst_info: 응급의료기관 정보가 딕셔너리로 담겨져 있는 리스트)
    :return: 성공여부(True|False), message(예외 메시지)
    '''

    sql = """
    MERGE INTO EMERGENCY_MEDICAL_INST_INFO EMI
    USING (SELECT :hpid AS HPID FROM DUAL) NEW_DATA
    ON (EMI.HPID = NEW_DATA.HPID)
    WHEN MATCHED THEN
		UPDATE SET EMI.DUTY_NM = :duty_nm, EMI.DUTY_ADDR = :duty_addr, EMI.DUTY_TEL = :duty_tel, 
		EMI.ER_TEL = :er_tel, EMI.MOD_DT = :cur_dt
    WHEN NOT MATCHED THEN
        INSERT (HPID, GU_CD, DUTY_NM, DUTY_ADDR, DUTY_TEL, ER_TEL, CRT_DT) 
        VALUES (:hpid, :gu_cd, :duty_nm, :duty_addr, :duty_tel, :er_tel, :cur_dt)
    """

    try:
        cursor.executemany(sql, emergency_medical_inst_info)
        conn.commit()
        return True, 'success'

    except Exception:
        conn.rollback()
        return False, traceback.format_exc()

def refresh_emergency_medical_inst_info_data(user, password, host, port, sid, stage1):
    '''
    응급의료기관 정보를 가져와 DB에 저장하는 주요 로직을 조정하는 메서드 \n
    * 자원 반납 수행
    :param user: 사용자 이름
    :param password: 비밀번호
    :param host: 호스트 이름
    :param port: 포트
    :param sid: 서비스 이름
    :param stage1: 주소(시도)
    :return:
    '''

    # 자원 반납을 위한 try-finally 문
    try:

        conn, cursor = connect_oracle_safety_master(user, password, host, port, sid)
        # conn, cursor 가 None 일 경우(DB 연결 중 예외 발생 시) 예외 발생
        if conn is None or cursor is None:
            raise oracledb.Error('DB 접속 중 에러 발생')

        emergency_medical_inst_info, message = get_emergency_medical_inst_info_fromapi(stage1)
        # emergency_medical_inst_info 가 None 일 경우(예외 발생 시) 예외 발생
        if emergency_medical_inst_info is None:
            raise Exception(message)

        result, message = insert_emergency_medical_inst_info(conn, cursor, emergency_medical_inst_info)
        # result 가 False 일 경우(예외 발생 시) 예외 발생
        if not result:
            raise Exception(message)

    # 자원 반납
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

    # 조회할 주소(시도)
    stage1 = '서울특별시'

    try:
        refresh_emergency_medical_inst_info_data(user, password, host, port, sid, stage1)
        print('refresh 성공')


    except Exception as e:
        print('refresh 실패')
        print(traceback.format_exc())

if __name__ == '__main__':
    main()
