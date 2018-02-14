#문자열 타입 확인 함수

sentence=input("값을 입력하세요")


if sentence.isalpha():
    print("글자입니다.")

if sentence.isdigit():
    print("숫자입니다.")

if sentence.isalnum():
    print("영숫자입니다.")

else:
    print("모르겠습니다.")

