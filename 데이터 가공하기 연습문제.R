library(googleVis)
Fruits
library(dplyr)

#1번
Fruits_2 <- filter(Fruits,Expenses>80)

#2번
Fruits_3 <- filter(Fruits,Expenses>90&Sales>90)

#3번
Fruits_4 <- filter(Fruits,Expenses >90 |Sales >80)

#4번
Fruits_5 <- filter(Fruits,Expenses %in% c(79,91))

#5번
select(Fruits,Fruit:Sales,-Location)

#6번
Fruits%>%
  group_by(Fruit)%>%
  summarise(sum= sum(Sales,na.rm=TRUE))

#7번
Fruits %>%
  group_by(Fruit)%>%
  summarise_each(funs(sum),Sales,Profit)


#apply
#1
data1 <- read.csv("data1.csv",header=T)
class(data1)
apply(data1[,c(2:15)],2,sum)
apply(data1[,c(2:15)],1,sum)

#2-1
data2 <- read.csv("1-4호선승하차승객수.csv",header=T)
#2-2
attach(data2)
tapply(승차,노선번호,sum) #노선번호별 승차인원수 합
tapply(하차,노선번호,sum) #노선번호별 하차인원 
apply(data2[,c(3,4)],2,sum)
aggregate(승차+하차~노선번호,data2,sum)
aggregate(승차~노선번호,data2,sum)
aggregate(하차~노선번호,data2,sum)

Fruits
#aggregate문법1
aggregate(Sales~Fruit,Fruits,mean)
aggregate(Expenses~Fruit,Fruits,max)
aggregate(Profit~Fruit,Fruits,min)
aggregate(Sales~Location,Fruits,mean)
aggregate(Profit~Fruit,Fruits,sum)
aggregate(Sales~Year,Fruits,sum)
aggregate(Expenses~Fruit,Fruits,mean)
aggregate(Profit~Location+Fruit,Fruits,mean)
aggregate(Sales~Location+Year,Fruits,sum)
aggregate(Expenses~Location+Fruit,Fruits,sum)
aggregate(Profit~Location+Year,Fruits,max)

#실습문제(2)보고서
data1 <- read.csv("data1.csv",header=T)
head(data1)
#1 apply
apply(data1[-1],2,sum)
apply(data1[-1],1,sum)
apply(data1[,c(10:14)],2,sum)
apply(data1[,c(10:14)],1,sum)
d1 <- apply(data1[,c(2,7,12)],2,sum)
d2 <- apply(data1[,c(2,7,12)],1,sum)

#sapply
sapply(data1[-1],sum)
sapply(data1[,c(10:14)],sum)
sapply(data1[,c(2,7,12)],sum)


#실습문제(3)보고서
#1번
data2 <-read.csv('1-4호선승하차승객수.csv',header=T)
head(data2)
attach(data2)
#2번
tapply(승차,노선번호,sum)
#3번
tapply(하차,노선번호,sum)
#4번
apply(data2[,c(3,4)],2,sum)
#5번
tapply(승차,노선번호,mean)
tapply(하차,노선번호,mean)
#6번
apply(data2[,c(3,4)],2,max)
apply(data2[,c(3,4)],2,min)
#7번
tapply(승차+하차,노선번호,min)

#실습문제(3)보고서 aggregate문법2
#1
aggregate(승차+하차~노선번호,data2,sum)
#2
aggregate(승차~노선번호,data2,sum)
#3
aggregate(하차~노선번호,data2,sum)
#4
aggregate(승차~노선번호,data2,mean)
#5
aggregate(하차~노선번호,data2,min)
#6
aggregate(승차+하차~노선번호,data2,max)
