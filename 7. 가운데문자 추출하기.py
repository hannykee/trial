#연습문제7 - 문자열 중 가운데 문자 출력하기

#함수 이름
def getMiddle(a):
    if len(a)%2 == 0:   #짝수일 때와
        b=len(a)
        c=int( (b/2) )  #0.5에서 변경!
        d=int( (b/2) - 1)  
        mid0=a[d]  #인덱싱으로 문자 출력
        mid1=a[c]
        print(mid0+mid1)  #가운데 두글자 출력
    else :               #홀수일 때
        b=len(a)
        c= int((b/2))
        mid2= a[c]
        print(mid2)

#메인 코드
a=input("하나의 단어를 입력하세요.")
getMiddle(a)
