import requests

API_URL = "https://www.safetydata.go.kr/V2/api/DSSP-IF-10943"
API_KEY = "7TML53MMO8B79RL6"

payloads = {
    "serviceKey": API_KEY,
    "returnType": "json",
    "pageNo": 1,
    "numOfRows": 5,  # 테스트를 위해 5개만 가져옴
}

response = requests.get(API_URL, params=payloads)

if response.status_code == 200:
    data = response.json()
    print("API 응답 데이터:", data)  # JSON 응답 데이터 출력
else:
    print("API 요청 실패:", response.status_code)
