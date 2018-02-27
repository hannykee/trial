#파이썬 환경설정 

#cmd에서 pip로 bs4다운로드 받기

from bs4 import BeautifulSoup


bs.find('p') #첫번째 만나는 p태그 하나의 처음<부터 마지막/>까지
        (p, 속성이름 ="값")
bs.find_all('p')
          (['p','img'])  #복수 검색은 리스트 형태로 묶어야 한다.
          
            ('^p') *import re ; re.compile('^p') # 정규식 사용 가
        # 속성으로도 검색할 수 있음

