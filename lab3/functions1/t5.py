def permutator(s, answer = ''):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        x = s[i]
        res = s[:i] + s[i + 1:]
        permutator(res, answer + x)

user_input = input('Enter a string: ')
(permutator(user_input))
