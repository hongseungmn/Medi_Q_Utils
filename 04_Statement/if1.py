#0,0.0,0+0j는 False와 같고 None,''(빈문자열) ,
#빈 이터레이터 객체([],{},(),set()등)는
#조건식으로 판단시 False로 간주된다
if not 0:
    print('0은 False다')
if not None:
    print('None은 False다')
if not '':
    print('\'\'은 False다')
if not []:
    print('[]은 False다')
#조건식은 모든 식이 될 수 있다
num1 =9
if num1:
    print('num1은',num1)
if num1 % 2:
    print('num1 % 2의 값은(산술식)',num1 % 2)
if num1 % 2==0 and num1 >=10:
    print('%d는 짝수고 10보다 크거나 같은 수이다' % num1)
#파이썬에서 조건식을 수학에서 사용하는 방식으로 간편화 할 수도 있다.
if 5 < num1 < 15:#num1 > 5 and num1 < 15
    print('{}는 5보다 크고 15보다 작다'.format(num1))
if num1 %2 ==0:
    pass
if num1 % 2 ==0 :
    print('num1은 %d이다' % num1)
    print('{}는 짝수다'.format(num1))

'''
ord(문자) : 문자의 아스키코드나 유니코드값을 반환
chr(숫자) : 숫자(아스키코드값 혹은 유니코드값)에 대응하는 문자를 반환
'''
print('[문자를 아스키(유니)코드로 변환]',ord('가'),sep='\n')
print('[아스키(유니)코드를 문자로 변환]',chr(44032),sep='\n')

code = ord(input('한 문자를 입력하세요?'))
print(code)
'''
문]사용자가 입력한 문자가 숫자인지 판단하여라
숫자면 "숫자입니다"라고 출력하여라
숫자가 아니면 "숫자가 아닙니다"라고 출력하여라
'''
isNumber = '0' <= chr(code) <= '9'
if isNumber:
    print('숫자입니다')
if not isNumber:
    print('숫자가 아닙니다')
'''
문]사용자가 입력한 값이 숫자인지 먼저 판단하고
   숫자라면 2의 배수인지를 판단하여
   2의 배수인 경우만 '2의 배수입니다'라고 출력하여라.
   2의 배수가 아닌 경우 '2의 배수가 아니다'라고 출력
   문자 '0'의 아스키 코드값:48, '1':49 '2':50......
'''
#방법1]하나의 조건식안에서 논리 연산으로 처리
isMultiple = '0'<=chr(code) <='9' and (code-ord('0')) %2 ==0
if isMultiple: print('2의 배수입니다')
if '0'<=chr(code) <='9' and (code-ord('0')) %2 !=0:print('2의 배수가 아닙니다')
#방법2]if문 안의 if문으로 처리
if '0'<=chr(code) <='9':
    isMultiple=(code-ord('0')) %2 ==0
    if isMultiple:
        print('2의 배수입니다')
    if not isMultiple:
        print('2의 배수가 아닙니다')

