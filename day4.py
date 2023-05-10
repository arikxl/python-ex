# ********page 24********

def ex1():
    top = int(input('Choose a number: '))
    for num in range(1, top+1):
        print(num)
# ex1()


def ex2():
    min = int(input('Choose a minimum number: '))
    top = int(input('Choose a maximum number: '))

    if min > top:
        temp = min
        min = top
        top = temp

    for num in range(min, top+1):
        print(num)
# ex2()


def ex3():
    n = int(input('Choose a number: '))
    for i in range(0, n + 1, 2):
        print(i)
# ex3()


def ex4():
    max = int(input('Choose the first number: '))
    den = int(input('Choose the second number: '))
    for i in range(0, max + 1, den):
        print(i)
# ex4()


def ex7():
    max_value = int(input('Choose a number: '))
    while True:
        num = int(input('Choose a number: '))
        if num <= 0:
            break
        if num > max_value:
            max_value = num
    print(f'The highest value entered is: {max_value}')

# ex7()


def ex8():
    min_value = int(input('Choose a number: '))
    while True:
        num = int(input('Choose a number: '))
        if num <= 0:
            break
        if num < min_value:
            min_value = num
    print(f'The lowest value entered is: {min_value}')
# ex8()


def ex9():
    highest_number = 0
    for i in range(1, 10):
        num = int(input(f'Enter number {i}: '))
        if num > highest_number:
            highest_number = num
            highest_index = i
    print(
        f'The highest number is {highest_number} and its index is {highest_index}')
# ex9()


def ex10():
    num = int(input('Choose a number: '))
    leftmost_digit = str(num)[0]
    print(f'The leftmost digit of {num} is {leftmost_digit}')
# ex10()


def ex11():
    num = int(input('Choose a number: '))
    number_of_digits = len(str(num))
    print(
        f'The number of digit of {num} is {number_of_digits}')
# ex11()


def ex13():
    num = int(input('Choose a number: '))
    digit = int(input('Choose a single digit: '))
    num_str = str(num)
    count =0

    for char in num_str:
        if int(char) == digit:
            count += 1
    print(f'The digit {digit} appears {count} times in the number {num}')
# ex13()


def ex14():
    num = int(input('Choose a number: '))
    num_str = str(num)
    reversed_str = num_str[::-1]
    print(reversed_str)
# ex14()


def ex15():
    num = int(input('Choose a number: '))
    num_str = str(num)
    if num_str == num_str[::-1]:
        print(f'{num} is a Palindrome!')
    else:
        print(f'{num} is not a Palindrome!')
# ex15()
