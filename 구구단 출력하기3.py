#구구단 출력하기3

a,b=0,0

a= int(input("시작단 값을 입력하세요."))
b= int(input("끝단 값을 입력하세요."))
if a>=b or (a <=0 or a > 9) or (b <=0 or b > 9):
       print("잘못된 값을 입력하셨습니다. 다시 입력해주세요.")

i,k,guguLine=0,0,""

for i in range(a,b+1):
       guguLine=guguLine +str( "  # %d단  #   " % i)
print(guguLine)
       
for k in range(1,10):
    guguLine="" #돌아와서 라인 초기화
    for i in range(a,b+1):
       guguLine=guguLine+str("%2d X %2d = %2d " % (i,k,i*k))
    print(guguLine)



