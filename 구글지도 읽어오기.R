#구글지도

setwd("c:\\r_temp")
install.packages("ggmap")
install.packages("stringr")
library(ggmap)
library(stringr)

loc <- read.csv("서울_강동구_공영주차장_위경도.csv",header=T)
loc
head(loc)

kd <- get_map("Amsa-dong",zoom=13, maptype = "roadmap")
    #구글에서 지도 불러오기("불러올 위치",zoom 확대정도,type)
kor.map <- ggmap(kd)+geom_point(data=loc, aes(x=37.546618, y=126.964747 ),size=3,alpha=0.7,color="red")
  #불러온 지도 그리기  #aes를 통해 위도와 경도 좌표 찍기 *aes안 데이터는 data항목에 있는 열 이름을 표시함
kor.map + geom_text(data=loc, aes(x = LON, y = LAT+0.001, label=주차장명),size=3)
           #  그 자리에 글자 찍기   #임의의 위치 설정(+0.001은 잘 안보일까봐 좌표 옆에 글씨쓰기)
ggsave("c:\\r_temp/kd.png",dpi=500)


#응용#
kd <- get_map("Amsa-dong",zoom=13, maptype = "roadmap")
#구글에서 지도 불러오기("불러올 위치",zoom 확대정도,type)
kor.map <- ggmap(kd)+geom_point(data=loc, aes(x=LON, y=LAT),size=3,alpha=0.7,color="red")
#불러온 지도 그리기  #aes를 통해 위도와 경도 좌표 찍기 *aes안 데이터는 data항목에 있는 열 이름을 표시함
kor.map + geom_text(data=loc, aes(x = LON, y = LAT+0.001, label=주차장명),size=3)
#  그 자리에 글자 찍기   #임의의 위치 설정(+0.001은 잘 안보일까봐 좌표 옆에 글씨쓰기)
ggsave("c:\\r_temp/kd.png",dpi=500)