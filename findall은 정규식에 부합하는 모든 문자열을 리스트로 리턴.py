#findall은 list로 넘어온다.

#공백이 있는 문자열에서 단어만 뽑기
import re
p=re.compile('[a-z]+')

result=p.findall("life is too short")
print(result)



#숫자만 추출하기
re.findall("\d+","서진수는 1975년 10월 23일 입니다 ^^")


#값 이외에 위치까지 함께
r=re.compile("[a-zA-Z]+")
result=r.finditer("My birthday is October 23th.")

for i in result:
    print(i.group())
    print(i.span())
