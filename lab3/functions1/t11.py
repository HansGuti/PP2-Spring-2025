def palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        print('yes')
    else:
        print('no')
user_input = input('Palindrome checker: ')
palindrome(user_input)