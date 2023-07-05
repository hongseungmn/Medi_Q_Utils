#str객체의 주요 메소드
from pprint import pp


def pprint(val):
    print(f'value:{val},type:{type(val)}')

print('1. join(Iterable 객체)')#주로 리스트를 문자열로 변환
#※단,리스트의 모든 요소는 문자열이어야 한다.리스트 요소중 하나라도 숫자인 경우 에러발생
#이런 경우 map함수를 보통 같이 적용한다.
a=['한라산','설악산','대둔산','덕유산']
b='▲'.join(a)
pprint(b)
a.append(2023)
print(a)
#b='▲'.join(a)#TypeError: sequence item 4: expected str instance, int found
b='▲'.join(map(str,a))
pprint(b)
print('2. split([구분자]) : 특정 구분자로 split해서 리스트로 반환(구분자 디폴트값은 공백)')
c=b.split('▲')
pprint(c)
#구분자가 없는 경우 문자열 전체가 리스트의 하나의 요소로 생성된다
d=b.split()
pprint(d)
print('3.replace():문자열 치환')
e='Hello World'
print(e.replace('World','Python'))
print(e)#str객체는 불변
print('4.lower():소문자로 변경')
print(e.lower())
print('5.upper():대문자로 변경')
print(e.upper())
print('6. lstrip([제거할 문자열 집합]):왼쪽부터 공백 혹은 지정한 문자열 집합 제거')
#※해당 값의 모든 조합으로 제거
#  제거할 문자열 집합은 제거할 단어를 넣거나 혹은 그 단어를 구성하는 알파벳를 넣자
#  단,공백이 있는 경우 반드시 공백도 포함시키자
f= '       Hello      World   '
print(f'X{f.lstrip()}Y')
print(f"X{f.lstrip(' Hello')}Y")
print(f"X{f.lstrip('He lo')}Y")
print(f"X{f.lstrip(' HeloWrd')}Y")
print('7. rstrip([제거할 문자열 집합]):오른쪽부터 공백 혹은 지정한 문자열 집합 제거')
print(f'X{f.rstrip()}Y')#X       Hello      WorldY
print(f"X{f.rstrip(' Hello')}Y")#X       Hello      WorldY
print(f"X{f.rstrip('dlorW ')}Y")#X       HeY
print(f"X{f.lstrip(' HeloWrd')}Y")#XY
print('8. rstrip([제거할 문자열 집합]):양쪽에서 공백 혹은 지정한 문자열 집합 제거')
print(f"X{f.strip()}Y")#XHello      WorldY
print(f"X{f.strip(' Helord')}Y")#XWY
print('9.zfill(자리수):0으로 자리수 채우기')
print('7'.zfill(2))
print('3.14'.zfill(6))
print('3.14'.zfill(3))#문자열의 길이보다 지정된 자리 폭의 길이가 작거나 같으면 아무것도 채우지 않는다
print('10.find()/rfind():찾은 문자열의 인덱스 반환')
g='Hello! He is a good'
print(g.find('He'))#왼쪽에서 부터 찾는다
print(g.rfind('He'))
print(g.find('he'))#찾은 문자열이 없는 경우 -1 반환
print('11.index()/rindex():찾은 문자열의 인덱스 반환')
print(g.index('He'))
print(g.rindex('He'))
#print(g.index('he'))#찾은 문자열이 없는 경우 ValueError: substring not found
print('12.count(문자열):문자열의 빈도수 반환')
print(g.count('He'))
print(g.count('o'))
print(g.count('he'))

