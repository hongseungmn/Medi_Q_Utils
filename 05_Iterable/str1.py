'''
순서가 있는 자료형(시퀀스 객체):str,list,tuple,range
공통 기능
1. (not) in 연산자로 요소(객체) 존재 파악
2. 인덱싱([인덱스]) 및 슬라이싱([시작인덱스 : 끝인덱스])
3. + 나 * 연산자로 시퀀스객체를 연결(+)하거나 같은 시퀀스객체를 배수(*)로 늘릴 수 있다
   단,range객체는 list로 변환후 +,*를 적용하자
   그리고 *연산자 사용시 0이나 음수를 곱하면 빈 객체가 된다
4. len(시퀀스객체)함수는 저장된 요소의 갯수 반환
'''
print('[빈 문자열 만들기]')
a=''#"",'''''',""""""
#len(반복가능한 객체)는 모든 반복 가능한 객체의 요소 수를 반환
print(f'value:{a},len:{len(a)},type:{type(a)}')
print('[NOT 빈 문자열 만들기]')
a='PYTHON'
print(f'value:{a},len:{len(a)},type:{type(a)}')
#순서가 있는 자료형(str,list,tuple,range)들은 각 요소에 인덱스로 접근 가능
#시퀀스객체[인덱스]
#인덱스는 양수(인덱스는 0부터 시작하고 왼쪽기준) 혹은 음수(인덱스는 -1부터시작하고 오른쪽 기준)
print('[인덱싱:인덱스로 요소에 접근]')
#index = int(input(f'추출할 문자의 인덱스를 입력(단,최대값은 {len(a)-1})?'))
#print(a[index])
#인덱스 범위를 벗어난 경우 - IndexError: string index out of range
print('[문자열에 for문 적용하기]')
for index in range(len(a)):
    print(f'인덱스:{index},요소:{a[index]}')

#enumerate(순서가 있는 자료형 즉 시퀀스객체): 리스트, 튜플, 문자열객체,range객체의 요소의 순서(인덱스)와 요소를
#튜플로 묶어서 enumerate 객체(반복가능한 객체)로 반환
#※ 보통 enumerate 함수는 for문과 함께 자주 사용된다
print('-' * 30)
for element in enumerate(a):
    print(element)
print('-' * 30)
for index,element in enumerate(a):#튜플을 구조분해(언패킹)해서 각각의 변수에 저장
    print(f'인덱스:{index},요소:{element}')

#시퀀스객체[인덱스]=새로운 요소로 변경하기
#a[0]='B'#TypeError: 'str' object does not support item assignment
#※문자열(불변-IMMUTABLE객체)의 값을 변경하려면 리스트로 변환후 변경해야 한다
#1.먼저 문자열을 리스트로 변환한다
b=list(a)
print(f'value:{b},len:{len(b)},type:{type(b)}')
#2.특정 인덱스의 문자열을 변경한다
b[0]='B'
print(f'value:{b},len:{len(b)},type:{type(b)}')
c=str(b)
print(f'value:{c},len:{len(c)},type:{type(c)}')
#방법1]join()함수 사용
c=''.join(b)
print(f'value:{c},len:{len(c)},type:{type(c)}')
#방법2]리스트의 각 요소를 문자열에 누적
c=''
for e in b:
    c+=e
print(f'value:{c},len:{len(c)},type:{type(c)}')
print('[슬라이싱:인덱스를 사용해서 특정 범위의 요소들 추출]')
#슬라이싱은 시퀀스 객체에만 적용됨
#※슬라이싱은 항상 오른쪽 방향으로 슬라이싱이 되야 한다
d='ABCDEFG'
#[시작인덱스:끝인덱스] - 시작인덱스부터  끝인덱스-1까지
print(d[1:1])#빈 문자열.슬라이싱 방향이 왼쪽임으로(1부터 0으로)
print(d[1:3])
print(d[1:-3])#1부터 -4(-3-1)까지
print(d[-1:-3])#빈 문자열.슬라이싱 방향이 왼쪽
#[:끝인덱스] -  처음부터 끝인덱스-1까지
print(d[:0])#빈 문자열.슬라이싱 방향이 왼쪽
print(d[:-1])
#[시작인덱스:] -  시작인덱스부터 끝까지
print(d[0:])
print(d[-len(d):])
#[:] -  모든 요소 슬라이싱
print(d[:])

#in (not in)  연산자 : 모든 시퀀스 객체에 공통으로 적용될수 있는 연산자
#                     객체안의 특정 요소의 존재여부를 파악할 수 있는 연산자
#찾을객체 in 반복가능한 시퀀스객체
e='JAVA'
print('A' in e)
print('A' not in e)
print('a' in e)
print('AVA' in e)

while True:
    email = input('이메일 주소를 입력하세요?')
    if '@' not in email:
        print('이메일 형식이 아닙니다')
    else:
        break
# * 및 +(문자열 연결)
print('HELLO '+'WORLD')
print('HELLO ' * 10)









