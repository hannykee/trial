import re

re.search("\d+","햄버거가 무려 7000원이나 하다니!!")
#결과 : <_sre.SRE_Match object; span=(8, 12), match='7000'>

#여기에 group()을 넣으면 match의 값만 반환
#start() 매치된 문자열의 시작 위치를 리턴
#end() 매치된 문자열의 끝 위치를 리턴
#span() 매치된 문자열의 (시작, 끝) 에 해당되는 튜플을 리턴한다.

p=re.compile("[python]")
p.match("python")
m.group()

m.start()

m.end()

m.span()
