#split()함수 - 주어진 문자열을 특정 패턴을 기준으로 분리한다.
import re
re.spilt('[:]+','apple orange : grape cherry')

re.split('[: ]+' 'apple orange : grape cherry')
   #:와 공백으로 분리
