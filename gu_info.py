import requests
import csv

def gu_cd_from_gu_nm(gu_nm):

    gu_cd = { "종로구": "111123"
            , "중구": "111121"
            , "용산구": "111131"
            , "은평구": "111181"
            , "서대문구": "111191"
            , "마포구": "111201"
            , "성동구": "111142"
            , "광진구": "111141"
            , "동대문구": "111152"
            , "중랑구": "111151"
            , "성북구": "111161"
            , "강북구": "111291"
            , "도봉구": "111171"
            , "노원구": "111311"
            , "양천구": "111301"
            , "강서구": "111212"
            , "구로구": "111221"
            , "금천구": "111281"
            , "영등포구": "111231"
            , "동작구": "111241"
            , "관악구": "111251"
            , "서초구": "111262"
            , "강남구": "111261"
            , "송파구": "111273"
            , "강동구": "111274"
            }
    return gu_cd[gu_nm]

def to_address(lat, lon, appkey):
    """
    위도, 경도 -> 주소 변환 메서드
    :param lat: 위도
    :param lon: 경도
    :param appkey: 카카오 REST API 앱키
    :return: addr: (주소)
    """

    # 카카오 REST API
    url = f"https://dapi.kakao.com/v2/local/geo/coord2regioncode?y={lat}&x={lon}"
    headers = {"Authorization": f"KakaoAK {appkey}"}

    # JSON 형식의 응답 data
    data = requests.get(url, headers=headers).json()

    addr = data["documents"][0]["address_name"]

    # 주소 반환
    return addr



def to_lat_lon(address, appkey):
    """
    주소 -> 위도, 경도 변환 메서드
    :param address: 주소
    :param appkey: 카카오 REST API 앱키
    :return: lat, lon (위도, 경도)
    """

    # 카카오 REST API
    url = f"https://dapi.kakao.com/v2/local/search/address?query={address}"
    headers = {"Authorization": f"KakaoAK {appkey}"}

    # JSON 형식의 응답 data
    data = requests.get(url, headers=headers).json()

    lat = data["documents"][0]["y"]
    lon = data["documents"][0]["x"]

    # 위도, 경도 반환
    return lat, lon


def main():

    # 카카오 앱키(하드 코딩으로 인해 잠재적 보안 이슈)
    appkey = "996cb75dc093f50fa2cf066a3ccb7b2a"

    # 서울시 대기오염 측정소 정보.csv 파일 읽은 후 INSERT 문 생성
    with open('서울시 대기오염 측정소 정보.csv', 'r', encoding='CP949') as f:

        reader = csv.reader(f)

        # 첫째 줄(헤더) 제외
        header = next(reader)

        # 행 단위로 읽으면서 측정소 주소 -> 위도, 경도 반환 후 INSERT 문 생성
        for row in reader :

            lat, lon = to_lat_lon(row[2], appkey)

            print(f"INSERT INTO GU_INFO VALUES ('{row[4]}', '{row[1]}', '{row[2]}', {lat}, {lon}, {row[3]});")



if __name__ == '__main__':
    main()
