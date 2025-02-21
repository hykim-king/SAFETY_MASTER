import requests
import cx_Oracle
import urllib3
import json

# Oracle DB 연결
def get_oracle_connection():
    try:
        # DSN을 makedsn을 통해 생성
        dsn = cx_Oracle.makedsn('192.168.100.30', '1522', service_name='XE')
        connection = cx_Oracle.connect(user='SAMA', password='SAMA1234', dsn=dsn)
        print("DB 연결 성공")
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Database connection error:", e)
        return None

# 데이터베이스에 데이터 삽입
def insert_data_to_db(connection, data):
    try:
        cursor = connection.cursor()

        for item in data:
            # API에서 받은 데이터에서 각 필드 값 추출
            sn = item.get('SN', None)
            crt_dt = item.get('CRT_DT', None)
            msg_cn = item.get('MSG_CN', None)
            rcptn_rgn_nm = item.get('RCPTN_RGN_NM', None)
            emrg_step_nm = item.get('EMRG_STEP_NM', None)
            dst_se_nm = item.get('DST_SE_NM', None)
            reg_ymd = item.get('REG_YMD', None)
            mdfcn_ymd = item.get('MDFCN_YMD', None)

            # 'SN' 필드가 None 또는 비어있는 경우 처리
            if sn is None or sn == "":
                print(f"잘못된 데이터: SN 값이 없습니다. 건너뜁니다.")
                continue  # 데이터를 건너뛰고 다음 항목으로 진행


            # 삽입될 데이터 출력 (디버깅을 위한 로그)
            print(f"삽입될 데이터: {sn}, {crt_dt}, {msg_cn}, {rcptn_rgn_nm}, {emrg_step_nm}, {dst_se_nm}, {reg_ymd}, {mdfcn_ymd}")
            # INSERT 쿼리 작성
            cursor.execute("""
                INSERT INTO DISASTER_MESSAGE (
                    DIS_MES_NUM, DIS_MES_DT, DIS_MES_CON, DIS_MES_AREA, 
                    DIS_MES_LEVEL, DIS_MES_TYPE, DIS_MES_CREATE_DT, DIS_MES_UPDATED_DT
                ) 
                VALUES (
                    :sn, :crt_dt, :msg_cn, :rcptn_rgn_nm, 
                    :emrg_step_nm, :dst_se_nm, :reg_ymd, :mdfcn_ymd
                )
            """,
                           sn=sn, crt_dt=crt_dt, msg_cn=msg_cn, rcptn_rgn_nm=rcptn_rgn_nm,
                           emrg_step_nm=emrg_step_nm, dst_se_nm=dst_se_nm,
                           reg_ymd=reg_ymd, mdfcn_ymd=mdfcn_ymd)


        # 커밋하여 데이터 저장
        connection.commit()
        print("데이터 삽입 성공!")
    except cx_Oracle.DatabaseError as e:
        print("데이터 삽입 오류:", e)
        connection.rollback()

# URL 및 파라미터 설정
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://www.safetydata.go.kr/V2/api/DSSP-IF-00247"
serviceKey = "N9CZ93UL56TDHH6B"
payloads = {
    "serviceKey": serviceKey,
    "returnType": "json",
    "pageNo": "1",  # 페이지 번호
    "numOfRows": "1000",  # 한 번에 가져올 데이터 개수
    "crtDt": "20230916"  # 기준 날짜
}

# 페이지 번호를 1부터 25까지 반복
for page_no in range(26, 27):
    payloads["pageNo"] = str(page_no)  # 페이지 번호 설정
    print(f"페이지 {page_no} 데이터 가져오기...")

    # 데이터 받아오기
    response = requests.get(url, params=payloads, verify=False)  # SSL 인증 경고 무시
    if response.status_code == 200:
        try:
            # API에서 JSON 응답을 추출
            json_response = response.json()
            print("응답 데이터:", json_response)  # 응답 데이터 전체를 출력해봅니다.

            # 응답에서 'body' 키가 데이터가 포함된 곳으로 보임
            if 'body' in json_response and json_response['body'] is not None:
                data = json_response['body']
                print(f"가져온 데이터 개수: {len(data)}")  # 받은 데이터 개수를 확인

                # DB 연결
                connection = get_oracle_connection()
                if connection:
                    # DB에 데이터 삽입
                    insert_data_to_db(connection, data)  # 여기서 connection과 data를 인자로 전달
                    connection.close()
            else:
                print("응답에 'body' 키가 존재하지 않거나 데이터가 없음.")
        except json.JSONDecodeError:
            print("응답 데이터가 JSON 형식이 아닙니다.")
    else:
        print(f"API 요청 실패. 상태 코드: {response.status_code}")