import re
#search는 문장의 어디에서든 나오는 부분을 우리에게 알려줌

#match는 그것이 문장의 처음에서 나오는지 알려줌


r=re.compile("[ab]")
print(r.search("pizza"))
#span=(4,5) 4번에서 만나서 4번에서 끝났다. match는 a를 찾아냈습니다.
print(r.match("pizza"))
#None 처음에 매칭이 되어 있지 않기 때문에 찾지 못한 결과.


#소문자나 대문자 피 찾고
r=re.compile("[pP]")

print(r.search("apple"))
 #search는 뒤에 상관 없이 가장 처음 나온 결과만 준다.
print(r.match("apPle"))
print(r.match("pP"))
#span=(0,1), match='p'




re.search("[pP]","apPle")
    #패턴이 시작하는 곳에서 가장 먼저 나오는 패턴 소문자 p나 대문자 P



