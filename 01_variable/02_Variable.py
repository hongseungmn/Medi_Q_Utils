import sys
print(sys.getrefcount(2023))
x=2023
print(sys.getrefcount(2023))
y=2023
print(sys.getrefcount(2023))
print(sys.getrefcount(1))
# is 연산자 : 객체가 같은 타입인지 확인하는 연산자
print(x is y)