import schedule
import time
import datetime
import cx_Oracle
from p13Oracle.PlayerDAO import PlayerDAO

def batch_task01():
    now=datetime.datetime.now()
    print(f'배치실행: {now.strftime('%Y-%m-%d %H:%M:%S')}')
    #배치 작업 코드
    dsn = cx_Oracle.makedsn('192.168.100.30','1522',service_name='XE') #DB연결 정보
    user = 'scott'      #사용자 계정
    password = 'pcwk'   #비밀번호

    #DAO객체 생성
    dao=PlayerDAO(dsn,user,password)

    rows = dao.doRetrieve()
    for row in rows:
        print(row)


    print(f'배치실행 종료: {now.strftime('%Y-%m-%d %H:%M:%S')}')


def batch_task02():
    now=datetime.datetime.now()
    print(f'배치실행: {now.strftime('%Y-%m-%d %H:%M:%S')}')
    #배치 작업 코드

    print(f'배치실행 종료: {now.strftime('%Y-%m-%d %H:%M:%S')}')

#매시간:17분에 실행
schedule.every().hour.at(":17").do(batch_task01)

#매10초
schedule.every(10).seconds.do(batch_task02)

while True:
    schedule.run_pending()
    time.sleep(1) #CPU과부하 방지
