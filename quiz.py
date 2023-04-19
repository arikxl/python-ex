print('Welcome to HBS quiz!!!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print('Great! lets play!!')
score = 0

answer = input('Who is the best team? ')
if answer.lower() == 'hbs':
    print('💪🏼')
    score += 1
else:
    print('Incorrect')

answer = input('Who is the best player? ')
if answer.lower() == 'hatuel':
    print('💪🏼')
    score += 1
else:
    print('Incorrect')

answer = input('Who is the best coach? ')
if answer.lower() == 'barda':
    print('💪🏼')
    score += 1
else:
    print('Incorrect')

answer = input('Who is the best owner? ')
if answer.lower() == 'alona':
    print('💪🏼')
    score += 1
else:
    print('Incorrect')

answer = input('Who is the best GK? ')
if answer.lower() == 'glazer':
    print('💪🏼')
    score += 1
else:
    print('Incorrect')

print(f'Your score is {score}.')
print(f'Your grade is {score//5 *100}')
