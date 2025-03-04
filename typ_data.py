import requests
import cx_Oracle
import xml.etree.ElementTree as ET
import schedule
import time
import datetime

def batch_task():
    now = datetime.datetime.now()
    print(f"🔹 배치 작업 실행: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # Oracle DB 연결
    conn = cx_Oracle.connect(
        'SAMA',  # DB 사용자 이름
        'SAMA1234',  # DB 비밀번호
        '192.168.100.30:1522/XE'  # DB 호스트, 포트, SID
    )
    cursor = conn.cursor()

    # 숫자로 변환하는 함수 (문자열이나 null 값 처리)
    def to_numeric(value, default=0):
        try:
            # 숫자로 변환, 변환 실패 시 기본값(default) 반환
            return float(value) if value is not None and value != 'null' else default
        except ValueError:
            # 변환 실패 시 기본값(default) 반환
            return default

    # API에서 데이터 가져오기
    url = 'https://apihub.kma.go.kr/api/typ02/openApi/SfcYearlyInfoService/getTyphoonList?pageNo=1&numOfRows=100&dataType=XML&year=2024&authKey=X4kLr7YTTFWJC6-2E7xVYw'
    response = requests.get(url)

    # 상태 코드 확인
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    # XML 데이터를 처리할 수 있는 라이브러리 필요 (예: xml.etree.ElementTree)
    if response.status_code == 200:
        try:
            # XML 데이터 파싱
            root = ET.fromstring(response.text)

            # 각 태풍 정보 추출 (예시, XML 구조에 따라 변경될 수 있음)
            for item in root.findall('.//item'):  # XML의 각 항목을 찾기 위한 예시
                for info in item.findall('.//info'):  # 각 item 안의 여러 info 태그 처리
                    TYP_NAME = info.find('typ_en').text if info.find('typ_en') is not None else None
                    TYP_ST = info.find('tm_st').text if info.find('tm_st') is not None else None
                    TYP_ED = info.find('tm_ed').text if info.find('tm_ed') is not None else None

                    # '2024'을 TYP_ST와 TYP_ED에 추가
                    if TYP_ST:
                        TYP_ST = '2024' + TYP_ST  # 예: '2024-08-20'
                    if TYP_ED:
                        TYP_ED = '2024' + TYP_ED  # 예: '2024-08-22'

                    # typ_ps와 typ_ws가 null일 경우 기본값 0을 설정
                    TYP_MIN_PRESSURE = to_numeric(info.find('typ_ps').text if info.find('typ_ps') is not None else None,
                                                  default=0)
                    TYP_MAX_WIND = to_numeric(info.find('typ_ws').text if info.find('typ_ws') is not None else None,
                                              default=0)
                    TYP_KOR_NAME = info.find('typ_name').text if info.find('typ_name') is not None else None
                    TYP_EFF = info.find('eff').text if info.find('eff') is not None else None

                    # DB에 삽입
                    cursor.execute("""
                MERGE INTO TYP T
                USING (SELECT 
                            :TYP_NAME AS TYP_NAME, 
                            :TYP_ST AS TYP_ST, 
                            :TYP_ED AS TYP_ED, 
                            :TYP_MIN_PRESSURE AS TYP_MIN_PRESSURE, 
                            :TYP_MAX_WIND AS TYP_MAX_WIND, 
                            :TYP_KOR_NAME AS TYP_KOR_NAME, 
                            :TYP_EFF AS TYP_EFF
                       FROM DUAL) S
                ON (T.TYP_NAME = S.TYP_NAME AND T.TYP_ST = S.TYP_ST)
                WHEN MATCHED THEN
                    UPDATE SET 
                        T.TYP_ED = S.TYP_ED,
                        T.TYP_MIN_PRESSURE = S.TYP_MIN_PRESSURE,
                        T.TYP_MAX_WIND = S.TYP_MAX_WIND,
                        T.TYP_KOR_NAME = S.TYP_KOR_NAME,
                        T.TYP_EFF = S.TYP_EFF
                WHEN NOT MATCHED THEN
                    INSERT (TYP_NUM, TYP_NAME, TYP_ST, TYP_ED, TYP_MIN_PRESSURE, 
                            TYP_MAX_WIND, TYP_KOR_NAME, TYP_EFF)
                    VALUES (TYP_SEQ.NEXTVAL, S.TYP_NAME, S.TYP_ST, S.TYP_ED, S.TYP_MIN_PRESSURE, 
                            S.TYP_MAX_WIND, S.TYP_KOR_NAME, S.TYP_EFF)
                """, {
                        'TYP_NAME': TYP_NAME,
                        'TYP_ST': TYP_ST,
                        'TYP_ED': TYP_ED,
                        'TYP_MIN_PRESSURE': TYP_MIN_PRESSURE,
                        'TYP_MAX_WIND': TYP_MAX_WIND,
                        'TYP_KOR_NAME': TYP_KOR_NAME,
                        'TYP_EFF': TYP_EFF
                    })

            # 커밋
            conn.commit()

        except Exception as e:
            print(f"Error parsing or inserting data: {e}")
    else:
        print("Error: Failed to retrieve data")

    # 연결 종료
    cursor.close()
    conn.close()

    print("✅ 배치 작업 완료!\n")

# 매시간 0분(정각)에 실행
schedule.every().hour.at(":50").do(batch_task)

while True:
    schedule.run_pending()
    time.sleep(1)  # CPU 과부하 방지를 위해 1초 대기
