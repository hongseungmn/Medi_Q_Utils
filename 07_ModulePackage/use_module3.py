#use_module3.py : 패키지 mathematics를 import해서 사용하기

#1. import 패키지명.모듈명 : 이때는 패키지 초기화 파일 설정 불필요
#import mathematics.module3
#print(dir()) # 'mathematics'만 보임 module3는 없음. 즉 패키지명.모듈명으로 이동
#print(mathematics.module3.add(10,5))
#print(mathematics.module3.minus(10,5))

#2. import 패키지명
#패키지 초기화 파일 (__init__.py) 설정 전에는 mathematics를 모듈로 인식한다
#즉 07_modulepackage패키지 안에서 mathematics.py를 찾게 된다
import mathematics
print(dir())
#print(mathematics.module3.add(10,5))
#※ import '패키지명' 을 사용하려면 패키지 초기화 파일에 설정을 해야한다
# 즉 패키지명을 패키지로 인식하도록
print(mathematics.module3.add(10,5))
print(mathematics.module3.minus(10,5))
