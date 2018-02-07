#연습문제3 - 급여계산
#라이프핵 포인트 : 나의 아르바이트 순수익 계산

#함수호출
def calc_monthly_salary():
    pay_t= time * pay
    ri= pay_t - trn
    print("1일 급여는 %d 입니다." %pay_t)
    print("하루 순수익은 %d 입니다." %ri)
    print("아르바이트 순수익은 %d 입니다." %(ri*day))

#변수
day, time, pay, trn, pay_t, ri =0,0,0,0,0,0
#메인코드

day=int(input("1.이번달 근무 일수를 입력하세요"))
time=int(input("2.하루 근무 시간을 입력하세요"))
pay=int(input("3.시간당 급여를 입력하세요(단위:원)"))
trn=int(input("4.하루 왕복 교통비를 입력하세요(단위:원)"))
calc_monthly_salary()
