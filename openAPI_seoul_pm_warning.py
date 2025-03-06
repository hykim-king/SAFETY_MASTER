import traceback

import oracledb
import requests

import kst
from openweatherAPI_wc import connect_oracle_safety_master


def get_pm_warning_fromapi(years):
    """
    공공데이터포털 API로 부터 서울의 미세먼지 경보 발령 내역을 가져오는 메서드
    :param years: 발령 내역을 조회할 년도 (리스트)
    :return: pm_warnings (딕셔너리가 담겨져 있는 리스트)
    """

    # 서울의 미세먼지 경보 발령 내역을 담을 리스트
    pm_warnings = []

    appid = 'JZERZAcyD%2FXIwOtiFrU%2Fu74Rn0O4K1hKx%2BhVqF2Td%2B6cFKaa6T1Kk13Hz%2B5P%2FnOtMbdmA2VFRmxNdJ9vL8KhbA%3D%3D'
    numofrows = 1000

    # 년도 리스트를 순회
    for year in years:

        url = f"http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo?serviceKey={appid}&returnType=json&numOfRows={numofrows}&pageNo=1&year={year}"


        try:
            # 응답 데이터
            data_json = requests.get(url).json()

            # 응답 데이터가 없으면 예외 발생
            if not data_json:
                raise Exception('응답 데이터가 없습니다.')

            else :

                # 결과 코드
                result_code = data_json['response']['header']['resultCode']

                # 조회 건수
                total_cnt = data_json['response']['body']['totalCount']

                if result_code != '00':
                    raise Exception('결과 코드가 성공이 아닙니다.')

                elif total_cnt == '0':
                    raise Exception('응답 건수가 0건 입니다.')

                else :

                    data = data_json['response']['body']['items']

                    # 응답 데이터를 순회하며 서울 지역 데이터만 추출
                    for elem in data:
                        if elem['districtName'] == '서울':

                            # 발령된 각 경보에 대한 정보를 담을 딕셔너리
                            pm_warning = {}

                            pm_warning['warn_id']  = elem['issueDate'].replace('-', '') + elem['issueTime'].replace(':', '') + elem['itemCode']
                            pm_warning['sn'] = elem['sn']
                            pm_warning['dist_nm'] = elem['districtName']
                            pm_warning['move_nm'] = elem['moveName']
                            pm_warning['issue_item'] = elem['itemCode']
                            pm_warning['issue_gbn'] = elem['issueGbn']
                            pm_warning['issue_conc'] = elem['issueVal']
                            pm_warning['issue_dt'] = elem['issueDate'].replace('-', '.') + ' ' + elem['issueTime']
                            pm_warning['clear_dt'] = elem['clearDate'].replace('-', '.') + ' ' + elem['clearTime']
                            pm_warning['cur_dt'] = kst.cur_time_kst()

                            pm_warnings.append(pm_warning)


        # 예외 포착시 None, 예외 메시지 반환
        except Exception:
            return None, traceback.format_exc()


    return pm_warnings, 'success'

def insert_pm_warning_h(conn, cursor, pm_warnings):
    '''
    API에서 가져온 미세먼지 경보 발령 내역들을 DB에 INSERT 하는 메서드\n
    * 예외 발생시 False 반환 \n
    * 성공 시 커밋, 실패 시 롤백
    :param conn:
    :param cursor:
    :param pm_warnings: 서울의 미세먼지 경보 발령 내역 정보가 딕셔너리로 담겨져 있는 리스트)
    :return:
    '''

    sql = """
    MERGE INTO PM_WARNING_H PMW
    USING (SELECT :warn_id AS WARN_ID FROM DUAL) NEW_DATA
    ON (PMW.WARN_ID = NEW_DATA.WARN_ID)
    WHEN MATCHED THEN
		UPDATE SET PMW.DIST_NM = :DIST_NM, PMW.MOVE_NM = :move_nm, PMW.ISSUE_ITEM = :issue_item, PMW.ISSUE_GBN = :issue_gbn,
		      	   PMW.ISSUE_CONC = :issue_conc, PMW.ISSUE_DT = :issue_dt, PMW.CLEAR_DT = :clear_dt, PMW.SN = :sn, PMW.MOD_DT = :cur_dt
    WHEN NOT MATCHED THEN
        INSERT (WARN_ID, DIST_NM, MOVE_NM, ISSUE_ITEM, ISSUE_GBN, ISSUE_CONC, ISSUE_DT, CLEAR_DT, SN, CRT_DT) 
        VALUES (:warn_id, :dist_nm, :move_nm, :issue_item, :issue_gbn, :issue_conc, :issue_dt, :clear_dt, :sn, :cur_dt)
    """

    try:
        cursor.executemany(sql, pm_warnings)
        conn.commit()
        return True, 'success'

    except Exception:
        conn.rollback()
        return False, traceback.format_exc()

def refresh_pm_warning_data(user, password, host, port, sid, years):
    '''
    서울의 미세먼지 경보 발령 내역을 가져와 DB에 저장하는 주요 로직을 조정하는 메서드 \n
    * 자원 반납 수행
    :param years: 조회할 년도
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

        pm_warnings, message = get_pm_warning_fromapi(years)
        # pm_warnings 가 None 일 경우(예외 발생 시) 예외 발생
        if pm_warnings is None:
            raise Exception(message)

        result, message = insert_pm_warning_h(conn, cursor, pm_warnings)
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

    # 조회할 년도
    years = [2025]

    try:
        refresh_pm_warning_data(user, password, host, port, sid, years)

        with open("./log/pmw_success_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_pm_warning_data 작업 완료')  # 성공 메시지 기록
            f.close()

    except Exception as e:

        with open("./log/pmw_error_log.txt", "a", encoding="utf-8") as f:
            f.write(f'\n{kst.cur_time_kst()} refresh_pm_warning_data 작업중 오류 발생')  # 오류 메시지 기록
            f.write('\n' + traceback.format_exc())  # 오류 메시지 기록
            f.close()

if __name__ == '__main__':
    main()
