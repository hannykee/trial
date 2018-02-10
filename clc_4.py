#간단한 계산기 -> 사용자의 입력을 받아서 사칙연산 자동으로 수행


a=int(input("첫 번째 숫자를 입력하세요 : "))
b=int(input("두 번째 숫자를 입력하세요 : "))
result=a+b
print(a, "+", b, "=", result)
result=a-b
print(a, "-", b, "=", result)
result=a*b
print(a, "*", b, "=", result)
result=a/b
print(a, "/", b, "=", result)
