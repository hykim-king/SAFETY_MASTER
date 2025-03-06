import requests
import oracledb
import traceback

# Oracle DB 연결 정보
DB_USER = "scott"
DB_PASSWORD = "pcwk"
DB_HOST = "localhost"
DB_PORT = 1521
DB_SID = "XE"

# API URL 설정
API_URL = "https://www.safetydata.go.kr/V2/api/DSSP-IF-00195"
API_KEY = "EW729M3N50O3W79U"  # 서비스 키

def connect_oracle():
    """
    Oracle DB 연결
    """
    dsn = f"{DB_HOST}:{DB_PORT}/{DB_SID}"
    try:
        conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn)
        cursor = conn.cursor()
        print("Oracle DB 연결 성공")
        return conn, cursor
    except oracledb.DatabaseError as e:
        print("DB 연결 실패:", e)
        exit()

def fetch_shelters():
    """
    API에서 대피소 데이터 가져오기 및 필터링
    """
    shelters = []
    pageNo = 1
    numOfRows = 1000  # 페이지당 최대 개수

    while True:
        payloads = {
            "serviceKey": API_KEY,
            "returnType": "json",
            "pageNo": pageNo,
            "numOfRows": numOfRows,
        }
        response = requests.get(API_URL, params=payloads)

        if response.status_code == 200:
            data = response.json()
            page_shelters = data.get("body", [])

            # 데이터가 없으면 종료
            if not page_shelters:
                break

            # '서울특별시' 대피소 필터링
            filtered_shelters = [s for s in page_shelters if "서울특별시" in (s.get("MNG_INST_NM") or "")]

            shelters.extend(filtered_shelters)
            pageNo += 1
        else:
            print("데이터 가져오기 오류:")
            break

    print(f" 총 {len(shelters)}개의 서울특별시 대피소 데이터 추출")
    return shelters

