#정수형(int)는 소수점이 없는 숫자를 의미
#100,-100 등
def pprint(value):
    print('value : ',value,sep='',end=',')
    print('type : ',type(value),sep='')


a = 100
pprint(a)

b = 10 / 5
pprint(b)
# int()함수 : 정수로 변환하는 함수 - 소수점 이하를 버린다
c = int(b)
pprint(c)

print('[각 진수로 숫자 표현하기]')
print('2진수 : ',0b10)