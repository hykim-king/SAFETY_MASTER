import pandas as pd
import oracledb
import json
import traceback
import os
import win32com.client  # Windows 환경에서 Excel COM API 사용
import chardet  # 인코딩 자동 감지 라이브러리

# Oracle DB 연결 정보
DB_USER = "SAMA"
DB_PASSWORD = "SAMA1234"
DB_HOST = "218.144.130.138"
DB_PORT = 1522
DB_SID = "XE"

# 파일 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE_PATH = os.path.join(current_dir, "한파응급대피소3.xlsx")
CSV_FILE_PATH = os.path.join(current_dir, "한파응급대피소3.csv")
UTF8_CSV_FILE_PATH = os.path.join(current_dir, "한파응급대피소3_utf8.csv")
JSON_FILE_PATH = os.path.join(current_dir, "한파응급대피소3.json")

print("엑셀 파일 경로:", EXCEL_FILE_PATH)


def convert_excel_to_csv_via_com(input_path, output_path):
    """엑셀 파일을 Excel COM API를 사용하여 CSV로 변환"""
    try:
        excel = win32com.client.Dispatch("Excel.Application")
        excel.DisplayAlerts = False
        wb = excel.Workbooks.Open(input_path)
        wb.SaveAs(output_path, FileFormat=6)  # CSV로 저장
        wb.Close(False)
        excel.Quit()
        print("✅ 엑셀을 CSV로 변환 완료:", output_path)
    except Exception as e:
        print("❌ 엑셀 → CSV 변환 실패:", e)
        exit()


# 엑셀을 CSV로 변환
convert_excel_to_csv_via_com(EXCEL_FILE_PATH, CSV_FILE_PATH)

# CSV 파일 존재 여부 확인
if not os.path.exists(CSV_FILE_PATH):
    print(f"❌ 오류: CSV 파일이 생성되지 않았습니다 -> {CSV_FILE_PATH}")
    exit()


def detect_encoding(file_path):
    """파일의 인코딩을 자동으로 감지"""
    try:
        with open(file_path, "rb") as f:
            raw_data = f.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            print(f"🔍 감지된 CSV 파일 인코딩: {encoding}")
            return encoding
    except Exception as e:
        print("❌ 인코딩 감지 실패:", e)
        exit()


def convert_csv_encoding(input_path, output_path):
    """CSV 파일을 UTF-8로 변환"""
    try:
        detected_encoding = detect_encoding(input_path)
        df = pd.read_csv(input_path, encoding=detected_encoding, dtype=str)
        df.to_csv(output_path, index=False, encoding="utf-8-sig")
        print("✅ CSV 인코딩을 UTF-8로 변환 완료:", output_path)
    except Exception as e:
        print("❌ CSV 인코딩 변환 실패:", e)
        exit()


# CSV 인코딩 변환
convert_csv_encoding(CSV_FILE_PATH, UTF8_CSV_FILE_PATH)


def convert_csv_to_json(input_path, output_path):
    """CSV 파일을 JSON으로 변환"""
    try:
        df = pd.read_csv(input_path, encoding="utf-8-sig", dtype=str)
        df.ffill(inplace=True)  # 병합된 셀 자동 채우기

        # OP_TYPE 값이 없으면 "기타"로 설정
        df["OP_TYPE"].fillna("기타", inplace=True)
        df["OP_TYPE"] = df["OP_TYPE"].apply(lambda x: "기타" if pd.isna(x) or x.strip() == "" else x)

        df.to_json(output_path, orient="records", force_ascii=False, indent=4)
        print("✅ CSV를 JSON으로 변환 완료:", output_path)
    except Exception as e:
        print("❌ CSV → JSON 변환 실패:", e)
        exit()


# CSV → JSON 변환
convert_csv_to_json(UTF8_CSV_FILE_PATH, JSON_FILE_PATH)

# JSON 파일 존재 여부 확인
if not os.path.exists(JSON_FILE_PATH):
    print(f"❌ 오류: JSON 파일이 생성되지 않았습니다 -> {JSON_FILE_PATH}")
    exit()


def read_json(file_path):
    """JSON 파일을 로드하여 리스트 반환"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"✅ JSON 데이터 로드 완료: {len(data)}개의 항목")
        return data
    except Exception as e:
        print("❌ JSON 파일 로드 실패:", e)
        exit()


def connect_oracle():
    """Oracle DB 연결"""
    dsn = f"{DB_HOST}:{DB_PORT}/{DB_SID}"
    try:
        conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn)
        cursor = conn.cursor()
        print("✅ Oracle DB 연결 성공")
        return conn, cursor
    except oracledb.DatabaseError as e:
        print("❌ DB 연결 실패:", e)
        exit()


def insert_data(conn, cursor, data):
    """데이터를 Oracle DB에 삽입"""
    sql = """
    MERGE INTO HANPA_EMERGENCY H
    USING (SELECT :SEQ_NO AS SEQ_NO, :SGG AS SGG, :FCLTY_TYPE AS FCLTY_TYPE, 
                  :FCLT_NM AS FCLT_NM, :OP_HOUR AS OP_HOUR, :ADDRESS AS ADDRESS, 
                  :CONTACT_NM AS CONTACT_NM, :OP_TYPE AS OP_TYPE FROM DUAL) NEW_DATA
    ON (H.SEQ_NO = NEW_DATA.SEQ_NO)
    WHEN MATCHED THEN
        UPDATE SET 
            H.SGG = NEW_DATA.SGG, H.FCLTY_TYPE = NEW_DATA.FCLTY_TYPE, H.FCLT_NM = NEW_DATA.FCLT_NM,
            H.OP_HOUR = NEW_DATA.OP_HOUR, H.ADDRESS = NEW_DATA.ADDRESS, H.CONTACT_NM = NEW_DATA.CONTACT_NM, H.OP_TYPE = NEW_DATA.OP_TYPE
    WHEN NOT MATCHED THEN
        INSERT (SEQ_NO, SGG, FCLTY_TYPE, FCLT_NM, OP_HOUR, ADDRESS, CONTACT_NM, OP_TYPE) 
        VALUES (NEW_DATA.SEQ_NO, NEW_DATA.SGG, NEW_DATA.FCLTY_TYPE, NEW_DATA.FCLT_NM, 
                NEW_DATA.OP_HOUR, NEW_DATA.ADDRESS, NEW_DATA.CONTACT_NM, NEW_DATA.OP_TYPE)
    """

    # 데이터 변환 (dict → tuple)
    data_to_insert = [
        (
            row["SEQ_NO"],
            row["SGG"],
            row["FCLTY_TYPE"],
            row["FCLT_NM"],
            row["OP_HOUR"],
            row.get("ADDRESS", None),  # NULL 허용
            row.get("CONTACT_NM", None),  # NULL 허용
            row.get("OP_TYPE", "기타")  # ✅ 기본값 "기타" 설정
        )
        for row in data
    ]

    try:
        cursor.executemany(sql, data_to_insert)
        conn.commit()
        print(f"✅ {len(data_to_insert)}개의 데이터가 성공적으로 삽입됨")
    except oracledb.DatabaseError as e:
        print("❌ 데이터 삽입 실패:", e)
        conn.rollback()


def main():
    try:
        conn, cursor = connect_oracle()
        data = read_json(JSON_FILE_PATH)
        if data:
            insert_data(conn, cursor, data)
        cursor.close()
        conn.close()
        print("✅ DB 연결 종료")
    except Exception as e:
        print("❌ 실행 중 오류 발생:", e)
        print(traceback.format_exc())


if __name__ == '__main__':
    main()
