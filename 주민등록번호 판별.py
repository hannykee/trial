import re

passw,idw,kname,ename,tel,hp,email,jumin,ip,sogae = '','','','','','','','','',''


r= re.compile("[00,99][01,12][01,31][-][1234]\d{6}")##주민번호 정규식
while True :
    str = input("주민번호입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         jumin=str
         print(str)
         break
