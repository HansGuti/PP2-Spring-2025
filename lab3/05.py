def permutator(s, answer = ''):
    if len(s) == 0:
        print(answer)
        return 
    for i in range(len(s)):
        c = s[i]
        res = s[:i] + s[i + 1:]
        permutator(res, answer + c)

start = input('Enter a string: ')
print('All permutations:')
permutator(start)