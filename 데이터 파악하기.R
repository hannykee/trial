#데이터 파악하기

setwd("c:\\r_temp")
exam <- read.csv("csv_exam.csv")
View(exam)
head(exam)
tail(exam)

library(ggplot2)

mpg<- as.data.frame(ggplot2::mpg)  #mpg는 ggplot2의 예제 데이터
head(mpg)
str(mpg)
length(mpg)


##전처리 패키기
install.packages("dplyr")
library(dplyr)
#1
mpg<- as.data.frame(ggplot2::mpg)
head(mpg)
#2
df_new <- rename(mpg, city = cty)
df_new <- rename(mpg, highway =hwy)
#3
head(df_new)





##파생변수 만들기

df <- data.frame(var1 = c(4,3,8),
                 var2 = c(2,6,1))
df
#sum 열 붙이기
df$var_sum <- df$var1 + df$var2   
df$var_mean <- (df$var1 + df$var2)/2
df
#############




#파생변수1)mpg의 통합 연비 변수 생성하기
mpg$total <- (mpg$cty + mpg$hwy)/2
head(mpg)

mean(mpg$total)  #전체적 자동자의 연비 평균 구할 수 있다.
#제거를 위한 mpg$total <- NULL

#파생변수2) 통합 연비 mean 대비 적절한지 판단하는 변수
                    #기준 값을 확인하기 위해
summary(mpg$total)  #요약통계량 산
#중간값과 평균 확인하면 나름 고르다
hist(mpg$total)

#하위 값 판단할 테스트 20값 이상이면 pass 그렇지 않으면 fail

mpg$test <- ifelse(mpg$total >=20, "pass", "fail")
head(mpg)

#빈도수 보여주는 것 table
table(mpg$test)
qplot(mpg$test) #ggplot2



mpg$grade <- ifelse(mpg$total >=30,"A",
                    ifelse(mpg$total >= 20, "B","C"))
head(mpg)
table(mpg$grade)  #등급 빈도표 생성
qplot(mpg$grade)


mpg$grade2 <- ifelse(mpg$total >=30, "A",
                     ifelse(mpg$total >=25, "B",
                     ifelse(mpg$total >=20, "C","D")))

head(mpg)


#실습 1번
mid<- as.data.frame(ggplot2::midwest)
head(midwest)
tail(midwest)
summary(midwest)
str(midwest)

#실습2\
mid <- rename(mid, total = poptotal)
mid <- rename(mid, asian = popasian)
head(mid)


#실습3
mid$ratio = mid$asian / mid$total
qplot(mid$ratio)

#실습4
mean(mid$ratio)

#실습5
mid$grade <- ifelse(mid$ratio >= 0.00487,"large","small")

#실습6
table(mid$grade)
qplot(mid$grade)

