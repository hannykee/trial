#웹페이지 한글 주소 인코딩하기

import urllib.parse

#def input_query(): #urllib.parse.quote_plus 사용 안함
#    q=str(input("검색어 입력하세요:"))
#    return "&query="+q
#print(input_query()) #quote는 공백문자를 %20으로 바꿔줌

def input_query():   #공백문자를 +로 바꿔줌
    q=urllib.parse.quote_plus(str(input("검색어 입력하세요: ")))
    return "&query=" +q
print(input_query())
