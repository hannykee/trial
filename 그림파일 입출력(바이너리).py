#바이너리 읽어서 새로운 파일로 쓰기 모드
k_image=open("C:\\Python34\\Koala.png","rb")  #rb로 바이너리로 파일 읽어오기
k_image_2=open("C:\\Python34\\Koala_2.png","wb") #wb로 바이너리로 저장할 파일 생성

k_image_2.write(k_image.read())    #k1에서 읽어온 이미지를 k2로 쓰기

k_image.close()  #반드시 두개 다 닫아야한다.
k_image_2.close()
