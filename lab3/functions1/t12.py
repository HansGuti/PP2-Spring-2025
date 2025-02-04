def histogram(h):
    for i in range(0, len(h)):
        print('*' * int(h[i]))
user_input = input('Enter a list of integers separated by space: ')
h = user_input.split()
histogram(h)