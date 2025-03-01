import re

txt = input('Enter: ')
x = re.sub(r'[,.\s]', ':', txt)

print(x)