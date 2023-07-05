def pprint(obj):
    #bool타입은 int타입으로도 체크 가능
    end = '\n' if isinstance(obj,int) or isinstance(obj,float) else ''
    print(f"값:{obj},타입:{type(obj)}",end=end)
    if not isinstance(obj,int) and not isinstance(obj,float):
        print(f',요소 수:{len(obj)}')

print('[리스트 생성 첫번째 : 빈 리스트]')#동적으로 요소 추가시 주로 사용
#방법1-[]
a=[]
pprint(a)
#방법2-list():list클래스의 생성자
a=list()
pprint(a)
print('[리스트 생성 두번째 : 같은 타입의 객체(요소) 저장]')
b=[1,2,3,4,5]#변수 하나에 여러개 데이타 설정:패킹
pprint(b)
print('[리스트 생성 세번째 : 다른 타입의 객체(요소) 저장]')
c=['가길동',20,3.14,True]
pprint(c)
print('[리스트 언 패킹(구조분해)]')
#리스트의 각 요소를 여러 변수에 나눠 담는 것:언패킹(구조분해)
#단, 변수의 개수가 요소의 개수와 정확히 일치해야 한다
c1,c2,c3,c4 = c
pprint(c1)
pprint(c2)
pprint(c3)
pprint(c4)#isinstance(a,int) int타입으로도 처리된다
print('[리스트 생성 네번째 : list(str객체)]')
list_=list('PYTHON')
pprint(list_)
print('[리스트 생성 다섯번째 : list(range객체)]')
list_ = list(range(5))
pprint(list_)
print('[요소 추가하기:append()]')
#※빈 리스트에 값(요소)을 할당할때는 [인덱스]=값 으로 할당하는게 아니라 append()함수를 이용해서 할당한다
#a[0]='가길동'#IndexError: list assignment index out of range
a.append('가길동')
a.append(20)
a.append('송파구')
pprint(a)
print('[요소 변경하기 : 리스트객체[인덱스]=새로운 요소]')
a[1]=40
a[2]='금천구'
pprint(a)
#a[3]='코스모'#IndexError: list assignment index out of range
a.append('코스모')
pprint(a)
print('[인덱싱:리스트객체[인덱스]]')
print(f'a[0]:{a[0]},a[1]:{a[1]},a[2]:{a[2]}')
print(f'요소 수 얻기:{len(a)}')
print('[슬라이싱:인덱스를 사용해서 특정 범위의 요소들 추출]')
#[시작인덱스:끝인덱스] - 시작인덱스부터  끝인덱스-1까지
print(a[1:1])#빈 리스트.슬라이싱 방향이 왼쪽임으로(1부터 0으로)
print(a[1:3])#[40,'금천구']
print(a[1:-3])#빈 리스트[]
print(a[-1:-3])#빈 리스트[]
#[:끝인덱스] -  처음부터 끝인덱스-1까지
print(a[:0])#빈 리스트[]
print(a[:-1])#['가길동', 40, '금천구']
#[시작인덱스:] -  시작인덱스부터 끝까지
print(a[0:])#['가길동', 40, '금천구', '코스모']
print(a[-len(a):])#['가길동', 40, '금천구', '코스모']
#[:] -  모든 요소 슬라이싱
print(a[:])#['가길동', 40, '금천구', '코스모']

f=['가','나','다','라']
for e in f:
    print(e)

for index in range(len(f)):
    print(f'인덱스:{index},요소:{f[index]}')
print('-'*30)
for index,ele in enumerate(f):
    print(f'인덱스:{index},요소:{ele}')

