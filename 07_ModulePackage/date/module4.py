import time
#time() : 1970 1.1 0:0:0부터 현재까지 지난 시간을 초단위로 반환
#localtime([초]) : 지역(한국)에 맞는 시간으로 변경하는 함수.struct_time객체 반환
#strftime('날짜 형식의 포맷 문자열', 시간)

def year():
  return time.strftime('%Y')
month = lambda : time.strftime('%m')
day = lambda : time.strftime('%d')