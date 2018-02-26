#urllib
import urllib.request   #리퀘스트 객채 import 
req=urllib.request      #변수에 넣기
req.urlopen("http://wikidocs.net/")  #url 만들어서 서버 열고

d=req.urlopen("https://wikidocs.net/")
status=d.getheaders()       #생략가능 (나의 상태 확인할 때 사용)
for s in status:
	print(s)
d.status        #200이 정상상태


d.read() #read로 웹페이지 소스코드 읽어오기


#parsing 내가 원하는 정보를 선별하여 긁어오기(정규식 사용)
#파싱을 편하게 해주는 Beautiful Soup 모듈
