#간단한 그림판 프로그램 만들기
#마우스 이벤트js 

from tkinter import *

##변수##
window=None
canvas=None

##함수##

##메인 코드##

window=Tk() ##윈도우 만들고##
window.title("그림판 비슷한 프로그램") ##제목##
canvas= Canvas(window, height=300, width=300) ##작업영역 만들기##
canvas.pack() ##작업영역을 윈도우와 캔버스 묶아주는 함수##
window.mainloop() ##운영체제 메인 루프에 들어가서 화면에 띄워주세요##
