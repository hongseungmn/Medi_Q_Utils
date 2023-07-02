#coding:utf-8 
print('Hello World')
print('안녕 파이썬')
#대소문자 엄격 구분
#자료형 선언이 없다
#a#NameError: name 'a' is not defined
a=None
a=10
print(a)
#한 라인에 여러개 명령어 작성시에는 마지막 명령을 제외한 명령어에는 ; 을 붙인다
b=20;c=a+b;print(c)
#result ='더하기 결과:'+c#TypeError: can only concatenate str (not "int") to str
result ='더하기 결과:'+str(c)
print(result)
#파이썬은 들여쓰기가 문법이다
    #주석은 상관없다
#    print(result)#IndentationError: unexpected indent
for i in range(5):
#print(i)#IndentationError: expected an indented block after 'for' statement on line 18
    print(i)
if b % 2 ==0:
    print(str(b)+'는 짝수')
else:
    print(str(b) + '는 홀수')