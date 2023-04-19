import random

max = input('Choose the max number: ')
if max.isdigit():
    max = int(max)
else:
    print('Please type only numbers')
    quit()

random_num = random.randint(1, max)
guesses = 0

while True:
    guesses += 1
    guess = input(f'Guess the number between 1-{max}: ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type only numbers')
        continue

    if guess == random_num:
        print('Great guess!')
        max += 5
        break
    elif guess < random_num:
            print('Your guess is below the number')
    else:
            print('Your guess is above the number')


print(f'You did it in {guesses} guesses')
