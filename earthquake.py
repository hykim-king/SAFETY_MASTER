import requests
import cx_Oracle
import schedule
import time
import datetime

def batch_task():
    now = datetime.datetime.now()
    print(f"🔹 배치 작업 실행: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # 여기에 실행할 코드 추가

    # URL 문자열
    url = 'https://apihub.kma.go.kr/api/typ01/url/eqk_list.php?tm1=201511231215&tm2=202503011215&disp=1&help=1&authKey=X4kLr7YTTFWJC6-2E7xVYw'

    # GET 요청
    response = requests.get(url)

    # 응답 상태 코드 확인
    if response.status_code == 200:
        try:
            # 응답을 텍스트로 변환
            response_text = response.text

            # 응답이 텍스트 형식인 경우, 데이터를 줄 단위로 처리
            lines = response_text.splitlines()

            # Oracle DB 연결
            def get_oracle_connection():
                try:
                    dsn = cx_Oracle.makedsn('192.168.100.30', '1522', service_name='XE')
                    connection = cx_Oracle.connect(user='SAMA', password='SAMA1234', dsn=dsn)
                    print("DB 연결 성공")
                    return connection
                except cx_Oracle.DatabaseError as e:
                    print("Database connection error:", e)
                    return None

            # DB 연결 얻기
            conn = get_oracle_connection()

            if conn is None:
                print("DB 연결 실패")
                exit()

            # 데이터를 EARTHQUAKE2 테이블에 삽입
            cursor = conn.cursor()

            for line in lines:
                # 각 줄을 ',' 기준으로 나누어 데이터 추출
                data = line.split(',')
                if len(data) < 12:
                    continue  # 데이터가 부족한 줄은 건너뛰기

                # ','로 데이터를 나누기 전에 필요한 값을 추출하여 변수에 저장
                EQK_AREA__REGION = int(data[0])  # 첫 번째 항목: EQK_AREA__REGION
                EQK_REPORT_TIME = data[1]  # 두 번째 항목: EQK_REPORT_TIME
                EQK_ORIGIN_TIME = data[3]  # 네 번째 항목: EQK_ORIGIN_TIME
                EQK_MT = float(data[4])  # 다섯 번째 항목: EQK_MT
                EQK_LAT = float(data[5])  # 여섯 번째 항목: EQK_LAT
                EQK_LON = float(data[6])  # 일곱 번째 항목: EQK_LON
                EQK_LOC = data[7]  # 여덟 번째 항목: EQK_LOC
                EQK_INTENSITY = None  # EQK_INTENSITY는 null로 설정
                EQK_COMMENTS = data[9]  # EQK_COMMENTS
                EQK_UPDATE = None  # EQK_UPDATE는 빈 값으로 설정
                EQK_ORIGIN_MSC = data[10]  # EQK_ORIGIN_MSC (API에서 데이터의 끝이라 가정)

                # 시퀀스를 사용하여 EQK_NUM 자동 생성
                cursor.execute("SELECT EQK_NUM_SEQ.NEXTVAL FROM DUAL")
                EQK_NUM = cursor.fetchone()[0]  # 시퀀스에서 다음 값을 가져옴

                # 삽입 쿼리 작성
                insert_query = """
                MERGE INTO EARTHQUAKE T
                USING (SELECT :EQK_REPORT_TIME AS EQK_REPORT_TIME, :EQK_ORIGIN_TIME AS EQK_ORIGIN_TIME FROM DUAL) S
                ON (T.EQK_ORIGIN_TIME = S.EQK_ORIGIN_TIME)  -- EQK_ORIGIN_TIME을 기준으로 중복 확인
                WHEN MATCHED THEN
                    UPDATE SET 
                        T.EQK_MT = :EQK_MT,
                        T.EQK_LAT = :EQK_LAT,
                        T.EQK_LON = :EQK_LON,
                        T.EQK_LOC = :EQK_LOC,
                        T.EQK_INTENSITY = :EQK_INTENSITY,
                        T.EQK_COMMENTS = :EQK_COMMENTS,
                        T.EQK_UPDATE = :EQK_UPDATE,
                        T.EQK_ORIGIN_MSC = :EQK_ORIGIN_MSC
                WHEN NOT MATCHED THEN
                    INSERT (
                        EQK_NUM, EQK_AREA__REGION, EQK_REPORT_TIME, EQK_ORIGIN_TIME, EQK_MT, 
                        EQK_LAT, EQK_LON, EQK_LOC, EQK_INTENSITY, EQK_COMMENTS, EQK_UPDATE, EQK_ORIGIN_MSC
                    ) VALUES (
                        :EQK_NUM, :EQK_AREA__REGION, :EQK_REPORT_TIME, :EQK_ORIGIN_TIME, :EQK_MT, 
                        :EQK_LAT, :EQK_LON, :EQK_LOC, :EQK_INTENSITY, :EQK_COMMENTS, :EQK_UPDATE, :EQK_ORIGIN_MSC
                    )
                """

                # 데이터 삽입 실행
                cursor.execute(insert_query, {
                    'EQK_NUM': EQK_NUM,
                    'EQK_AREA__REGION': EQK_AREA__REGION,
                    'EQK_REPORT_TIME': EQK_REPORT_TIME,
                    'EQK_ORIGIN_TIME': EQK_ORIGIN_TIME,
                    'EQK_MT': EQK_MT,
                    'EQK_LAT': EQK_LAT,
                    'EQK_LON': EQK_LON,
                    'EQK_LOC': EQK_LOC,
                    'EQK_INTENSITY': EQK_INTENSITY,
                    'EQK_COMMENTS': EQK_COMMENTS,
                    'EQK_UPDATE': EQK_UPDATE,
                    'EQK_ORIGIN_MSC': EQK_ORIGIN_MSC
                })

            # 커밋하여 변경사항 저장
            conn.commit()

            # 연결 종료
            cursor.close()
            conn.close()

            print("데이터가 성공적으로 삽입되었습니다.")

        except Exception as e:
            print("예외 발생:", e)

    else:
        print(f"응답 실패! 상태 코드: {response.status_code}")

    print("✅ 배치 작업 완료!\n")

# 매시간 0분(정각)에 실행
schedule.every().hour.at(":15").do(batch_task)

while True:
    schedule.run_pending()
    time.sleep(1)  # CPU 과부하 방지를 위해 1초 대기



