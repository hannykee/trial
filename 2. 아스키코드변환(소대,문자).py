#연습문제2- 입력된 소문자를 대문자 변환하기(아스키코드)
#라이프핵 포인트: <ord> 함수 사용하여 입력문자를 아스키 문자로 변환 (소/대문자 32차이)
#                 <chr> 함수 사용하여 아스키문자 일반문자로 변환

#숙제: 소문자 하나에서 소문자 열로 바꿔보기

#함수
def my_upper():
    b=int(ord(a)) #아스키 문자로 변환
    c= b-32 #소문자에서 대문자로 변환
    print(chr(c)) #숫자를 문자로 변환
    
#변수


#메인코드
a=input("소문자 하나를  입력하세요.")
#al=input("소문자 열을 입력하세요.")
my_upper()
