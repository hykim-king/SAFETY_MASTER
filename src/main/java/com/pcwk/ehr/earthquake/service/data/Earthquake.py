import requests

# URL 문자열
url = 'https://apihub.kma.go.kr/api/typ01/url/eqk_now.php?tm=202502191215&disp=0&help=1&authKey=X4kLr7YTTFWJC6-2E7xVYw'

# GET 요청
response = requests.get(url)

# 응답 상태 코드 확인
if response.status_code == 200:
    print("서버로부터 응답을 정상적으로 받았습니다.")
    # 응답 본문을 텍스트로 출력
    print(response.text)  # 응답 본문 출력
else:
    print(f"서버에서 응답을 받지 못했습니다. 상태 코드: {response.status_code}")
