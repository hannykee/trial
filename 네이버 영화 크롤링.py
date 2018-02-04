#네이버 영화 평점 크롤링하기_실습_hannykee

#필요한 패키지
import os
import urllib.parse
import urllib.request
import re
import time
import random

from bs4 import BeautifulSoup
#읽어올 페이지 URL : http://movie.naver.com/movie/bi/mi/basic.nhn?code=158191
# 1201572


url1='http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
url2='&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='

#네이버 개발자페이지에서 확인 가능(고정값)
hdr = {
    'User-Agent' : 'Mozilla/5.0(Windows NT 6.3; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/46.0.2490.86Safari/537.36',
    'Host' : 'movie.naver.com',
    'Connection' : 'keep-alive',
    'referer' : 'http://m.naver.com'
    }

def split_url():   #url을 읽어오는 함수 : 영화에서 뒷부분이 고유문자 code=158191
    
#http://movie.naver.com/movie/bi/mi/basic.nhn?code=158191
    url=input('url을 입력하세요: ')
    code_str = re.search('code=[0-9]*',url).group()  #정규식으로 code=뒤에 복수의 문자열(group)을 찾기
    code= re.search('[0-9]+', code_str).group()  #정규식으로 숫자 하나이상으로 이루어진 패턴 찾기

    return code  #숫자만 반환 fetch_reviews 함수로!

def fetch_score_result(URL):
    print(URL)
    result={}
    result_list = []

    res = urllib.request.Request(URL, headers=hdr)
    response=urllib.request.urlopen(res)

    html=response.read()

    soup = BeautifulSoup(html, 'html.parser')

    score_result = soup.find('div', class_='score_result').find('ul')  #div 안 클래스 속성이름이 score_result라는 네이버 댓글 구조 
    lis = score_result.find_all('li') # 그 안에 내용 li 태그로 읽어옴

    for li in lis:
        score = li.find('div', class_='star_score').find('em').get_text()  #평점은 em태그 안에 10처럼 숫자로 입력

        spectator = li.find('div', class_='score_reple').find('span').get_text() #작성자 이름  span태그 안에 있음 속성이름은 score_reple
        review = li.find('div', class_='score_reple').find('p').get_text() #댓글 내용 p태그 안에 있음 속성 이름은 

        if spectator =='관람객':
            review = review[3:]


        result['score'] = score
        result['review'] = review

        result_list.append({
            'score' : score,
            'review' : review
            })

    return result_list
#리스트로 점수와 후기 읽어옴.


def input_save_path():   #저장경로 설정 함수
    save_path = str(input("input save path: "))  #저장경로를 문자열로 받아서
    save_path = save_path.replace('\\','/')  #/를 \\로 바꿔주고
    if not os.path.isdir(os.path.split(save_path)[0]): #경로가 파이썬 리스트에 없으면 
        os.mkdir(os.path.split(save_path)[0]) #경로를 새로 만들어해준다.
    return save_path #사용자가 입력한 경로를 반환한다.

def fetch_reviews():
    code=split_url()  #숫자만 입력된 고유번호
    f=open(input_save_path(), 'w', encoding='utf-8')  #한글로 인코딩해서 쓰기모드, 경로 함수 실행하여 사용자가 입력한 경로 받음
    page = 1   #페이지 1에서 시작
    while True:   
        count = int(input('게시물의 검색 개수를 입력하세요(10단위): '))  #검색할 개수 받아서
        if count % 10 ==0:  #개수가 10인지 아닌지 확인하고, 10단위면 진행
            break
    l_count = 1  
    isLoop = True
    while isLoop:
        URL = url1 + code + url2 + str(page)
        result_list = fetch_score_result(URL)

        for r in result_list:

            f.write('==' * 40 + '\n')
            f.write('영화 평점: ' + r['score'] + '\n')
            f.write('리뷰 내용: ' + r['review'] + '\n')
            f.write('==' * 40 +'\n')
            l_count +=1
            if l_count > count:
                isLoop= False
                break
        page +=1
        if not isLoop or l_count ==count:
            isLoop= False
            break

        sleepTime = random.randint(4,10) #어떤 함수인지 다음에 알아보기!
        time.sleep(sleepTime)
        print(str(sleepTime) + '초 기다렸습니다.')
    f.close()
fetch_reviews()      #1. 제일 먼저 실행되는 함수
