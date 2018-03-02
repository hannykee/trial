library(dplyr)
exam <- read.csv("csv_exam.csv")
head(exam)
tail(exam)


exam %>% filter(class==1)

#복수 조건 가능 ( & )
# ( | )

#해당 열만 출력
exam %>% filter(class %in% c(1,3,5))
library(googleVis)
library(ggplot2)
mpg
#1번
mpg %>%
  group_by(class)%>%
  summarise(mean_cty = mean(cty))
#2번
mpg %>%
  group_by(class)%>%
  summarise(mean_cty = mean(cty))%>%
  arrange(desc(mean_cty))
#3번
mpg%>%
  