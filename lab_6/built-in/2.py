text = input('Enter: ')
upper_cnt, lower_cnt = 0, 0

for char in text:
    if char.isupper():
        upper_cnt+=1
    elif char.islower():
        lower_cnt+=1


print(f'The number of uppercase letters: {upper_cnt}')
print(f'The number of lowercase letters: {lower_cnt}')