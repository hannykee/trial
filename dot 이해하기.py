import re

r=re.compile("a.c")
print(r.search("abc"))

print(r.search("afc"))

print(r.search("ac"))


#.는 하나 이상의 모든 문자
#?는 0또는 1개의 문자
#*는 0번 이상 즉, a*는 a가 무한정 있어도 되고 없어도 된다.
#+는 1개 이상의 반복을 필요로 한다.
#{m,n}
#{2} 반드시 두 번 나와야 함
#{3, } 최솟값 3부터 무한대까지
