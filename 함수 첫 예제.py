def cal(num1, num2, method='sum'):
    if method=='sum':
        print(num1+num2)
    elif method=='min':
        print(num1-num2)
    elif method=='prod':
        print(num1=num2)

cal(1,2)

cal(1,2,'prod')

cal(1,2,'min')

#기본값 다 넣고 / 인수 없이 호출하면 기본값으로 출력
def cal(num1, num2=2, method='sum'):
    if method=='sum':
        print(num1+num2)
    elif method=='min':
        print(num1-num2)
    elif method=='prod':
        print(num1=num2)

cal()

#기본값을 하나만 넣고 설정하면
#기본값을 줘야하면 다 줘야 하거나,
     #뒤에 값만 줄 수 있으나 맨 앞만 주는 건 오류난다.
def cal(num1=1, num2, method):
    if method=='sum':
        print(num1+num2)
    elif method=='min':
        print(num1-num2)
    elif method=='prod':
        print(num1=num2)
