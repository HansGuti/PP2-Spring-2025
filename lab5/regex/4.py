import re

txt = input('Enter: ')
x = re.findall(r'[A-Z][a-z]+', txt)

if x:
    print(f'The sequences of one upper case letter followed by lower case letters: {x}')
else:
    print('No match founded.')