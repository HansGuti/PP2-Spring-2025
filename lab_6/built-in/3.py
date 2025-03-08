s = input('Enter: ').lower()

if s == ''.join(reversed(s)):
    print('The string passed a palindrome test!')
else:
    print('Unfortunately, test did NOT pass.')
