# ********page 15********

def ex5():
    name = input('Your name please: ')
    salary = int(input('Your salary please: '))
    if salary <= 23000:
        tax = salary * 0.1
    elif salary <= 46000:
        tax = 2300 + ((salary - 23000) * 0.2)
    elif salary <= 120000:
        tax = 6900 + ((salary - 46000) * 0.3)
    elif salary <= 220000:
        tax = 29100 + ((salary - 120000) * 0.4)
    else:
        tax = 69100 + ((salary - 220000) * 0.5)
    print(f'{name} is going to pay ${tax} tax.')
# ex5()

# ********page 17********


def ex4():
    year = int(input('Choose year: '))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')
# ex4()


def ex5():
    month = int(input('Choose month: '))
    year = int(input('Choose year: '))

    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days = 29
        else:
            days = 28
    else:
        days = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1]

    if days is not None:
        print(f'On month {month} on year {year} there is {days} days.')
    else:
        print('Please choose a month between 1-12')
# ex5()


# ********page 42********
def ex1(hours, minutes, seconds):

    hh = str(hours).zfill(2)
    mm = str(minutes).zfill(2)
    ss = str(seconds).zfill(2)
    return (f'{hh}:{mm}:{ss}')


# hours = int(input('Enter hours: '))
# minutes = int(input('Enter minutes: '))
# seconds = int(input('Enter seconds: '))
# print(ex1(hours, minutes, seconds))


# ********page 44********
def ex1():
    wins = 0
    draws = 0

    for i in range(3):
        score = input(f'What was the score of game {i+1}? (xx:xx): ')
        score_parts = score.split(':')
        MTA = int(score_parts[0])
        rivals = int(score_parts[1])

        if MTA > rivals:
            wins += 1
        elif MTA == rivals:
            draws += 1
    print(f'MTA got {wins * 2 + draws} points.')
# ex1()


def ex2():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    num3 = float(input("Enter number 3: "))
    num4 = float(input("Enter number 4: "))

    average = (num1 + num2 + num3 + num4) / 4

    if num1 == 0:
        average = 'there is no average (0)'
    elif num2 == 0:
        average = num1
    elif num3 == 0:
        average = (num1 + num2) / 2
    elif num4 == 0:
        average = (num1 + num2 + num3) / 3
    print(f'The average is: {average}')
# ex2()
