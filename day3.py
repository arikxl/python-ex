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
