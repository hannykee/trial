##공백제거하기 실습


inStr="<<<파<<이>>썬>>>"
outStr=""
outStr1=""

for i in range(0,len(inStr)) :
    if inStr[i]!='<' :
        outStr+=inStr[i]

for i in range(0,len(outStr)) :
    if outStr[i]!='>' :
        outStr1+=outStr[i]
    
print('원 문자열 ==> '+'['+inStr + ']')
print('공백 제거==>'+'[' + outStr1 + ']')


