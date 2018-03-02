#데이터 변형
install.packages("stringr")
library(stringr)

str_detect() #특정 문자 포함 여부 확인
str_detect(fruits,'A')
str_detect(fruits,^a) #정규식 사용 가능

str_detect(frutis,ignore.case('a')) #대소문자 무시하기
fruits <- c('apple','Apple','banana','pineapple')
str_count(fruits,ignore.case('a'))
str_count(fruits,'a')

##문자열 합치기
str_C("apple","banana")
str_C("Fruits:",fruits)
str_c(fruits,"name is",fruits)
str_c(fruits.collapse="")
str_c(fruits.collapse="-")

#문자 반복 출력
str_dup(fruits,3)

#문자열의 길이 출력
str_length('apple')
str_length(fruits)

#특정 문자의 위치 값 찾기
str_locate('apple','a',na.rm=T)
str_locate(fruits,'a',na.rm=T)

#문자 바꾸기 함수
str_replace('apple','p','*')
str_replace_all('apple','p','*')

#str_split()함수
fruits <- str_c('apple','/','orange','/','banana')
fruits

#기호 기준 분리
str_split(fruits,"/") 

#문자 떼어내기
fruits
str_sub(fruits,start=1,end=3)

#공백 제거하기
str_trim('  ')




#sqldf패키지 활용하기
#install.packages("sqldf")
library(sqldf)
library(googleVis)
Fruits

sqldf('SELECT *FROM Fruits') #모든 데이터 얹기
        #     필드이름(*모든)
sqldf('SELECT * FROM Fruits
      WHERE Fruit=\'Apples\'')
                    #문자그대로 'Apples'
     #      조건

#출력되는 행수제한
sqldf('SELECT *FROM Fruits limit 3')

#정렬해서 출력하기
sqldf('SELECT *FROM Fruits 
      ORDER BY Year')
sqldf('SELECT *FROM Fruits 
      ORDER BY Year,Sales')
sqldf('SELECT *FROM Fruits 
      ORDER BY Year Desc') #내림차순 역정렬



#그룹함수 사용하여 
#a)합계 판매량 구하기
sqldf('SELECT SUM(Sales) FROM Fruits')

sqldf('SELECT max(Sales) FROM Fruits')
#min()   AVG() 평균


#GROUP BY 사용하기 -> 과일 이름 별로 판매 합계 구하기
sqldf('SELECT Fruit, SUM(Sales)
      From Fruits
      GROUP BY Fruit')

######가장 많이 팔린 과일 이름 추출하기 (쿼리 내에 서브 쿼리에 넣을 수 있다.)
sqldf('SELECT Fruit
       FROM Fruits
      WHERE Sales=(select max(Sales) from Fruits)')

#주쿼리    Sales값이 111인지 찾아서 이름만 출력   서브쿼리(111)

#단일행 서브 쿼리 사용하기
sqldf('SELECT * FROM Fruits
      WHERE Sales > (SELECT Sales 
      FROM Fruits
      WHERE expenses=78)')


#평균 판매량
sqldf('SELECT Fruit, AVG(Sales)
      FROM Fruits
      GROUP BY Fruit')

#총 수량 파악하기
sqldf('SELECT COUNT(*) FROM Fruits')






