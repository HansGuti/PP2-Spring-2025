import re
text = input('Enter your text: ')
x = re.findall(r'ab*', text)
if x:
    print(f'Match of {x} has been found!')
else:
    print('Unfortunately, no match found.')