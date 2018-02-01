#빅데이터 분석반 복습_hannykee


#연습문제-  문자열에서 연속된 아이템이 제거된 리스트 만들기
#Life Hacking Point : 현관문 비밀번호(사이트 아이디/비밀번호)를 깜빡한 어머니에게 보안이 취약한 메세지로 비밀번호를 상기시켜줄 때

#함수 문제
def no_continuous(s):
    list_s=[]
    for i in range(0,len(s)):
        if s[i] not in list_s:
            list_s.append(s[i])
    return [list_s]


#변수정의
s=''
i=0
a=''

#메인 코드
s=input("매개변수를 입력하세요.")
test=no_continuous(s)
print("매개변수 입력 값에 대한 결과:", test)

