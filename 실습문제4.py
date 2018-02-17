#실습- *을 사용자가 입력한 만큼 반복하여 누적 출력하기- 중첩 for문 이용

a=int(input("원하는 *의 최대 개수를 입력하세요."))
print("당신이 입력한 개수는 %d 개 입니다." %a)

i,k=0,0
sum=""


for i in range(0,a+1): # 사용자가 입력한 개수개 만큼 반복하라
    for k in range(1,2): #변수가 하나씩 증가하면서 뒤에 별을 더하여 출력하라
        sum='*'

    print(sum*i)    
    if i==a+2:
        break
        
