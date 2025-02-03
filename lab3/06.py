def reverse_string(s):
    words = s.split()
    reversed = words[::-1]
    return ' '.join(reversed)

s = input('Enter a sentence: ')
print('Reversed sentence:', reverse_string(s))    