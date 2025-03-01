import re

txt = input('Enter: ')
x = re.findall('a.*b$', txt)

if x:
    print('There is a match!')
else:
    print('No match founded.')