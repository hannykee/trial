#a와 b는 인수니까 숫자가 아닌 이렇게 변수가 들어가야함
def sum(a,b) :
        #return 은 결과 값만 print는 출력
        a=a+b
        print(a)
        #return(a)
print(sum(1,2))
#3 함수에서 찍은 것
#3 print에서 찍은 것


# 함수호출 - 자주 사용하는 기능을 따로 함수로 설정
        #함수 모듈화#
#  import 함수  #파이썬 함수 가져오기

#return문이 존재하면 함수에서 실행 후 print함수 명령으로 넘어감
 # 않으면 안됨
#함수 값으로 메인에서 어떤 처리를 해야하면 return문 존재(전역변수)
#함수 값을 함수 내에서만 처리한다면 return쓰지 않음(지역변수)

#함수의 return값은 대입연산 오른쪽에 그대로 대입


#함수 정의 부분

def func1():
    result=100
    return result

def func2():
    print("반환값 없는 함수 실행")

#변수 선언 부분
hap=0
    
#메인 코드 부분
hap=func1()
print("func1()에서 돌려준 값 ==> %d " %hap)
func2()



#매개변수(parameter)
 1) 개수 정해놓고
 2) 인수개수 정해지지 않았을 때 앞에 *를 사용하면 모든 인수를 모아 튜플로 만듦



def sum(*a): #지금은 튜플 형태 별이 두개면 함수 형태가 딕셔너리 형태
    total = 0
    for i in a:
        total += i #total = total + i 라는 뜻입니다.#
        return total
        print(total)
        
sum(1,2,3)
sum(1,2,3,4)



def dic_func(**para):
    for k in para.keys():
        print ("%s --> %d 명입니다. " %(k, para[k]))
dic_func(아이오아이=11, 소녀시대=8, 걸스데이 =4, AOA =7)
#딕셔너리 형식, 함수를 호출할 때 딕셔너리 형식으로 키=값(value)으로 입력한다.

#값이 넘어오지 않으면 기본값으로 나옴
#뒤쪽부터  기본값으로 사용, 앞에 값은 없어도 기본값으로 넘어가서 실행됨(이 경우 앞의 값 하나만 매칭한다.
#기본값 위치에 기본 값이 들어가도록
#인수 3개에 기본값을 넣고 파라미터 없이 출력하면 어떻게 되는지

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
