#이미지 크롤링 소스

import urllib.parse
import urllib.request
import re


#함수
def bind_url(): #URL을 만들어준다.
    default_url='https://openapi.naver.com/v1/search/image.xml?'
    start='&start=1'
    sort='&sort=sim'
    display='&display=10'
    query='&query='+urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))
    full_url= default_url + sort + display + query
    #print(full_url)
    return full_url

def fetch_contents_from_url(): #요청하고 열어서 데이터를 가져옴-> 요구하는 방법이 달라짐
    url=bind_url()
    headers={
        'Host':'openapi.naver.com',
        'User-Agent' : 'curl/7.43.0',
        'Accept':'*/*',
        'Content-Type':'application/xml',
        'X-Naver-Client-Id' : '2Jka9mtDaTWkqxFZsWM4',
        'X-Naver-Client-Secret': 'tqlg3iKdVZ'
        }
    r=urllib.request.Request(url,headers=headers)
    m=urllib.request.urlopen(r)
    html=m.read()
    return html

def extract_text_in_tags(tags,tagname="title"): #태그 지워줌(bs4대신)
    txt = []
    reg = "[^<" +tagname+">][^<]+" #정규식
    #print(reg)
    for tag in tags :
        txt.append(re.search(reg,tag).group()) #bs4를 사용하지 않고 정규식만 가지고 파싱한다.
    print(txt)
    return txt

def get_contents_from_html():
    html=fetch_contents_from_url()
    #print(html)
    title_tags=re.findall("<title>[^<]+</title>",html.decode('utf-8'))#정규식  #타이틀 태그(내 타이틀, 아이템 나옴) #태그로 둘러쌓인 것 bs4에서는 title_getitle인데, 못하니까 위 함수에서 <제거해줌
    link_tags=re.findall("<link>[^<]+</link>",html.decode('utf-8'))#정규식  #utf-8로 디코딩해라(이상한 원문을 한글로 바꿈)
    print(link_tags)
    titles= extract_text_in_tags(title_tags,tagname="title")
    links= extract_text_in_tags(link_tags,tagname='link')
    f= open("image.html","w")
    f.write("<html><body>")
    for i in range(1,len(titles)):
        f.write("<p>"+titles[i]+"</p>")
        f.write("<img src="+links[i]+" />")
    f.write("</body></html>")
    f.close()

get_contents_from_html()


#bs4사용하고 있지 않음-> 정규식만 가지고 작업한다.
#파일이 다운되는 것이 아니라 이미지 주소만 읽어온다. 파일을 메모장에서 열면 소스 복붙하여 다운로드 명령을 따로 줘야 다운로드
