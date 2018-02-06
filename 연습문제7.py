#연습문제7 - 가운데 문자 출력하기

#함수 이름
def getMiddle(a):
    if len(a)%2 == 0:
        b=len(a)
        c=int( (b/2) + 0.5)
        d=int( (b/2) - 0.5)
        mid0=a[d]
        mid1=a[c]
        print(mid0+mid1)
    else :
        b=len(a)
        c= int((b/2))
        mid2= a[c]
        print(mid2)

#메인 코드
a=input("하나의 단어를 입력하세요.")
getMiddle(a)


#라이프핵 포인트 추가
