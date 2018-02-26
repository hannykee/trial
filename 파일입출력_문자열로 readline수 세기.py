
r=open("test.txt","r")
str,count="",0
for a in range(0,6):
    file=r.readline()
    count+=len(file)
    
print(count)
r.close()


