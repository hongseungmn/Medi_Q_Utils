print('[빈 문자열 만들기]')
a = '' # "" , '''''' , """"""
#len(반복하능한 객체)는 모든 반복가능한 객체의 요소 개수를 반환
print(f'value : {a}, len : {len(a)}, type : {type(a)}')
print("[Not 빈 문자열 만들기]")
a = 'PYTHON'
print(f'value : {a}, len : {len(a)}, type : {type(a)}')


#enumerate(순서가 있는 자료형 즉 시퀀스 객체) : 리스트, 튜플, 문자열객체, range객체의 요소의 순서(인덱스)와 요소를
# 튜플로 묶어서 enumerate 객체(반복가능한 객체)로 반환
#※ 보통 enumerate 함수는 for문과 함께 자주 사용된다
for element in enumerate(a):
    print(element)

for index, element in enumerate(a): # 튜플을 구조분해(언패킹)해서 각각의 변수에 저장
    print(f'인덱스 :{index},  요소 :{element}')

#시퀀스 객체[인덱스] = 새로운 요소로 변경하기
#a[0] = 'B'
#print(a)
#※문자열(불변-IMMUTABLE 객체)의 값을 변경하려면 리스트로 변환 후 변경해야 한다
b = list(a)
b[0] = 'B'
print(b)

c = ''.join(b)
print(c)

d = 'ABCDEFG'
#[시작인덱스 : 끝인덱스] - 시작인덱스부터 끝인덱스-1까지
print(d[1:1])# 빈 문자열.-> 슬라이싱 방향이 왼쪽이므로(1부터 0으로)

print(d[1:-3]) # 1부터 -4까지
print(d[1:-2])
print(d[1:-1])


