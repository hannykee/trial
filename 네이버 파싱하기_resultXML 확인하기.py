import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#라이브러리 불러옴



defaultURL = 'https://openapi.naver.com/v1/search/news.xml?'
#고정 url 네이버에서 긁어오기
#끝에 ? 꼭 붙여라 뒤에 더 있다는 의미
#블로그 https://openapi.naver.com/v1/search/blog.xml?
#카페 https://openapi.naver.com/v1/search/cafearticle.xml?
#이미지 https://openapi.naver.com/v1/search/image.xml?
#지식인 검색 https://openapi.naver.com/v1/search/kin.xml?



sort='sort=sim' #첫번째만 &없어도 됨.
start='&start=1'
display='&display=2' #100개를 가져온다. [몇 개 가져올지]
query='&query='+urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))

fullURL= defaultURL + sort + start + display + query
#fullURL로 합치기

print(fullURL)

file=open("naver_news3.txt","w",encoding='utf-8')

#파일명만 쓰기
#검색해서 넘길 때 받아 저장할 때 한글처리 utf-8로 바꿔야함.

headers={
    'Host':'openapi.naver.com',
    'User-Agent' : 'curl/7.43.0',
    'Accept':'*/*',
    'Content-Type':'application/xml',
    'X-Naver-Client-Id' : '2Jka9mtDaTWkqxFZsWM4',
    'X-Naver-Client-Secret': 'tqlg3iKdVZ'
    }


#headers=에 *딕셔너리 형태*로 보내야하는 정보 담음
#user-Agent 그대로 , Accept 다 받아주세요, 콘텐츠 타입, 아이디와 시크릿키*변수 이름 주의)

req = urllib.request.Request(fullURL,headers=headers)
#리퀘스트로 접근 (유알엘, 헤더스=헤더스)**주의: 가져가야할 속성 이름 = 내 변수 딕셔너리 이름
#req는 문을 여는 허락문서
#status 200 나올 것

f=urllib.request.urlopen(req)
#url 열고 읽고(변수에 저장)
#request는 접속, urlopen은 데이터를 웹문서에서 읽어오는 것 (허락문서 변수에 담기)

resultXML=f.read()
print(resultXML)

               
               


#strip=True 역슬러쉬 없애주고
#역슬러쉬 다시 만들어줌(보다 정확하게 하려고)
#이 경우 find_all은 가져와진 100개 나옴

#닫고
