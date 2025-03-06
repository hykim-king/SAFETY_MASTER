import traceback

import oracledb
import requests
import xmltodict

import kst
from openweatherAPI_wc import connect_oracle_safety_master


def get_er_bed_info_current_fromapi(stage1):
    """
    공공데이터포털 API로 부터 서울 권역의 응급실 가용병상 정보를 가져오는 메서드 \n
    * 예외 발생시 None 반환
    :param stage1: 주소(시도)
    :return: er_bed_info (딕셔너리가 담겨져 있는 리스트), message (예외 메시지)
    """

    # 응급실 가용병상 정보를 담을 리스트
    er_bed_info = []

    appid = 'JZERZAcyD%2FXIwOtiFrU%2Fu74Rn0O4K1hKx%2BhVqF2Td%2B6cFKaa6T1Kk13Hz%2B5P%2FnOtMbdmA2VFRmxNdJ9vL8KhbA%3D%3D'
    numofrows = 1000

    url = f"http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire?serviceKey={appid}&STAGE1={stage1}&pageNo=1&numOfRows={numofrows}"

    # 예외 처리
    try:

        # 응답 데이터(xml 형식)
        data_xml = requests.get(url).text

        # 응답 데이터가 없으면 예외 발생
        if not data_xml:
            raise Exception('응답 데이터가 없습니다.')

        else:

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

            else:
                data = data_json['response']['body']['items']['item']


                for elem in data:

                    # 응답 결과의 각 요소에 대해 데이터 정제(결측치 처리)
                    elem = er_bed_data_cleansing(elem)

                    er_bed = {}

                    er_bed['ebi_id'] = elem['hpid']+ elem['hvidate'][0:12]
                    er_bed['hpid'] = elem['hpid']
                    er_bed['hvi_dt'] = kst.kst_from_serial_kst(elem['hvidate'][0:12])
                    er_bed['hvec'] = elem['hvec']
                    er_bed['hvoc'] = elem['hvoc']
                    er_bed['hvcc'] = elem['hvcc']
                    er_bed['hvncc'] = elem['hvncc']
                    er_bed['hvccc'] = elem['hvccc']
                    er_bed['hvicc'] = elem['hvicc']
                    er_bed['hvgc'] = elem['hvgc']
                    er_bed['hv2'] = elem['hv2']
                    er_bed['hv3'] = elem['hv3']
                    er_bed['hv4'] = elem['hv4']
                    er_bed['hv5'] = elem['hv5']
                    er_bed['hv6'] = elem['hv6']
                    er_bed['hv7'] = elem['hv7']
                    er_bed['hv8'] = elem['hv8']
                    er_bed['hv9'] = elem['hv9']
                    er_bed['hv10'] = elem['hv10']
                    er_bed['hv11'] = elem['hv11']
                    er_bed['hvct_yn'] = elem['hvct_yn']
                    er_bed['hvmri_yn'] = elem['hvmri_yn']
                    er_bed['cur_dt'] = kst.cur_time_kst()

                    # 응급실 가용 병상 정보 리스트에 추가
                    er_bed_info.append(er_bed)

    # 예외 포착시 None, 예외 메시지 반환
    except Exception:
        return None, traceback.format_exc()

    return er_bed_info, 'success'

def er_bed_data_cleansing(elem):
    '''
    응급실 가용 병상 정보의 각 요소에 대한 데이터 정제
    * 결측치가 존재할 경우 해당 요소 추가 후 'N' or '0'으로 초기화
    :param elem: 응급실 가용 병상 정보 리스트의 요소
    :return: elem (딕셔너리)
    '''

    keys = ['hpid', 'hvi_dt', 'hvec', 'hvoc', 'hvcc', 'hvncc', 'hvccc', 'hvicc', 'hvgc', 'hv2', 'hv3', 'hv4', 'hv5'
           , 'hv6', 'hv7', 'hv8', 'hv9', 'hv10', 'hv11', 'hvct_yn', 'hvmri_yn']
    for key in keys:
        if not elem.get(key):

            if key.endswith('yn'):
                elem[key] = 'N'
            else:
                elem[key] = '0'

    return elem



def insert_er_bed_info(conn, cursor, er_bed_info):
    '''
    API에서 가져온 응급실 가용병상 정보들을 DB에 INSERT 하는 메서드 \n
    * 예외 발생시 False 반환 \n
    * 성공 시 커밋, 실패 시 롤백
    :param conn:
    :param cursor:
    :param er_bed_info: 응급실 가용병상 정보가 딕셔너리로 담겨져 있는 리스트)
    :return: 성공여부(True|False), message(예외 메시지)
    '''

    sql = """
    MERGE INTO ER_BED_INFO EBI
    USING (SELECT :ebi_id AS EBI_ID FROM DUAL) NEW_DATA
    ON (EBI.EBI_ID = NEW_DATA.EBI_ID)
    WHEN MATCHED THEN
		UPDATE SET EBI.HVEC = :hvec, EBI.HVOC = :hvoc, EBI.HVCC = :hvcc, EBI.HVNCC = :hvncc, EBI.HVCCC = :hvccc
		     , EBI.HVICC = :hvicc, EBI.HVGC = :hvgc, EBI.HV2 = :hv2, EBI.HV3 = :hv3, EBI.HV4 = :hv4, EBI.HV5 = :hv5
			 , EBI.HV6 = :hv6, EBI.HV7 = :hv7, EBI.HV8 = :hv8, EBI.HV9 = :hv9, EBI.HV10 = :hv10, EBI.HV11 = :hv11
			 , EBI.HVCT_YN = :hvct_yn, EBI.HVMRI_YN = :hvmri_yn, EBI.MOD_DT = :cur_dt
    WHEN NOT MATCHED THEN
        INSERT (EBI_ID, HPID, HVI_DT, HVEC, HVOC, HVCC, HVNCC, HVCCC, HVICC, HVGC, HV2, HV3, HV4
		      , HV5, HV6, HV7, HV8, HV9, HV10, HV11, HVCT_YN, HVMRI_YN, CRT_DT)
        VALUES (:ebi_id, :hpid, :hvi_dt, :hvec, :hvoc, :hvcc, :hvncc, :hvccc, :hvicc, :hvgc, :hv2, :hv3, :hv4
		      , :hv5, :hv6, :hv7, :hv8, :hv9, :hv10, :hv11, :hvct_yn, :hvmri_yn, :cur_dt)"""

    try:
        cursor.executemany(sql, er_bed_info)
        conn.commit()
        return True, 'success'

    except Exception:
        conn.rollback()
        return False, traceback.format_exc()


def refresh_er_bed_info_data(user, password, host, port, sid, stage1):
    '''
    응급실 가용병상 정보를 가져와 DB에 저장하는 주요 로직을 조정하는 메서드 \n
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

        er_bed_info, message = get_er_bed_info_current_fromapi(stage1)
        # er_bed_info 가 None 일 경우(예외 발생 시) 예외 발생
        if er_bed_info is None:
            raise Exception(message)

        result, message = insert_er_bed_info(conn, cursor, er_bed_info)
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
        refresh_er_bed_info_data(user, password, host, port, sid, stage1)
        with open("./log/ebc_success_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_er_bed_info_data 작업 완료')  # 성공 메시지 기록
            f.close()

    except Exception as e:
        with open("./log/ebc_error_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_er_bed_info_data 작업중 오류 발생')  # 오류 메시지 기록
            f.write('\n' + traceback.format_exc())  # 오류 메시지 기록
            f.close()

if __name__ == '__main__':
    main()
