'''
for 변수  in 반복가능한 객체:

반복가능한 객체(Iteratable):요소가 여러개 있다. 하나씩 꺼내올 수 있다
반복가능한 객체 인지는 dir(객체)를 통해서 알 수 있다
__iter__라는 함수가 있다며 그것은 반복 가능한 객체다

반복기(Iterator): 반복가능한 객체의 __iter__()함수 호출시 반환된 객체.
                              반복기의 __next__()함수를 통해 요소를 하나씩 꺼내온다

                Iterator를 만드는 방법 두가지
                1.class로 만든다(__iter__(self),__next__(self)함수 오버라이딩)
                2.함수로 만들거나(yield키워드로 요소를 반환하는 함수)

[for문 작동방식]
for 변수 in 반복가능한객체:
    pass
1. 반복가능한객체의 __iter__()함수가 실행되어 iterator객체 생성
2. 반복때마다 iterator객체.__next__()함수가 호출되어  요소를 하나씩 꺼내와서 변수에 저장
3. 모든 요소를 다 꺼내오면 Stopiteration발생하여 for문 중지
'''
print('[문자열에서 한 문자씩 꺼내오기]')
for element in 'PYTHON':
    print(element)
print('[문자열 길이 만큼 반복은 하고 꺼내온 값을 사용하지 않을때]')
#문자열 길이 만큼 HELLO출력 6번 출력
#아래 _(UNDER BAR)는 스트링 객체에서 꺼내온 값을 무시하고자 할때
for _ in 'PYTHON':
    print('HELLO')

print(_)
#range()함수(생성자)는 Iterable객체를 반환한다(range타입)
a=range(5)
print(dir(a))
print('value:{},type:{}'.format(a,type(a)))
it=a.__iter__()
print(it.__next__())
print(it.__next__())
for i in a:
    print(i)
print('[문자열 길이만큼 반복하기-len()함수 사용]')
for i in range(len('PYTHON')):
    print('i가 %d일때 : %s' % (i,'HELLO'))
#range()함수
print('[range(숫자)]')
for index in range(5):#끝숫자-1
    print('HELLO',index)

print('[range(시작숫자,끝숫자)]')
for index in range(5,10):#끝숫자-1
    print('HELLO',index)

print('[range(시작숫자,끝숫자,증감폭(양수))]')
for index in range(5,10,2):#끝숫자-1
    print('HELLO',index)
print('[range(시작숫자,끝숫자,증감폭(음수))]')
for index in range(10,5,-2):#끝숫자+1
    print('HELLO',index)
#반복문을 이용해서 1부터 10까지 누적합:1+2+3+4+5+6+7+8+9+10
sum =0
for i in range(1,11):
    sum+=i
print('{}부터 {}까지 누적합:{}'.format(1,10,sum))
#1부터 10까지 숫자중 2의 배수의 합:2+4+6+8+10
#방법1]2씩 증가하도록 증감식 작성
sum=0
for i in range(0,11,2):
    sum += i
print('{}부터 {}까지 2의배수의 누적합:{}'.format(1, 10, sum))
#방법2]1부터 1씩증가하면서  10까지 반복하면서
#      i의 값이 2의 배수인 경우에만 누적
sum=0
for i in range(1,11):
    if i % 2 ==0:
        sum+=i
print('{}부터 {}까지 2의배수의 누적합:{}'.format(1,10,sum))
print('for문이 끝난 후 i의 값:',i)
'''
문]1부터 100까지 숫자중 3의 배수 이거나 5의 배수인
숫자의 합을 구해라
단, 3과5의 공배수인 경우 ,누적합에 단 한번만
포함시켜라.
3+5+6+9+10+12+15+18+20+21+24+25+27+30......
'''
sum=0
for i in range(1,101):
    if i % 3==0 or i % 5==0:
        sum+=i
print('{}부터 {}까지 3 및 5의 배수의 누적합:{}'.format(1,100,sum))
'''
문]1부터 100까지 숫자중 3의 배수 이거나 5의 배수인
숫자의 합을 구해라
단, 3과5의 공배수는 제외시켜라
즉 15,30,45,60..은 제외

3+5+6+9+10+12+18+20+....
'''
#방법1] or 하고 and연산 사용
sum=0
for i in range(1,101):
    if (i % 3==0 or i % 5==0) and i % 15 !=0:
        sum+=i
print('{}부터 {}까지 3 및 5의 배수의 누적합(공배수 제외):{}'.format(1,100,sum))
#방법2]^(XOR)연산 사용
sum=0
for i in range(1,101):
    if (i % 3==0) ^ (i%5==0):
        sum += i
print('{}부터 {}까지 3 및 5의 배수의 누적합(공배수 제외):{}'.format(1,100,sum))

'''
이중 for문 :for문 안의 for문
이중 for문에서 바깥 for문은 행(row)를 의미
안쪽 for문은 열(column)을 나타낸다
'''
repeat=0
for i in range(3):
    for k in range(3):
        repeat+=1
        print('HELLO',repeat)


print('-' * 50)
for i in range(5):
    for k in range(5):
        if i >= k :
            print('%-2c' % '*', ' ', end='')
    print()


for i in range(1,10):
    for j in range(2,10):
        print('%d * %d = %-2d ' % (j,i,i*j), ' ', end='')
    print()


# 1부터 10까지 누적합 : whilte문 사용
sum = 0
i = 1# 쵝식
while i <= 10: #반복조건
    sum +=i # 실행문
    i +=1 # 증감식
print('1부터 10까지 누적합 : ',sum)


sum = 0
i = 1
while i<= 1000:
    if (i % 3 == 0) ^ (i % 5 == 0):
        sum += i
    i +=1

print('1부터 1000까지 3과 5의 배수의 누적합(공배수 제외) : ',sum,sep='')

#반복할 횟수가 정해지지 않은 경우 while문 사용
import random
i = 1
while i != 5:
    i = random.randint(1,10) # 1부터 10까지 난수 발생
    print('i는 ',i)

i=1#바깥 While의 초기식
k=1
while i < 5: #바깥 while문(행)
    while k < 5: #안쪽while의 초기식
        if i==k:
            print('%-2d' % 1, end='')
        else:
            print('%-2d' % 0 ,end='')
        k +=1#안쪽 while의 증가식
    i+=1#바깥 while의 증감식
    k=1

import re
print(re.__file__)
print('[1. 패턴 객체 사용 - 패턴객체.함수()') #패턴객체 재사용 가능
email = input('이메일을 입력하세요?')
#re.compile('정규표현식") 로 Pattern객체 생성
#re.compile('[a-zA-Z]+@\\w')


log="[17.07.11 23:29:11] [INFO ]  [eclipse.galileo-bean-thread-50618297 galileo.site.SiteBean:317 ] - ##galileo_bean end. MessageExchange_ID:id:localhost-15a6308ba1c-6:86071562";