﻿import re

passw,idw,kname,ename,tel,hp,email,jumin,ip,sogae = '','','','','','','','','',''
r= re.compile("^[A-Z]([[가-힣][0-9]]{1,9})$"     )##ID 정규식
while True :
    str = input("ID입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         idw=str
         print(str)
         break   


r= re.compile("^[A-Z]\S{7,9}"     )##Password 정규식
while True :
    str = input("Password입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         passw=str
         print(str)
         break   

r= re.compile("[가-힣]+"     )##한글이름  정규식
while True :
    str = input("한글이름입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         kname=str
         print(str)
         break

r= re.compile( "[a-zA-Z]+"    )##영문이름 정규식
while True :
    str = input("영문이름입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         ename=str
         print(str)
         break

r= re.compile( "[15|16|17|18]\d[001:354]|d[01:24]"    )##학번입력 정규식
while True :
    str = input("학번입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         ename=str
         print(str)
         break

r= re.compile("\d{2,3}[-]\d{3,4}[-]\d{4}"     )##일반전화번호 정규식
while True :
    str = input("일반전화번호입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         tel=str
         print(str)
         break

r= re.compile("\d{3}[-]\d{4}[-]\d{4}"     )##핸드폰 번호 정규식
while True :
    str = input("핸드폰번호입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         hp=str
         print(str)
         break
        
r= re.compile("\w+[@][a-z]+[.][kr|com|net|edu]"     )##e-mail 정규식
while True :
    str = input("E-mail입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         email=str
         print(str)
         break
        
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

r= re.compile( "\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}"    )##ip주소 정규식
while True :
    str = input("ip주소입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         ip=str
         print(str)
         break     
    
r= re.compile("^[:alpha:]\[[가-힣]|[0-9]|[_]]+[.][^](exe|dll)")##자기소개서 파일 정규식
while True :
    str = input("자기소개서 파일입력")
    if r.search(str) == None:
         print("잘못입력")
         continue
    else :
         sogae=str
         print(str)
         break
       
  

        
        
        
