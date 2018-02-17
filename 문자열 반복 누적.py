#print라는 문자열을 한 단어씩 누적 반복하여 출력하기

txt = "print"

i=0

for i in range(0,len(txt)+1):
    print(str(txt[0:i]))
    
