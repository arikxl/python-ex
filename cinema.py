films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 2],
    "Ghost Busters": [12, 0]
}

while True:
    choice = input('What film do you want to watch? ').title()

    if choice in films:
        age = int(input('How old are you? '))

        if age >= films[choice][0]:

            if films[choice][1] > 0 :
                print('enjoy the film.')
                films[choice][1]-=1
            else: 
                print('Sorry. there is no more seats available.')
        else:
            print('You are too young for this film...')
    else:
        print('We dont have that film.')