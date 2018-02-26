#os 모듈

import os
os

os.getcwd()  #현재 파이썬 작업 중 디렉터리 출력



os.chdir("C:\\temp") #체인지디렉토리 현재 작업 디렉터리 변경

for name in os.listdir("C:\\temp") #입력한 경로의 파일과 폴더 목록을 리스트로 반환

os.mkdir("C:\\Users\\student\\Desktop\\KH\\9일차\\test") #테스트란 디렉토리 만들어줌
        #현재 디렉토리에 추가할 것이면 ("이름만 입력") 해도 나옴
for name in os.listdir("C:\\Users\\student\\Desktop\\KH\\9일차"):
    print(name)

#권한이 없다고 나오면 관리자 권한으로 실행해야 한다.

os.makedirs("") #하위 폴더 포함 폴더를 만들어 준다.

os.remove("") #파일 지우기(파일 이름만 입력하면 현재폴더에서, 경로 지정하면 다른 폴더)

#원칙적으로 디렉토리 내 파일이 없어야 디렉터리 지울 수 있음

os.rmdir("폴더") #빈 디렉터리만 삭제 가능
os.removedirs("폴더") #하위 디렉토리도 지워가며 다수를 삭제
