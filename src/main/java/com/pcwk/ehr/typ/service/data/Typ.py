import requests
import json

# URL 문자열
url = 'https://apihub.kma.go.kr/api/json?authKey=X4kLr7YTTFWJC6-2E7xVYw'

# GET 요청
response = requests.get(url)

# 응답을 JSON 형태로 변환
json_response = response.json()

print(json_response)