def insert_faclt_data(conn, cursor, shelters):
    """
    FAClT 테이블에 데이터 삽입 (MERGE INTO 사용)
    """
    sql = """
    MERGE INTO FAClT F
    USING (SELECT :FCLT_CD AS FCLT_CD FROM DUAL) NEW_DATA
    ON (F.FCLT_CD = NEW_DATA.FCLT_CD)
    WHEN MATCHED THEN
        UPDATE SET 
            F.SGG_CD = :SGG_CD, F.SE_CD = :SE_CD, F.FCLT_NM = :FCLT_NM, F.FCLT_DSGN_DAY = :FCLT_DSGN_DAY,
            F.FCLT_SE_CD = :FCLT_SE_CD, F.EMD_CD = :EMD_CD, F.EMD_NM = :EMD_NM, 
            F.FCLT_ADDR_LOTNO = :FCLT_ADDR_LOTNO, F.FCLT_SCL = :FCLT_SCL, F.SCL_UNIT = :SCL_UNIT, 
            F.FCLT_ADDR_RONA = :FCLT_ADDR_RONA, F.LOT_PROVIN = :LOT_PROVIN, F.LOT_MIN = :LOT_MIN, 
            F.LOT_SEC = :LOT_SEC, F.LAT_PROVIN = :LAT_PROVIN, F.LAT_MIN = :LAT_MIN, F.LAT_SEC = :LAT_SEC, 
            F.GRND_UDGD_SE = :GRND_UDGD_SE, F.SHNT_PSBLTY_NOPE = :SHNT_PSBLTY_NOPE, F.OPN_YN = :OPN_YN,
            F.MNG_INST_NM = :MNG_INST_NM, F.ORTM_UTLZ_TYPE = :ORTM_UTLZ_TYPE, F.MNG_INST_TELNO = :MNG_INST_TELNO,
            F.ROAD_NM_CD = :ROAD_NM_CD
    WHEN NOT MATCHED THEN
        INSERT (FCLT_CD, SGG_CD, SE_CD, FCLT_NM, FCLT_DSGN_DAY, FCLT_SE_CD, EMD_CD, EMD_NM,
                FCLT_ADDR_LOTNO, FCLT_SCL, SCL_UNIT, FCLT_ADDR_RONA, LOT_PROVIN, LOT_MIN, LOT_SEC, 
                LAT_PROVIN, LAT_MIN, LAT_SEC, GRND_UDGD_SE, SHNT_PSBLTY_NOPE, OPN_YN, MNG_INST_NM, 
                ORTM_UTLZ_TYPE, MNG_INST_TELNO, ROAD_NM_CD) 
        VALUES (:FCLT_CD, :SGG_CD, :SE_CD, :FCLT_NM, :FCLT_DSGN_DAY, :FCLT_SE_CD, :EMD_CD, :EMD_NM,
                :FCLT_ADDR_LOTNO, :FCLT_SCL, :SCL_UNIT, :FCLT_ADDR_RONA, :LOT_PROVIN, :LOT_MIN, :LOT_SEC, 
                :LAT_PROVIN, :LAT_MIN, :LAT_SEC, :GRND_UDGD_SE, :SHNT_PSBLTY_NOPE, :OPN_YN, :MNG_INST_NM, 
                :ORTM_UTLZ_TYPE, :MNG_INST_TELNO, :ROAD_NM_CD)
    """

    data_to_insert = [
        {
            "FCLT_CD": s.get("FCLT_CD"),
            "SGG_CD": s.get("SGG_CD"),
            "SE_CD": s.get("SE_CD"),
            "FCLT_NM": s.get("FCLT_NM"),
            "FCLT_DSGN_DAY": s.get("FCLT_DSGN_DAY"),
            "FCLT_SE_CD": s.get("FCLT_SE_CD"),
            "EMD_CD": s.get("EMD_CD"),
            "EMD_NM": s.get("EMD_NM"),
            "FCLT_ADDR_LOTNO": s.get("FCLT_ADDR_LOTNO"),
            "FCLT_SCL": s.get("FCLT_SCL"),
            "SCL_UNIT": s.get("SCL_UNIT"),
            "FCLT_ADDR_RONA": s.get("FCLT_ADDR_RONA"),
            "LOT_PROVIN": s.get("LOT_PROVIN"),
            "LOT_MIN": s.get("LOT_MIN"),
            "LOT_SEC": s.get("LOT_SEC"),
            "LAT_PROVIN": s.get("LAT_PROVIN"),
            "LAT_MIN": s.get("LAT_MIN"),
            "LAT_SEC": s.get("LAT_SEC"),
            "GRND_UDGD_SE": s.get("GRND_UDGD_SE"),
            "SHNT_PSBLTY_NOPE": s.get("SHNT_PSBLTY_NOPE"),
            "OPN_YN": s.get("OPN_YN"),
            "MNG_INST_NM": s.get("MNG_INST_NM"),
            "ORTM_UTLZ_TYPE": s.get("ORTM_UTLZ_TYPE"),
            "MNG_INST_TELNO": s.get("MNG_INST_TELNO") if s.get("MNG_INST_TELNO") else "정보 없음",
            "ROAD_NM_CD": s.get("ROAD_NM_CD")
        }
        for s in shelters
    ]

    try:
        cursor.executemany(sql, data_to_insert)  # 다중 삽입 실행
        conn.commit()
        print(f" {len(data_to_insert)}개의 시설 데이터 DB에 저장 완료")
    except oracledb.DatabaseError as e:
        print("데이터 삽입 실패:", e)
        conn.rollback()

def main():
    try:
        conn, cursor = connect_oracle()
        shelters = fetch_shelters()
        if shelters:
            insert_faclt_data(conn, cursor, shelters)
        cursor.close()
        conn.close()
        print("DB 연결 종료")
    except Exception as e:
        print("실행 중 오류 발생:", e)
        print(traceback.format_exc())

if __name__ == '__main__':
    main()