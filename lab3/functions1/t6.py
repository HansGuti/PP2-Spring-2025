def reversed_string(s):
    s_list = s.split()
    s_list.reverse()
    return ' '.join(s_list)

user_input = input('Enter a string: ')
print(reversed_string(user_input))