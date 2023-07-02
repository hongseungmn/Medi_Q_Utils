def pprint(obj):
    # bool타입은 int 타입으로도 체크 가능
    end = '\n' if isinstance(obj, int) or isinstance(obj, float) else ''
    print(f'객체 :{obj}, 타입 :{type(obj)}', end=end)
    if not isinstance(obj, int) and not isinstance(obj,float):
        print(f',요소 갯수 :{len(obj)}')

print('[리스트 생성 첫번째 : 빈 리스트]')

print('[리스트 생성 두번째 : 같은 타입의 객체(요소) 저장')
b = [1,2,3,4,5] # 변수 하나에 여러개 데이터 설정 : 패킹
pprint(b)

print('[리스트 생성 세번째 : 다른 타입의 객체(요소) 저장')
c = ['가길동',20,3.14,False]
pprint(c)

print('[리스트 언 패킹(구조분해)')
#리스트의 각 요소를 여러 변수에 나눠 담는 것 : 언패킹(구조 분해)
#단, 변수의 개수가 요소의 개수와 정확히 일치해야 한다
c1, c2, c3, c4 = c
pprint(c1)
pprint(c2)
pprint(c3)
pprint(c4)

print('[리스트 생성 네번쨰 : list(str)')
list_ = list('PYTHON')
pprint(list_)

print('[리스트 생성 다섯번째 : list(range객체)]')
list_ = list(range(5))
pprint(list_)

print('[요소 추가하기 : append()')

print('[슬라이싱 : ')