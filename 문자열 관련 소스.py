ss= "Python is Easy. 그래서 progrraming이 재미있다."
ss.upper()          #모두 대문자로#
ss.lower()          #모두 소문자로#
ss.swapcase()       #대소문자 상호 변환#
ss.title()          #맨 앞만 대문자로#

ss="아기다리 고기다리 던 방학이닷~!"
ss.count("기")
                    #변수.count(찾을 문자, 시작위치, 마지막위치-생략하면 0)#
ss.index("기",5)      #가장 먼저 만나는 결과만 보여줌 index(단어,시작위치)

##[예외처리] 반드시 조건문과 함께 사용- 에러처리되니까 if문 else문 ##
ss.find()
##[예외처리] -1로 결과가 나와서 조건문과 사용하기 용이함
ss.rfind() 오른쪽부터 셈
ss.startswith()
ss.endswith()       #시작과 끝에 원하는 문자를 넣을 경우 사용
# (, end="") 커서를 내려 라인이 넘어가는 것을 막아준다.

  #         ss=input("문자열 입력 ==> ")
print("출력 문자열 ==>",end='')

if ss.startswith('(')==False :
         print("(", end='')

print(ss, end='')

if ss.endswith(')')==False :
         print(')', end='') #


ss.lstrip() #왼쪽 공백 제거하기
ss.rstrip() #오른쪽 공백 제거하기
strip() #양쪽 공백 제거하기

#예시
exp1='----파----이----썬----'
print(exp1.strip('-'))
#파----이----썬


exp2='<<<파 << 이 >> 썬 >>>'
print(exp2.strip('<>'))
#파 << 이 >> 썬 


ss.replace("아기다리", "고기고기")
    #ss.replace(old,nex[, max]) *max는 최대 개수를 지정
#예시
str12 = "a-a-a-a-a"
str12.replace("a","b")
#b-b-b-b-b
str12.replace("a","b",3)
#b-b-b-a-a

#단어 쪼개기 - 일반 문자열을 리스트(자료구조)로 변경
ss.split()  #지정된 문자로 문자열을 나눠주고 리스트로 표현된다.
#예시

str12 = "a-a-a-a-a"
str12.split("-")
#['a', 'a', 'a', 'a', 'a']   #리스트
str12.split("-",3) #개수 지정하기
#['a', 'a', 'a', 'a-a']


len(ss) # 사용자가 입력한 문자의 글자 개수에 따라 (for문의 마지막 은 +1이므로 마지막요소 +1)
 #가운제 공백 제거
inStr="   한글   Python   프로그래밍   "
outStr=""

for i in range(0,len(inStr)) :
    if inStr[i]!=' ' :
        outStr+=inStr[i]
print('원 문자열 ==> '+'['+inStr + ']')
print('공백 제거==>'+'[' + outStr + ']')


#전체 개수를 센 이후에 해당되는 데이터가 공백이 아니라면 넘어가고, 공백이면 지우기

#지정한 문자 지우기

inStr="<<<파<<이>>썬>>>"
outStr=""
outStr1=""

for i in range(0,len(inStr)) :
    if inStr[i]!='<' :
        outStr+=inStr[i]

for i in range(0,len(outStr)) :
    if outStr[i]!='>' :
        outStr1+=outStr[i]
    
print('원 문자열 ==> '+'['+inStr + ']')
print('공백 제거==>'+'[' + outStr1 + ']')



##문자열 분리, 결합
split() #문자열을 공백이나 다른 문자로 분리해서 리스트를 반환
splitline() #행 단위로 분리
join() #문자열을 합해줌 #리스트를 결합할 때 주로 사용!

##List표시 [] 데이터 모음


#문자로 출력되도록(str)






#한꺼번에 많은 자료 받아들일 때 리스트를 사용


#리스트 + 리스트 = 뒤에 붙이기
#리스트[:] + 리스트[:] = 연산


#삭제는 구조 자체를 바꾸는 것del(aa[1])
# 여러개 한번에 삭제 aa[1:4] = []
                    #aa[1] = [] 절대 안됨!!
#반드시 기억


append()  #해당되는 데이터의 끝에 추가

insert()  #지정된 위치에 값을 삽입

len() #리스트 개수 추가되는지 확인







#글자 정형화 시킬 때 많이 사용(글자 개수 동일하게 맞추기)
center() #숫자만큼 전체 자릿수를 잡은 후 문자열을 가운데 배치
ljust() #왼쪽에 붙여 출력
rjust() #오른쪽에 붙여 출력
zfill() #오른쪽으로 붙여 쓰고 왼쪽 빈 공간은 0으로 채움



#정규식 들어갈 때 와일드 문자로 사용
#결과가 T나 F로 나온다 (문자열 구성 파악)
isdigit( ) # 전체가 숫자로만 구성되어 있는가
isalpha( ) # 전체가 글자(한글/영어)로만 구성되어 있는가
isalnum( ) # 전체가 글자와 숫자가 섞여서 구성되어 있는가
islower( ) # 전체가 소문자로만 구성되어 있는가
isupper( ) # 전체가 대문자로만 구성되어 있는가
isspace( ) # 전체가 공백문자로만 구성되어 있는가


#** 변수명이 아니라 문자열로 바로 쓸수도있

