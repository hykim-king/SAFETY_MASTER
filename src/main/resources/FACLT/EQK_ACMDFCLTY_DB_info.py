import requests
import oracledb
import traceback

# Oracle DB 연결 정보
DB_USER = "SAMA"
DB_PASSWORD = "SAMA1234"
DB_HOST = "218.144.130.138"
DB_PORT = 1522
DB_SID = "XE"

# API URL 설정
API_URL = "https://www.safetydata.go.kr/V2/api/DSSP-IF-10943"
API_KEY = "7TML53MMO8B79RL6"  # 서비스 키

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
    API에서 대피소 데이터 가져오기
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

            shelters.extend(page_shelters)
            pageNo += 1
        else:
            print("데이터 가져오기 오류: HTTP", response.status_code)
            break


    print(f" 총 {len(shelters)}개의 대피소 데이터 추출")
    return shelters

def insert_shelter_data(conn, cursor, shelters):
    """
    EQK_ACMDFCLTY 테이블에 데이터 삽입 (MERGE INTO 사용)
    """
    sql = """
    MERGE INTO EQK_ACMDFCLTY E
    USING (SELECT :VT_ACMDFCLTY_NM AS VT_ACMDFCLTY_NM FROM DUAL) NEW_DATA
    ON (E.VT_ACMDFCLTY_NM = NEW_DATA.VT_ACMDFCLTY_NM)
    WHEN MATCHED THEN
        UPDATE SET 
            E.ARCD = :ARCD, E.ACMDFCLTY_SN = :ACMDFCLTY_SN, E.HDONG_CD = :HDONG_CD,
            E.ACMD_BULD_MNG_NO = :ACMD_BULD_MNG_NO, E.DTL_ADRES = :DTL_ADRES, 
            E.VT_ACMD_PSBIL_NMPR = :VT_ACMD_PSBIL_NMPR, E.FCLTY_AR = :FCLTY_AR, 
            E.BDONG_CD = :BDONG_CD, E.RN_DTL_ADRES = :RN_DTL_ADRES, 
            E.USE_SE_CD = :USE_SE_CD, E.LO = :LO, E.LA = :LA, 
            E.EQK_ACMDFCLTY_ADRES = :EQK_ACMDFCLTY_ADRES
    WHEN NOT MATCHED THEN
        INSERT (VT_ACMDFCLTY_NM, ARCD, ACMDFCLTY_SN, HDONG_CD, ACMD_BULD_MNG_NO, DTL_ADRES, 
                VT_ACMD_PSBIL_NMPR, FCLTY_AR, BDONG_CD, RN_DTL_ADRES, 
                USE_SE_CD, LO, LA, EQK_ACMDFCLTY_ADRES) 
        VALUES (:VT_ACMDFCLTY_NM, :ARCD, :ACMDFCLTY_SN, :HDONG_CD, :ACMD_BULD_MNG_NO, :DTL_ADRES, 
                :VT_ACMD_PSBIL_NMPR, :FCLTY_AR, :BDONG_CD, :RN_DTL_ADRES, 
                :USE_SE_CD, :LO, :LA, :EQK_ACMDFCLTY_ADRES)
    """

    data_to_insert = []
    for s in shelters:
        VT_ACMDFCLTY_NM = s.get("VT_ACMDFCLTY_NM", "").strip()  # 공백 제거 후 값 가져오기
        if not VT_ACMDFCLTY_NM:  # NULL 또는 빈 문자열이면 기본값 설정
            VT_ACMDFCLTY_NM = "정보 없음"

        data_to_insert.append({
            "VT_ACMDFCLTY_NM": VT_ACMDFCLTY_NM,
            "ARCD": s.get("ARCD", "정보 없음"),
            "ACMDFCLTY_SN": s.get("ACMDFCLTY_SN", "정보 없음"),
            "HDONG_CD": s.get("HDONG_CD", "정보 없음"),
            "ACMD_BULD_MNG_NO": s.get("ACMD_BULD_MNG_NO") if s.get("ACMD_BULD_MNG_NO") else "정보 없음",
            "DTL_ADRES": s.get("DTL_ADRES") if s.get("DTL_ADRES") else "정보 없음",
            "VT_ACMD_PSBIL_NMPR": s.get("VT_ACMD_PSBL_NMPR", "정보 없음"),
            "FCLTY_AR": s.get("FCLTY_AR", "정보 없음"),
            "BDONG_CD": s.get("BDONG_CD", "정보 없음"),
            "RN_DTL_ADRES": s.get("RN_DTL_ADRES") if s.get("RN_DTL_ADRES") else "정보 없음",
            "USE_SE_CD": s.get("USE_SE_CD", "정보 없음"),
            "LO": s.get("LO", "0.0"),  # 경도 값이 없으면 기본값 0.0
            "LA": s.get("LA", "0.0"),  # 위도 값이 없으면 기본값 0.0
            "EQK_ACMDFCLTY_ADRES": s.get("EQK_ACMDFCLTY_ADRES", "정보 없음"),
        })

    # 삽입할 데이터 확인
    print("DB에 삽입할 데이터 예시:", data_to_insert[:5])

    try:
        cursor.executemany(sql, data_to_insert)  # 다중 삽입 실행
        conn.commit()
        print(f" {len(data_to_insert)}개의 대피소 데이터 DB에 저장 완료")
    except oracledb.DatabaseError as e:
        print("데이터 삽입 실패:", e)
        conn.rollback()


def main():
    try:
        conn, cursor = connect_oracle()
        shelters = fetch_shelters()
        if shelters:
            insert_shelter_data(conn, cursor, shelters)
        cursor.close()
        conn.close()
        print("DB 연결 종료")
    except Exception as e:
        print("실행 중 오류 발생:", e)
        print(traceback.format_exc())

if __name__ == '__main__':
    main()