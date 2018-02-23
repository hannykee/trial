import re

re.search("[^ap]","apple")

re.search("[^ab]","bread")

re.search("[^ab]","orange")

print(re.search("[가-사]","강원도에서"))
print(re.search("[가-사]","강원도에서"))

re.search("\d+","햄버거가 무려 7000원이나 하다니!!").group()

