import re
data="""
park 800905-1049118
kim 700905-1059119
"""
pat=re.compile("(\d{6})[-]\d{7}")    #d=숫자 {개수} [문자] 
print(pat.sub("\g<1>-*******", data))   #g<0> 밖에서부터 "큰따옴표" 그룹 g<1> 안 괄호 그룹
                                        #그대로 쓰고 -*******을 붙인다., 데이터라는 곳에서
                                        #패턴 부분화 하기
        #sub는 replace처럼 대체한다.
