
n= input("진법을 입력하세요.")
a= input("수를 입력하세요.")
b= input("수를 입력하세요.")

if n=='2':
    ta2=int(a, 2) #2진수로 변환
    tb2=int(b, 2)
    result1= bin(ta2 & tb2) #비트 연산, 2진수로 변환
    result2= bin(ta2 | tb2)
    result3= bin(ta2 ^ tb2)
    
    print("두 수의 & 연산 결과 :" , result1)
    print("두 수의 | 연산 결과 :",  result2)
    print("두 수의 ^ 연산 결과 :",  result3)


elif n=='8':
    ta8=int(a, 8) #2진수로 변환
    tb8=int(b, 8)
    result1= oct(ta8 & tb8) #비트 연산, 8진수로 변환
    result2= oct(ta8 | tb8)
    result3= oct(ta8 ^ tb8)
    
    print("두 수의 & 연산 결과 :" , result1)
    print("두 수의 | 연산 결과 :",  result2)
    print("두 수의 ^ 연산 결과 :",  result3)


elif n=='10':
    ta10=int(a, 2) #2진수로 변환
    tb10=int(b, 2)
    result1= int(ta10 & tb10) #비트 연산, 10진수로 변환
    result2= int(ta10 | tb10)
    result3= int(ta10 ^ tb10)
    
    print("두 수의 & 연산 결과 :" , result1)
    print("두 수의 | 연산 결과 :",  result2)
    print("두 수의 ^ 연산 결과 :",  result3)


elif n=='16':
    ta16=int(a, 2) #2진수로 변환
    tb16=int(b, 2)
    result1= hex(ta16 & tb16) #비트 연산, 16진수로 변환
    result2= hex(ta16 | tb16)
    result3= hex(ta16 ^ tb16)
    
    print("두 수의 & 연산 결과 :" , result1)
    print("두 수의 | 연산 결과 :",  result2)
    print("두 수의 ^ 연산 결과 :",  result3)
