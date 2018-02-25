#while문 -무한루프 돌릴 때 사용
    #안쪽에 범위를 주지 않으면 조건을 벗어나는 문장을 스스로 만들지 못함
#주의#    조건 벗어나는 문장이 안 쪽에 들어가 있어야 한다!

a=0

while a<5:
    print(a)
    a +=1 # a=a+1과 같은 의미입니다



1부터 1000까지 더하는 프로그램
sum=0
x=1
while x < 1001 :
    sum += x
    x += 1 #탈출 조건이 필수 , if문의 증가값과 같음

print(sum) 



i,k,guguLine=


i=2 #시작값은 while문 밖에서 세팅
while i < 10: #조건문 끝 값 쓰고
    guguLine=
    i+=1  #하나씩 증가해야 한다. 중요! 명령을 다 실행하고 맨 마지막에 해야 함)

i=1

#########어려우니까 중첩은 for문을 활용하자! while안에도 for문 활용 
while i < 10:
    guguLine=""
    k=2 ## 구구단 다시 시작해야 하니까 위치 매우 중요#    
    while k <10:
        guguLine=guguLine+str("%2d)
        i+= 1
    print(guguLine)
    i += 1
#####

while은 무한루프 때 사용   ### ctrl + C 누르면 무한루프가 중지된다.

#while True:
print("ㅋ", end="")#


#반복문 탈출 문장
break문

위치는 출력하기 전에 break 문 삽입

if 어떤 것
        break


#break는 조건이 무엇이든 완전히 나옴
#continue 반복 중에 조건을 만나면 그 순간만 수행 안하고 다시 반복하러 넘어감


#1부터 100까지 더하되, 누적합계(hap)가 1000이상이 되는 시작 지점 구하기

hap, i=0,0

for i in range(1,101):
    hap += i
    if hap >=1000:
        break

print("1~100의 합에서 최초로 1000이 넘는 위치 : %d " %i)

