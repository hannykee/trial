#1.연습문제 - 이진수로 변환하고, 눈으로 보기 편하도록 4자리씩 자르기 
#2. 라이프핵 포인트

#함수
def print_readable_bin():
    num1=bin(num)  #숫자도 인덱스로 한자리씩 인식 가능합니다!
    list1= []

    for i in range(2,len(num1),4):  #명령구조 (2부터 num1의 길이-1까지, 4개 구간폭으로 실행하며 반복한다.)
        list1.append(num1[i:i+4]) # 4개씩 잘라서 리스트로 뒤에 붙이기(예 인덱스1,2,3,4까지)
    b='-'.join(list1)  #4개 단위에서 -기호 삽입하기  
    print(b) #나눠진 이진수 출력
    

#변수

#메인
num=int(input("숫자를 입력하세요"))
print_readable_bin()
