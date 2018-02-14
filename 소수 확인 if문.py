#소수 확인 if문

#입력 숫자 소수인지 일반숫자인지 확인

a = int (input("정수를 입력하세요"))

for i in range(2, a):
    if a%i == 0:
        print("일반숫자입니다.")
                break
    else:
        print("소수입니다.")
