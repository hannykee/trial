#os.path 모듈
#

import os
os

os.makedirs("C:\\Python34\\temp\\dir1\\dir2")


os.isdir("") #폴더 유무 판단하기 -T/F
# os.path.isdir("C:\\Python34\\NEWS.txt")
os.isfile("") #파일의 유무 판단하기 -T/F
#os.path.isfile("C:\\Python34\\NEWS.txt")

#확장자가 없는 파일도 많이 존재한다. 

os.path.exists("") #파일이나 폴더가 존재하는지 동시에 판단하기
os.path.getsize("") #파일의 크기 확인하기 (데이터 없으면 0)

os.path.split("") #파일과 폴더의 경로를 구분해주는 함수
os.path.spilttext("") #파일과 폴더의 경로, 확장자를 구분해주는 함수
os.path.join(join_1[0],join_1[1]) #파일이름과 폴더 이름을 합쳐주는 함수
os.path.dirname("") #경로를 돌려준다.
os.path.basename("") #파일명을 돌려준다.
