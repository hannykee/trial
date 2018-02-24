import re
url = '<a href="C:\Python34\Koala.jpg"> 그림 </a><font size="10">'
print(re.search('href="(.*?)">',url).group(1))



#.한문자가 *0번이상 반복 ">로 닫혀야 한다.
