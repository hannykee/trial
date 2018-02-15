#16진수를 구분하는 것
#진수의 규칙을 if문으로 연결하기

a, result=0,0

a=input("16진수 한 글자를 입력하세요.")

if (a > 'A' and a < 'G') or (a >= 'a' and a < 'g') or (a >= '0' and a <='9') :
	result = int(a, 16)
	print("10진수 == >" ,result)
else :
	print("16진수가 아닙니다.")
