known_users = ['Alice', 'Bob', 'Claire', 'Emma', 'Fred','Greg', 'Harry']

while True:
    print('Hi. My name is Travis')
    name = input('Enter your name: ').capitalize()

    if name in known_users:
        print(f'Hello {name}!')
        remove = input('Would you like to be removed from the system? (y/n) ').lower()
        if remove == 'y':
            known_users.remove(name)
            print(known_users)
        elif remove == 'n':
            print(f'bye {name}')
        else:
            print('Invalid key')
    else:
        print(f'{name} is NOT recognised. ')
        add_me = input('Would you like to be added to the system? (y/n) ').lower()
        if add_me == 'y':
            known_users.append(name)
            print(known_users)
        else:
            print(f'bye {name}')
