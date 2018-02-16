#사용자에게 시작,끝,배수설정 입력 받아 계산

i,hap=0,0
num1,num2,num3=0,0,0

num1=int(input("시작값 입력 : "))
num2=int(input("끝값 입력 : "))
num3=int(input("설정할 배수 입력 : ")) #입력된 배수들의 범위 내 합

for i in range(num1,num2+1) :
    if i % num3 == 0:
        hap =hap + i

    
print("%d에서 %d까지 %d의 배수의 합 : %d" %(num1,num2,num3,hap))
