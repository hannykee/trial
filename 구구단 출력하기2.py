#구구단 출력하기2

i,k, guguLine=0,0,""

for i in range(2,10):
    guguLine=guguLine+("  # %d단 #  " %i)# 이경우 서식이므로 str((서식))로 바꿔주어야 한다.
print(guguLine)

for k in range(1,10,1):
    guguLine="" #돌아오면 라인 초기화, 옆으로 올 때 항상 사용
    for i in range(2,10,1):
        guguLine=guguLine+str("%2d X %2d =%2d" % (i,k,i*k)) #서식, 수식을 가져와서 문자열로 만드는 str()
    print(guguLine)

