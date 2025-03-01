import re

txt = input('Enter: ')
x = re.split('[A-Z]', txt)
print(x)
