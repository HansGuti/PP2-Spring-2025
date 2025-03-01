import re

txt = input('Enter: ')
x = re.sub(r'[A-Za-z][A-Z]', lambda match: match.group(0)[0] + "_" + match.group(0)[1].lower(), txt)

print(x)