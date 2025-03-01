import re

txt = input('Enter a string: ')
x = re.findall(r'[a-z]+_[a-z]+', txt)

if x:
    print(f'The sequences of lowercase letters joined with an underscore are {x}.')
else:
    print('No match founded.')
