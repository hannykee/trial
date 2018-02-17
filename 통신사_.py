#사용자가 입력한 번호의 통신사 출력
#입력 출력은 메인에서
#함수는 search에서 결과만 넘기게끔
#반드시 모든 번호를 입력받고 앞에만 추출해서 함수로 넘긴 후에 짝을 찾아서
#데이터 메인으로 다시 ##return문이 존재한다.

#함수    조건:함수부분에서는 검색만 하세요!
def search_tel(input1):
    input2= input1.split("-") #결과가 리스트로 나타난다.
    input3=str(input2[0])
    dic1={'011':'SKT','016':'KT','019':'LGT','010':'알수없음'}
    return dic1[input3]
#변수
input1,input2,input3="",[],""

#메인
input1=input("휴대번호를 입력하세요.")
tel=search_tel(input1)
print("당신이 입력한 번호의 통신사는 %s 입니다" %tel)
