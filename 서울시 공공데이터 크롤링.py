#서울시 오픈소스 크롤링

import urllib.request
from bs4 import BeautifulSoup
import re
import os

list_url="http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"
detail_url="http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"

def get_save_path():
    save_path= str(input("저장할 위치와 파일명을 적어주세요. :")) #저장할 위치와 파일명
    save_path=save_path.replace("\\","/")  #하나 들어가있는 것을 두개로\\바꿔라.

    if not os.path.isdir(os.path.split(save_path)[0]): #디렉토리 확인, 정확하게 경로와/파일명  즉(앞에 경로 있는지 확인)
        os.mkdir(os.path.split(save_path)[0])         #없으면 False return 잇으면 True

    return save_path #사용자가 입력한 대로

def fetch_list_url():  #14자리 숫자 찾아온다.-> return params(14자리 숫자 리스트)
    request_header=urllib.parse.urlencode({"page":"1"}) #페이지를 1번으로 무조건 넘겨준다.고정되어 있는 것
    request_header=request_header.encode("utf-8") #인코딩 정보 고정
    url=urllib.request.Request(list_url,request_header) #list_url주소와 requset_header(1번페이지로)를 가지고 접속한다.
    res=urllib.request.urlopen(url).read().decode("utf-8") #접속해서 열고 읽어오고, 디코드

    bs=BeautifulSoup(res, "html.parser")  #bs4가 쓸 수 있도록 res(html텍스트 형태)를 객체형태로 바꾸기(규칙)
    listbox = bs.find_all("ul",class_="pclist_list2") #ol/ul내 item태그 li의 클래스이름이이 ""인 것을 다 찾아온다.
    params=[]
    for i in listbox:
        params.append(re.search("[0-9]{14}",i.find("a")["href"]).group())  #숫자 14자리를 찾아서 넘겨준다.
                        #패턴매칭, 앵커 태그가 있는 14자리의 숫자를 묶어 가져오세요.  => 클릭한 제목 하나하나에 대한 고유번호
    return params

def fetch_detail_url(): 
    params=fetch_list_url()

    f=open(get_save_path(), 'w', encoding="utf-8") 

    for p in params:

        request_header = urllib.parse.urlencode({"RCEPT_NO" : str(p)})   #고유번호 ; p
        request_header = request_header.encode("utf-8")

        url=urllib.request.Request(detail_url, request_header)
        res=urllib.request.urlopen(url).read().decode("utf-8")

        bs=BeautifulSoup(res,"html.parser")
        div=bs.find("div",class_="form_table")

        tables=div.find_all("table")

        info= tables[0].find_all("td")

        title = info[0].get_text(strip=True)
        date = info[1].get_text(strip=True)

        question=tables[1].find("div", class_="table_inner_desc").get_text(strip=True)
        answer=tables[2].find("div", class_="table_inner_desc").get_text(strip=True)

        f.write("==" * 30 + "\n")

        f.write(title + "\n")
        f.write(date + "\n")
        f.write(question + "\n")
        f.write(answer + "\n")

        f.write("==" * 30 + "\n")


fetch_detail_url()
                      
