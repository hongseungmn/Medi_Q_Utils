#use_module4.py : import가 아닌 from절을 사용해서 module4 사용하기


#from date.module4 import *
print(dir())
print(year(), month(), day(), sep='-')

#from 패키지 import * 혹은 변수, 함수, 클래스
from date import *
print(year(), month(), day(), sep='-')
print(dir()) # 이름공간에 아무것도 없다. 즉 패키지 초기화 파일 설정 필요
