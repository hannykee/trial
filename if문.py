반드시 반복문에서는 변수 선언을 먼저 해야한다.

#if 문

# if 항목 in 리스트:
if '딸기' in fruit:
    print("딸기가 있네요")


#함수 : 
eval() #실행가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수
#) hi + a = hia , 2+5 = 7

divmod(a,b) # 2개의 숫자를 입력으로 받아, 나누기를 해서 몫과 나머지를 구함



#for문 
반복횟수 in list1   #튜플, 문자열, 리스트
        in (1,2,3,4,5)
        in range(:)
#  i 는 본인이 임의로 설정하면 되고, i에 반복해야할 데이터가 들어가게 된다. 
리스트인쇄
for i in list1:
    print(i)
누적합계    
sum=0
for i in range(0,1001)
sum += i
            
#range 함수(시작값, 끝값+1, 증가값 #i가 증가값씩 증가한다.즉, 간격) -> 리스트 결과값으로 돌려준다.:

#출력 한줄로 하기 (1내용,end="")
짝수를 만들기
0부터10까지(명령에는 11),2씩 증가

i,hap=0,0

for i in range(1,11,1):
    hap=hap+i
print("1에서 10까지의 합 : %d" %hap)



500과 1000 사이에 있는 홀수의 합 구하기

i,hap=0,0

for i in range(501,1001,2) :

    hap = hap+i

print


#만약 7의 배수의 합계라면 in range(500가까운 7의 배수, ,7):
                        #안 쪽에 if문으로 설정
                         # in range(7,101,7)

#사용자로부터 입력한 값까지 더하는 것 -> range에 변수 사용 가능
num1=int(input))
for i in range(0,num2,2):


#중첩 반복문 => 변수 2개 (구구단 예시 81번 반복을 좌항 우항 각각)


#while문


#break, continue(제어)문

