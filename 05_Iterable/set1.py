#※set는 중복을 허용하지 않는다
#순서가 없기때문에 출력시 순서없이 출력된다.

print('[집합 생성 첫번째:빈 집합]')
#a={}#딕셔너리다
a=set()#생성자 함수로만 만들 수 있다
print('value:{},type:{}'.format(a,type(a)))
print('[집합 생성 두번째:{요소1,요소2,....}]')
a={4,10,282,3.14,5,20}
print(a)
print('[집합 생성 세번째:set() - 리스트나 튜플을 집합으로 변환(중복 요소 제거됨)]')
#a=set(1,2,3,4,5)#TypeError: set expected at most 1 argument, got 5
#a=set(1)#TypeError: 'int' object is not iterable
a=set((1,2,3,4,5,4,3,3,5,1))#set([1,2,3,4,5,4,3,3,5,1])
print(a)
print(set(list(range(1,6))))
print('[집합 생성 네번째:{문자열} 혹은 set(문자열:중복문자는 제거됨)]')
a={'HELLO'}#문자열이 하나의 요소가 된다
print(f'value:{a},type:{type(a)}')
a=set('HELLO')#문자 하나 하나가 요소가 된다(중복 문자는 제게됨)
print(f'value:{a},type:{type(a)}')
print('[집합 생성 다섯번째:set(((),(),....))]')
a=set([(1,2),(3,4),(4,5,6)])#튜플 혹은 리스트의 각 요소가 집합의 각 요소가 된다
print(a)
#집합의 요소로 수정이 가능한 리스트나 딕셔너리는 집합의 요소가 될수 없다
#a=set([(1,2),[3,4],(4,5,6)])#TypeError: unhashable type: 'list'
a={(1,2),(3,4),(4,5,6)}
print(a)
a={True,100,3.14,-1}
print(a)
