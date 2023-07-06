#use_module1.py : 모듈 module1.py를 import해서 사용하기
#모듈 불러오기 : import 모듈명(.py를 제외한 파일명)
import module1
print('-' * 30)
import module1 # 최초 import한 것만 유효하다. 즉 한번만 import 하면 된다
print(dir(module1))# module1이라는 모듈명으로 접근할 수 있는 이름(변수, 함수, 클래스 등) 출력
#print(PI) #NameError : name 'PI' is Not 