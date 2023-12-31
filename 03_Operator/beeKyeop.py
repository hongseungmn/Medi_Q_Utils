'''
-비교연산자(이항연산자)의 결과는
True아니면 False(bool값)
> : ~보다 크다
>=: ~보다 크거나 같다
< : ~보다 작다
<=: ~보다 작거나 같다
!=: 같지 않다
==: 같다
-비교 연산자는 모두 우선순위가 같다
-산술연산자가 비교 연산자보다 우선 순위가 높다
-비교 연산자를 사용한 식은 비교식
'''
from locale import format

print('[숫자 비교]')
num1 = num2 =10
print(num1 >=num2)
b= num1 <= num2
print('%d <= %d의 결과:%s' % (num1,num2,b))
b= num1 != num2
print('%d != %d의 결과:%s' % (num1,num2,b))
#숫자뿐만 아니라 문자열도 ==와 != 연산자로 비교할 수 있다
#물론 대소도 비교 가능.이때는 아스키 코드혹은 유니코드값으로 비교한다
'''    
아스키 코드:1byte로 표현할 수 있는 문자
(영문자 와 숫자)
십진수로 정의한 값을 아스키 코드라 함.
예]A의 아스키 코드값:65(이진수:1000001)
키보드에서 A라고 치면 컴퓨터 메모리에 
1000001로 저장됨.
소문자 a는 아스키 코드값이 97

유니코드:1BYTE로 표현이 안되는 문자
(한글이나 한자등)
은 3BYTE가 필요하다.\\x16진수로 정의한 값을
유니코드라 한다.
'''
print('[문자열 비교]')
print('HELLO' == 'hello')
print('ABC' >= 'ABc')
b = 15 % 3 * 2 + 4 > (10-2) *4 != True
#1](10-2) : 8
#2]15 % 3 : 0
#3] 2]의결과 * 2 : 0
#4] 1]의 결과 * 4 : 32
#중간정리: 0 + 4 > 32 != True
#5]0+ 4 : 4
#  4 > 32 != True
#6] 4 > 32 : False
#  False != True : True

print('15 %% 3 * 2 + 4 > (10-2) *4 != True의 결과:%s' % b)
#  ==, !=는 값 자체를 비교하고, is, is not은 객체(object)를 비교
# id()함수:객체의 주소값 반환하는 함수
print('[==와 is 연산자]')
a=1
b=1.0
print(a==b)
print(a is b)
print('a의 주소:{},b의 주소:{}'.format(id(a),id(b)))
#bool()함수: 정수, 실수 혹은  문자열,객체등을 bool로 만들 때는  사용
#0혹은 0.0이  그리고 ''(빈문자열) 혹은 빈 객체를 제외한  모든 정수,실수, 문자열,객체등은 True이다
#빈 리스트[]를 bool로 변환시 False로 변환됨
a=0.0
b=False
print('value:{},type:{}'.format(a,type(a)))
print('value:{},type:{}'.format(b,type(b)))
print(a==b)#0.0==0
print(a is b)
print(bool(a))
print(bool(a) is b)

print('0:{},0.0:{},빈 문자열:{},빈 객체:{}'.format(bool(0),bool(0.0),bool(''),bool([])))
print('-1:{},3.0:{},\'HELLO\':{},[1,2]:{}'.format(bool(-1),bool(3.0),bool('HELLO'),bool([1,2])))

#※빈 리스트를 bool값과 비교시에는 bool()함수로 변환후 비교
#단,빈 리스트를 not함께 쓸때는 bool()변환 불필요
a=[]
print(a==b)#[]는 0으로 처리 불가([]==False)
print(bool(a)==b)#False == False
print((not a)!=b)#True != False


