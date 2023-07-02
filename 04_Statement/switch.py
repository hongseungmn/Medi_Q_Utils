'''
파이썬에는 switch문이 없다
딕션너리 와 사용자 정의 함수를 이용해서 switch문 효과를 낼수 있다
'''
kor,eng,math = map(int,input('세 개의 숫자 입력(공백구분)?').split())
avg = (kor+eng+math)//30
"""
def switch(key):
    '''
    학점을 반환하는 함수
    key:학점
    return:학점을 나타내는 문자열
    '''
    return {10:'A학점',9:"A학점",8:'B학점',7:'C학점',6:'D학점'}.get(key,'F학점')
print('평균:%.2f,학점:%s' % ((kor+eng+math)/3,switch(avg)))
"""
def switch(key):
    return {
        10:lambda : 'A학점',
        9: lambda: 'B학점',
        8: lambda: 'C학점',
        7: lambda: 'D학점',
        6: lambda: 'F학점',
        5: lambda: 'F학점',
        4: lambda: 'F학점',
        3: lambda: 'F학점',
        2: lambda: 'F학점',
        1: lambda: 'F학점',
        0: lambda: 'F학점'

    }[key]

#f = switch(avg)
#print('평균:%.2f,학점:%s' % ((kor+eng+math)/3,f()))
#위 두줄을 한줄로
print('평균:%.2f,학점:%s' % ((kor+eng+math)/3,switch(avg)()))
#print('value:{},type:{}'.format(f,type(f)))





