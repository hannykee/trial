##연습문제 1 - 급여지급##

##변수 선언##
time, money, pay_t, result=0,0,0,0

##메인

time = int(input("당신의 근로시간을 입력하세요.")) 
money = int(input("당신의 시간당 임금을 입력하세요."))
pay_t= money * time #사용자에 의해 입력받은 급여를 계산#

result= "당신의 급여는 %s원  입니다"

print(result % pay_t)
          

