import requests
import json

# 모든 대피소 데이터를 저장할 리스트 초기화
url = "https://www.safetydata.go.kr"
dataName = "/V2/api/DSSP-IF-10943" # 민방위 대피소 데이터 url 입력
shelters = []
pageNo = 1
numOfRows = 1000  # 한 페이지당 최대 행 수
while True:
    # API 요청에 필요한 파라미터 설정
    payloads = {
        "serviceKey": "7TML53MMO8B79RL6",
        "returnType": "json",
        "pageNo": pageNo,
        "numOfRows": numOfRows,
    }

    # API 요청 보내기
    response = requests.get(url + dataName, params=payloads)
    if response.status_code == 200:
        data = response.json()
        # 최종 요청 URL 출력 (디버깅용)
        print(f"최종 요청 URL: {response.url}")

        # 'body' 부분에서 대피소 데이터 가져오기
        page_shelters = data.get("body", [])
        if not page_shelters:
            # 더 이상 가져올 데이터가 없으면 루프 종료
            break

            # '서울특별시' 대피소 필터링
            filtered_shelters = [s for s in page_shelters if "서울특별시" in (s.get("EQK_ACMDFCLTY_ADRES") or "")]


        shelters.extend(page_shelters)
        pageNo += 1  # 다음 페이지로 이동
    else:
        print("데이터 가져오기 오류:", response.status_code)
        break

# 가져온 대피소 데이터의 개수 출력
print(f"총 {len(shelters)}개의 대피소 데이터를 가져왔습니다.")


print(shelters[0])
print(shelters[22823])

# 파일로 저장
with open("shelters.json", "w", encoding="utf-8") as f:
    json.dump(shelters, f, ensure_ascii=False, indent=4)  # ensure_ascii=False: 한글 깨짐 방지