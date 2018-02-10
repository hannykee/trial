from tkinter import *

##변수##
window=None
canvas=None
x1, y1, x2, y2 = None, None, None, None     # 선의 시작점과 끝점 좌표

##함수##

#def는 블럭이 따로 설정된다.
def mouseClick(event):
        global x1, y1, x2, y2
        x1=event.x
        y1=event.y

def mouseDrop(event):
        global x1, y1, x2, y2
        x2=event.x
        y2=event.y
        canvas.create_line(x1,y1,x2,y2,width = 5, fill="red")


##메인 코드##

window=Tk() ##윈도우 만들고##
window.title("그림판 비슷한 프로그램") ##제목##
canvas= Canvas(window, height=300, width=300) ##작업영역 만들기##

canvas.bind("<Button-1>", mouseClick) #오른쪽 버튼 1번 / 왼쪽 버튼 2번
canvas.bind("<ButtonRelease-1>", mouseDrop)


canvas.pack() ##작업영역을 윈도우와 캔버스 묶아주는 함수##
window.mainloop() ##운영체제 메인 루프에 들어가서 화면에 띄워주세요##
