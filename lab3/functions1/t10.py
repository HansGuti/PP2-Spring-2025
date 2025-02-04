def uniqq(lst):
    new_list = []
    for x in lst:
        if x not in new_list:
            new_list.append(x)
    return new_list

user_input = input('Enter elements separated by spaces: ')
lst = user_input.split()
print(uniqq(lst))