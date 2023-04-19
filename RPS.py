import random

wins = 0
loses = 0

options = ['rock', 'scissors', 'paper']

while True:
    user_Choice = input('Type Rock/Paper/Scissors or Q to quit: ').lower()

    if user_Choice == "q":
        break

    if user_Choice not in options:
        continue

    random_num = random.randint(0, 2)
    computer = options[random_num]
    print(f'Computer is {computer}.')

    if computer == user_Choice:
        print('Its a draw!')
        continue

    if user_Choice == "rock" and computer == 'scissors' or user_Choice == "paper" and computer == 'rock' or user_Choice == "scissors" and computer == 'paper':
        print('You won!')
        wins += 1
        continue
    else: 
        print('Sorry. You lost!')
        loses +=1

print(f'You got {wins} points.')        
print(f'Computer got {loses} points.')        
print('GoodBYE!!❤️❤️')
