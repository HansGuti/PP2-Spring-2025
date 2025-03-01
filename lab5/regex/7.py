import re

txt = input('Enter: ')
x = re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), txt)

print(x)