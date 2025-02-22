import requests
import cx_Oracle

# URL 문자열
url = 'https://apihub.kma.go.kr/api/typ01/url/eqk_list.php?tm1=201511231215&tm2=202502211215&disp=1&help=1&authKey={API_KEY}'

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

        # 데이터를 EARTHQUAKE 테이블에 삽입
        cursor = conn.cursor()

        for line in lines:
            # 각 줄을 ',' 기준으로 나누어 데이터 추출
            data = line.split(',')
            if len(data) < 12:
                continue  # 데이터가 부족한 줄은 건너뛰기

            # ','로 데이터를 나누기 전에 필요한 값을 추출하여 변수에 저장
            EQK_AREA__REGION = int(data[0])   EQK_AREA__REGION
            EQK_REPORT_TIME = data[1]   EQK_REPORT_TIME
            EQK_ORIGIN_TIME = data[3]   EQK_ORIGIN_TIME
            EQK_MT = float(data[4])   EQK_MT
            EQK_LAT = float(data[5])   EQK_LAT
            EQK_LON = float(data[6])   EQK_LON
            EQK_LOC = data[7]   EQK_LOC
            EQK_INTENSITY = None   EQK_INTENSITY는 null로 설정
            EQK_COMMENTS = data[9]  EQK_COMMENTS
            EQK_UPDATE = None  EQK_UPDATE는 빈 값으로 설정
            EQK_ORIGIN_MSC = data[10]  # EQK_ORIGIN_MSC (API에서 데이터의 끝이라 가정)

            # 시퀀스를 사용하여 EQK_NUM 자동 생성
            cursor.execute("SELECT EQK_NUM_SEQ.NEXTVAL FROM DUAL")
            EQK_NUM = cursor.fetchone()[0]  # 시퀀스에서 다음 값을 가져옴

            # 삽입 쿼리 작성
            insert_query = """
            INSERT INTO EARTHQUAKE (
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
