import datetime
from datetime import timezone, timedelta

def kst_from_serial_kst(serial_kst):
    '''
    'YYYYMMDDHH24MI' 형식의 KST(UTC+9) 시간을 을 -> 'YYYY.MM.DD HH24:MI' 형식으로 변경 \n
    출력 format = YYYY.MM.DD HH24:MI
    :param serial_kst:
    :return: kst_str
    '''

    serial_kst_date = datetime.datetime.strptime(serial_kst, '%Y%m%d%H%M')

    kst_str = datetime.datetime.strftime(serial_kst_date, '%Y.%m.%d %H:%M')

    return kst_str

def kst_serial_from_unix(unix):
    """
    유닉스 형식의 시간 => KST(UTC+9) 형식으로 변환 \n
    출력 format = YYYYMMDDHH24MI
    :param unix:
    :return: kst_str
    """

    # timezone 설정 KST(UTC+9)
    KST = timezone(timedelta(hours=9))

    kst_str = datetime.datetime.fromtimestamp(unix, KST).strftime("%Y%m%d%H%M")

    return kst_str

def kst_from_unix(unix):
    """
    유닉스 형식의 시간 => KST(UTC+9) 형식으로 변환 \n
    출력 format = YYYY.MM.DD HH24:MI
    :param unix:
    :return: kst_str
    """

    # timezone 설정 KST(UTC+9)
    KST = timezone(timedelta(hours=9))

    kst_str = datetime.datetime.fromtimestamp(unix, KST).strftime("%Y.%m.%d %H:%M")

    return kst_str

def cur_time_kst():
    """
    KST(UTC+9) 형식의 현재 시간 반환
    출력 format = YYYY.MM.DD HH24:MI
    :return: cur_time_kst_str
    """

    cur_time_kst_str = datetime.datetime.now().strftime("%Y.%m.%d %H:%M")

    return cur_time_kst_str



def main():
    unix = 1739935579
    serial_kst = '202502201600'

    print(kst_serial_from_unix(unix))
    print(kst_from_unix(unix))
    print(cur_time_kst())
    print(kst_from_serial_kst(serial_kst))






if __name__ == '__main__':
    main()
