def string(s):
    return string(s[1:]) + s[0]
s = input()
print(string(s))