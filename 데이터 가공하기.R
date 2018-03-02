#데이터 변형 기초문법(다양한 함수 사용법)
??ggplot   #함수 도움말 웹페이지로 이동하기
rm(list=ls())

library(googleVis)
Fruits
aggregate(Sales~Year,Fruits,sum)
aggregate(Sales~Fruit,Fruits,sum)

#추가 조건은 +로 확장이 가능하다
aggregate(Sales~Fruit,Fruits,max) #Furit별로 가장 많이 Sales 된 수량
aggregate(Sales~Location,Fruits,max)
aggregate(Sales~Fruit+Year,Fruits,max) 

#sapply#워드 클라우드에서 extractNoun이라는 함수를 전체에 적용
#apply함수는 matrix를 원칙으로 한다.


mat1<- matrix(c(1:6),nrow=2,byrow=T)
mat1

apply(mat1,1,sum) #각 행의 합계를 구하기
apply(mat1,2,sum) #각 열의 합계를 구하기

apply(mat1[,c(2,3)],2,max) #2열과 3열의 최댓갓 구하기

#lapply는 리스트에 적용된다. -> 리스트나 배열의 형태로 돌려준다!!
list1 <- list(Fruits$Sales)
#sapply는 리스트에 적용된다. -> 벡터의 형태로 돌려준다.
list2 <- list(Fruits$Profit)
lapply(c(list1,list2),max) #list1과 2에서 max값을 구해서 리스트 형태로 출력
sapply(c(list1,list2),max)
#값만 나오므로 주로 sapply를 사용한다.

lapply(Fruits[,c(4,5)],max)
sapply(Fruits[,c(4,5)],max)

#데이터 프레임을 대상으로 한 
tapply(출력값, 기준컬럽, 적용함수)
attach(Fruits)#######반드시 붙이고 사용한다.
tapply(Sales,Fruit,sum)
tapply(Sales,Year,sum)


#데이터 프레임이 아니 ㄴ벡터나 리ㅡ트 형태로 데이터 들이 있을 떄 
#마치 데이터프레임처럼 연산을 해주느 ㄴ함수는 
mapply(sum,vec1,vec2,vec3)




#sweep 함수로 한꺼번에 차이 구하기 #행렬말고도 다 적용 
#전체 - 기준값

mat1
a <- c(1,1,3)
sweep(mat1,2,a)

#length함수로 함수의 요소의 개수나 줄 수 파악하기
a<- c(1:5)
length(a)
length(Fruits) #데이터 프레임에서는 열의 개수를 센다!




ggplot2::geom_bar  #해당되는 패키지 안에 있는 값을 가져올 수 있다.




#정렬함수
sort1 <- Fruits$Sales
sort1
sort(sort1)
sort(sort1,decreasing = T)



#plyr 패키지
setwd("c:\\r_temp")
install.packages("plyr")
library(plyr)
fruits<-read.csv("fruits_10.csv,header=T")
fruits



######################################################################dplyr 패키지
install.packages("dplyr")
library(dplyr)
data1<- read.csv("2013년_프로야구선수_성적.csv")
data1


# 1. filter 조건을 주어서 필터링하기
data2 <- filter(data1,경기 >120)   #데이터,조건
data3 <- filter(data1,경기 >120 & 득점 >80)
data4 <- filter(data1, 포지션 %in% c('1루수','2루수'))   #or 은 | 사용한다. 

#2. select  특정 컬럼만 선택해서 사용
select(data1,선수명,포지션,팀) #컬럼을 데이터 뒤에 나열
select(data1,순위:타수)
select(data,-홈런,-타점,-도루)
#조합해서 사용하면 filter조건을 준 것을 select해서 그 친구들 열만 가져올 수 있따.
#         %>% 기법

data1 %>%
  select(선수명,팀,경기,타수)%>%
  filter(타수>400)  #출력값은 데이터프레임

#3. arrange 데이터 오름차순/내림차순 정렬
data1 %>%
  select(선수명,팀,경기,타수)%>%
  filter(타수>400)%>%
  arrange(타수)   #역정렬은 arrange(desc(타수))

#4. mutate 기존 변수 활용 새로운 변수 생성
data2 <- data1 %>% 
  select(선수명,팀,경기,타수)%>%
  mutate(경기x타수 = 경기*타수) %>%
  arrange(경기x타수)

#5. group_by 그룹 반들기
#5. summarise(with groop_by) 주어진 데이터를 집계한다.
#데이터 뜯어내기 -> (min,max,mean,count)
#단수(대상데이터)
data1 %>%
  group_by(팀)%>%
  summarise(avarage=mean(경기,na.rm=TRUE))  #na.rm=TRUE 잘못된 값 지우기
#복수(대상데이터)
data1 %>%
  group_by(팀)%>%
  summarise_each(funs(mean),경기,타수)  #(적용할 함수, 적용될 필드 나열)


data1%>%
  group_by(팀)%>%
  summarise_each(funs(mean,n()),경기,타수)
  





