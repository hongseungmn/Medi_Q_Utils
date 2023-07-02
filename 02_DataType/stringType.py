#파이썬에서 문자열을 만드는 방법은 총 4가지로
# ' , " ,''',"""로 감싸면 문자열이 된다.
print('Hello World')
print("Hello World")
print('''Hello World''')
#print('Hello
#      World')#SyntaxError: unterminated string literal (detected at line 6)
print('''Hello
         World''')
print("""
        Hello
        World
        !
        """)
# '''와 """안에는 ' 와 " 둘다 넣을 수 있다
print('''
올해 2023's의 목표
    1.건강
    2.취업
''')
print("""
올해 2023's의 목표
    1."건강"
    2."취업"
""")

s='HELLO'
print('value:',s,',type:',type(s))
#len()함수로 문자열 길이 구하기
print(len(s))
print(len('안녕'))
'''
※유니코드 문자열을 인코딩없이 그대로 파일에 쓰거나 다른 시스템으로 
  네트워크 전송을 할 수는 없다. 
  왜냐하면 유니코드 문자열은 단순히 문자셋의 규칙이기 때문이다.
  파일에 쓰거나 다른 시스템으로 유니코드 문자열을 전송하기 위해서는 
  바이트로 변환해야만 한다
'''
#encode('문자셋') : 유니코드 문자열을 바이트 문자열로 만드는 함수
#문자셋를 생략하면 디폴트 값인 utf-8로 동작.
print(s)#HELLO 문자열 :type이 str
print(s.encode(encoding='utf-8'),type(s.encode()))#b'HELLO' 바이트 문자열 :type이 bytes
print('안녕')#안녕
print('안녕'.encode())#b'\xec\x95\x88\xeb\x85\x95'
print(len(b'\xec\x95\x88\xeb\x85\x95'))#한글은 3바이트 차지
#decode():인코딩된 바이트 문자열을 (유니코드) 문자열로 변환하는 함수(bytes클래스의 메소드)

print(b'HELLO'.decode())#HELLO
print(b'\xec\x95\x88\xeb\x85\x95'.decode())#안녕

#문자열 연결하기 : + 사용

print('HELLO '+'WORLD')
#print('HELLO '+'WORLD ' + 2023)#TypeError: can only concatenate str (not "int") to str
print('HELLO '+'WORLD ' + str(2023))
#문자열 반복하기 : * 사용
#0이나 음수를 곱하면 빈 문자열 단, 실수는 곱할 수 없다(에러)
print('=' * 50)

