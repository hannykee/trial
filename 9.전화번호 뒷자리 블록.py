#전화번호 맨뒤 4자리 제외한 나머지 *로 바꾸기
#전화번호를 문자열 s로 입력받는 hide_numbes함수를 완성

#함수
def hide_numbers(s):
    s1=s[len(s)-4:len(s)] #len으로 세부 범위 설정!!!  #범위설정 시 반대로 하는 것 체크
    s2=s[0:len(s)-4]    #뒷 4자리를 제외한 나머지 앞자리
    s3='*'* len(s2)    #앞을 *기호로 바꿀 것(수정)
    s4=s3+s1
    print(s4)
    
#메인
s=input("전화번호를입력하세요.")
hide_numbers(s)
