#구구단 거꾸로 출력하기

user1=0
user1=int(input("원하는 단을 입력하세요"))
print("몇단? %d " %user1)

k=0
for k in range(9,0,-1):
    print(" %d X %d= %2d" %(user1, k, user1*k))

              
