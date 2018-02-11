##실습) 시프트 연산##
#시프트할 숫자 입력0, 출력할 횟수 입력0 

a = int(input("시프트할 숫자를 입력하세요"))
b = int(input("출력할 횟수를 입력하세요"))

result=0
i=0

for i in range(1,b+1):
    result = a <<i
    print("%d << %d = %d" %(a, i, result))

for i in range(1,b+1):
    result = a>> i
    print("%d>> %d= %d" %(a, i, result))
