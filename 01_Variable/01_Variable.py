#변수 선언 방법1]변수명 = 데이터
a=10
print(a)
print(type(a))#type(변수 혹은 값):자료형 반환 <class 'int'>
print(a,type(a),sep=',')#값과 타입을 한줄로 출력
#변수 선언 방법2]변수명1, 변수명2, 변수명3,.. = 반복가능한 객체(이터레이터)
#이터레이터의 요소를 여러 변수에 나눠 담는 것을 언패킹(unpacking) 또는 구조분해(destructuring)라고 한다.
#변수명1, 변수명2, 변수명3 = 데이타1, 데이타2, 데이타3 혹은 (데이타1, 데이타2, 데이타3)
a,b,c ="파이썬",'10',20#("파이썬",'10',20)
print('a의 값:%s,a의 자료형:%s' % (a,type(a)))
print('b의 값:%s,b의 자료형:%s' % (b,type(b)))
print('c의 값:%s,c의 자료형:%s' % (c,type(c)))
#변수 선언 방법3]변수명 = 반복가능한 객체(이터레이터)
#여러 개의 데이터를 이터레이터를 이용해 하나의 변수에 묶어 담는 것을 패킹(packing)
#변수명 = 데이타1, 데이타2, 데이타3 혹은 (데이타1, 데이타2, 데이타3)
d=10,'20','파이썬'#(10,'20','파이썬') 즉 int,str,str객체를 튜플로 묶어서(패킹) 변수 d에 저장
print('d의 값:%s,d의 자료형:%s' % (d,type(d)))
#변수 선언 방법4]변수명1 = None
#z#NameError: name 'z' is not defined
z=None
print('z의 값:%s,z의 자료형:%s' % (z,type(z)))

x,y=10,20
print('x=',x,',y=',y)
y,x=x,y
print('x=',x,',y=',y)
import keyword
print(keyword.kwlist)
#elif = 10#SyntaxError: invalid syntax 키워드를 변수로 사용할 수 없다
#변수 삭제
del x# 혹은 del(x)
#print(x)#NameError: name 'x' is not defined
