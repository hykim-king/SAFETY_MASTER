import requests
import cx_Oracle
import urllib3
import json

# Oracle DB 연결
def get_oracle_connection():
    try:
        connection = cx_Oracle.connect("your_username", "your_password", "your_host:your_port/your_service_name")
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Database connection error:", e)
        return None

# 데이터베이스에 데이터 삽입
def insert_data_to_db(connection, data):
    try:
        cursor = connection.cursor()
        for item in data:
            # 필요한 컬럼을 추가합니다.
            crtDt = item.get('crtDt', '')
            some_field1 = item.get('some_field1', '')
            some_field2 = item.get('some_field2', 0)

            # INSERT 쿼리
            cursor.execute("""
                INSERT INTO earthquake_data (crtDt, some_field1, some_field2)
                VALUES (:crtDt, :some_field1, :some_field2)
            """, crtDt=crtDt, some_field1=some_field1, some_field2=some_field2)

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
    "pageNo": "25",  # 페이지 번호
    "numOfRows": "1000",  # 한 번에 가져올 데이터 개수
    "crtDt": "20230916"  # 기준 날짜
}

# 데이터 받아오기
response = requests.get(url, params=payloads, verify=False)  # SSL 인증 경고 무시
if response.status_code == 200:
    try:
        json_response = response.json()
        data = json_response.get('data', [])  # 'data' 키에 데이터를 저장한다고 가정

        # DB 연결
        connection = get_oracle_connection()
        if connection:
            # DB에 데이터 삽입
            insert_data_to_db(connection, data)
            connection.close()
    except json.JSONDecodeError:
        print("응답 데이터가 JSON 형식이 아닙니다.")
else:
    print(f"API 요청 실패. 상태 코드: {response.status_code}")
