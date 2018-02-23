#이메일 형식인지 아닌지 확인하는 문제
import re

e=re.compile('\w+[@]\w+')
e.match("romain pasta")
e.group()

e.match("romainpasta@naver.com")
e.group()
