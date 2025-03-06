import requests
import oracledb
import traceback
import xml.etree.ElementTree as ET

# 🔹 Oracle DB 연결 정보
DB_USER = "SAMA"
DB_PASSWORD = "SAMA1234"
DB_HOST = "192.168.100.30"
DB_PORT = 1522
DB_SID = "XE"

# 🔹 API URL 설정
API_KEY = "65686358627a697a363042446d4955"
API_URL = f"http://openapi.seoul.go.kr:8088/{API_KEY}/xml/tbClnswspfGnrlStat/1/26/"

def connect_oracle():
    """
    Oracle DB 연결
    """
    dsn = f"{DB_HOST}:{DB_PORT}/{DB_SID}"
    try:
        conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn)
        cursor = conn.cursor()
        print(" Oracle DB 연결 성공")
        return conn, cursor
    except oracledb.DatabaseError as e:
        print(" DB 연결 실패:", e)
        exit()

def fetch_water_facilities():
    """
    API에서 급수시설 데이터를 가져와 반환 (XML → Python 리스트 변환)
    """
    try:
        response = requests.get(API_URL)

        # 응답 상태 코드 확인
        if response.status_code != 200:
            print(f" API 요청 실패: {response.status_code}")
            print("응답 내용:", response.text)
            return None

        print(" API 응답 성공")
        print("응답 내용 일부:", response.text[:500])  # 응답 일부 출력

        # XML 데이터를 파싱하여 리스트로 변환
        return parse_xml(response.text)

    except requests.exceptions.RequestException as e:
        print(" API 요청 중 오류 발생:", e)
        return None

def parse_xml(xml_data):
    """
    XML 데이터를 파싱하여 Python 리스트로 변환
    """
    facilities = []
    root = ET.fromstring(xml_data)

    for row in root.findall(".//row"):  # row 태그 내 데이터 추출
        facility = {
            "SGG": row.find("SGG").text if row.find("SGG") is not None else None,
            "SGG_FCLT": row.find("SGG_FCLT").text if row.find("SGG_FCLT") is not None else None,
            "PUMP_TON_": row.find("PUMP_TON_").text if row.find("PUMP_TON_") is not None else None
        }
        facilities.append(facility)

    print(f"✅ {len(facilities)}개의 급수시설 데이터 변환 완료")
    return facilities

def insert_ewsf_data(conn, cursor, facilities):
    """
    EWSF 테이블에 급수시설 데이터 삽입 (MERGE INTO 사용)
    """
    sql = """
    MERGE INTO EWSF E
    USING (SELECT :SGG AS SGG FROM DUAL) NEW_DATA
    ON (E.SGG = NEW_DATA.SGG AND E.SGG_FCLT = :SGG_FCLT)
    WHEN MATCHED THEN
        UPDATE SET 
            E.PUMP_TON_ = :PUMP_TON_
    WHEN NOT MATCHED THEN
        INSERT (SGG, SGG_FCLT, PUMP_TON_) 
        VALUES (:SGG, :SGG_FCLT, :PUMP_TON_)
    """

    try:
        cursor.executemany(sql, facilities)  # 다중 삽입 실행
        conn.commit()
        print(f"{len(facilities)}개의 급수시설 데이터 DB에 저장 완료")
    except oracledb.DatabaseError as e:
        print("데이터 삽입 실패:", e)
        conn.rollback()

def main():
    try:
        conn, cursor = connect_oracle()
        facilities = fetch_water_facilities()
        if facilities:
            insert_ewsf_data(conn, cursor, facilities)
        cursor.close()
        conn.close()
    except Exception as e:
        print(traceback.format_exc())

if __name__ == '__main__':
    main()
