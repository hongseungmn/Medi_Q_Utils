#※break문과 continue문은 반복문 안에서만 사용가능
#break#SyntaxError: 'break' outside loop
#continue #SyntaxError: 'continue' outside loop
i=0
while i < 10000000000000000000000000000000000000000000000000000000000000000000000000:
    i+=1
    print('[i가 {}일때]'.format(i))
    print('continue문 이전 출력문')
    if i % 2 ==0: continue
    print('continue문 이후 출력문')
    print('break문 이전 출력문')
    if i==3: break
    print('break문 이후 출력문')