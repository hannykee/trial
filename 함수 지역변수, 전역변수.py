#2017-12-29





#지역변수(함수 자신만 사용하는 저장소), 전역변수(공용으로 사용하는 저장소)

#함수 선언 부분

def func1():
    a=10
    print("func1()에서 a의 값 %d " %a)

def func2():
    print("func2()에서 a의 값 %d" %a)

#변수 선언 부분
a=20

#메인코드 부분
func1() #10
func2() #20




#재귀호출함수(자기 자신을 끊임없이 부른다.)
#recursion

def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return factorial(n-1)*n
    
#1) 재귀호출은 자기 자신을 불러 진행하고
    #결과를 스택(stack)구조에 쌓아놓고 출력한다.
#2) 재귀호출 함수는 끝내는 조건이 존재해야한다.

호출지점		호출문장	
main		fact(5)=(24*5)	
fact(5)	return	fact(4)=(6*4)=24  *5
fact(4)	return	fact(3)=(2*6)=12  *4
fact(3)	return	fact(2)=(1*2)=2	  *3
fact(2)	return	fact(1)=(1*1)=1	  *2
fact(1)	return	fact(0)=1	  *1
fact(0)	return	#호출한 리턴 값은 함수를 지우고 들어간다.	


#함수를 변수에 저장할 수 있다.
#함수를 리스트에 담을 수 있다.



#함수를 매개변수로 사용하기

#함수 변수 담아 사용하는 것과 같다.
#함수 이름을 변수에 담고 그 변수를 통해 함수를 호출한다.

def hello_korean():
    print('안녕하세요.')
def hello_english():
    print('Hello.')
def greet(hello):
    hello()

greet(hello_korean)

greet(hello_english)



모듈: 많이 사용하는 함수를 만들어 놓고, 프로그램에서 해당 함수를 사용할 때
함수를 import 하여 사용하면 편리함
# 같은 위치에 활용 코드 저장


# 모듈 이름은 파일 이름으로 설정한다.


#함수를 호출할 때 'Func.함수이름()형식
#더 유용한 것은
모듈명 import 함수1,함수2,함수3
모듈명 import *


###
from Func import func1,func2,func3
또는 Func import *




#함수 모듈위치 변경은 일시적이다!
shell에서
import sys
sys.path
sys.path.append('')

#함수
import sys
sys.path.insert(0, "D:/p_temp_test")

import 함수
함수.dic(a=1,b=1)


#모듈에 중간에 함수가 변경되면
import imp
imp.reload(모듈이름)


