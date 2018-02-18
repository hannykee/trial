#1.주사위 게임#

import random

jack= random.randrange(1,7)
jill= random.randrange(1,7)
print("jack의 주사위 숫자: %d jill의 주사위 숫자 : %d" %(jack,jill))


if jack > jill :
    print("jack이 이겼습니다.")
elif jack == jill:
    print("jack 과 jill이 비겼습니다.")
else :
    print("jill이 이겼습니다.")

