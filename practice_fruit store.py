#연습문제 과일가게

#변수 선언 부분
fruit_name, fruit_num, sentence =0,0,0

fruit_name=input("어떤 과일 찾으세요?")
fruit_num=input("몇 개 드릴까요?")
sentence = "주문하신 과일은 %s %s 개 입니다"


print(sentence %(fruit_name, fruit_num))
