#연습문제 8 - 워터멜론

def water_melon(n):
    list10=""

    
    for i in range(1,n+1):
        
        if i % 2 == 0: #짝수 번호면 수 인쇄
            list10+='박'
        else : #홀수 번호면 박 인쇄
            list10+='수'
        
    return(list10)


#메인코드
n=int(input("정수 n을 매개변수로 입력하세요."))

nr=water_melon(n)
n3=water_melon(3)
n4=water_melon(4)
print("입력한 n:", nr)
print("n이 3인 경우: " ,n3 )
print("n이 4인 경우: " ,n4 )

#라이프핵 포인트 추가
