import random
print('Hello! What is your name?')
name = input()

x = random.randint(1, 20)

print(f'Well, {name}, I am thinking of a number between 1 and 20.')
cnt = 0
while True:
    print('Take a guess.')
    a = int(input())
    cnt += 1
    if a < x:
        print("Your guess is too low.")
    elif a > x:
        print('Your guess is too high.')
    else:
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
        break