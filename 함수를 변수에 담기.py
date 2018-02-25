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
