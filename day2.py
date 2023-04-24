# ********page 14********

def ex1():
    num1 = input('Choose the first number: ')
    num2 = input('Choose the second number: ')
    if num2 > num1:
        print('Growing...')
# ex1()


def ex4():
    num1 = int(input('Choose the first number: '))
    num2 = int(input('Choose the second number: '))
    if num1 % num2 == 0:
        print(f'{num1} is divisible by {num2} without remainder')
    if num2 % num1 == 0:
        print(f'{num2} is divisible by {num1} without remainder')
# ex4()


def ex5():
    num1 = int(input('Choose the first number: '))
    num2 = int(input('Choose the second number: '))
    if num1 < num2:
        print(f'{num1} \n {num2}')
    elif num2 < num1:
        print(f'{num2} \n {num1}')
    else:
        print(num1, num2)
# ex5()


def ex6():
    programmer_name = input('Programmer Name: ')
    current_salary = int(input('Current salary is: '))
    salary_after_raise = current_salary*1.1

    if salary_after_raise > 6000:
        salary_after_raise = current_salary*1.05

    print(f"{programmer_name}'s salary is {round(salary_after_raise,2)} after the raise.")
# ex6()