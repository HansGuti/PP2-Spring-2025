import re

txt = input('Enter: ')
x = re.sub(r'[A-Za-z][A-Z]', lambda match: " ".join(match.group(0)), txt)

print(x)