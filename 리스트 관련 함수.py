#한꺼번에 많은 자료 받아들일 때 리스트를 사용


#리스트 + 리스트 = 뒤에 붙이기
#리스트[:] + 리스트[:] = 연산


#삭제는 구조 자체를 바꾸는 것del(aa[1])
# 여러개 한번에 삭제 aa[1:4] = []
                    #aa[1] = [] 절대 안됨!!
#반드시 기억


append()  #해당되는 데이터의 끝에 추가(누적)

insert()  #지정된 위치에 값을 삽입

len() #리스트 개수 확인



aa=[]
for i in range(0,100) :
    aa.apend(0)

len(aa)

#리스트 하나씩 수 증가하며 
aa=[]
for i in range(0,100) :
    aa.apend(i)

len(aa)


#리스트 조작 함수 피피티에서 긁어오기
insert() <-> del()
reverse() sort() 차
append() pop() 차이



#리스트 안에 또다른 리스트
#변수[2][1] 인덱싱 2차원으로 한다.
