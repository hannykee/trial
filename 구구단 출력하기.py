#구구단 출력하기

i,k=0,0

for i in range(2,10,1):
    print("\n - %d단 - \n" %i)
    for k in range(1,10,1):
        print(" %d X %d= %2d" %(i, k, i*k))
 #한 줄 떨어지기, #단입니다 표시되기
#i 값과 k 값들이 끝 값이 되거나 하나 넘을 때 종료된다.
              
