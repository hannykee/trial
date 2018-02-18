#2번 문제 = 과락, 합격, 불합격

s1=int(input("첫 번째 과목 점수를 입력하세요."))
s2=int(input("두 번째 과목 점수를 입력하세요."))
s3=int(input("세 번째 과목 점수를 입력하세요."))

if s1 < 40 or s2 < 40 or s3 < 40:
    print("과락입니다.")
elif (s1 + s2 + s3)*3 >=60 :
    print("합격입니다.")
else:
    print("불합격입니다.")
