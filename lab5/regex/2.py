import re
text = input('Enter the text: ')
x = re.findall(r'ab{2,3}', text)

if x:
    print(f'The match of {x} has been found!')
else:
    print('No match found.')