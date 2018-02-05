#1.연습문제

#함수
def print_readable_bin():
    num1=bin(num)  #숫자도 인덱스로 한자리씩 인식 가능합니다!
    list1= []

    for i in range(2,len(num1),4):
        list1.append(num1[i:i+4]) # 4개씩 잘라서 리스트로 뒤에 붙이기
    b='-'.join(list1)    
    print(b)
    

#변수

#메인
num=int(input("숫자를 입력하세요"))
print_readable_bin()
