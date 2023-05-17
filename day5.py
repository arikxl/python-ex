import math

# ********page 35********

def ex1():
    num = 0
    for i in range(1, 11):
        new_num = int(input('Choose a number: '))
        if num > new_num:
            # print(i)
            return 'Not Sorted'
        else:
            num = new_num
    return 'Sorted'
# print(ex1())


def ex4():
    votes = {
        1: 0,  # agree
        2: 0,  # against
        3: 0  # abstain
    }

    for i in range(1, 171):
        vote = int(input('Enter vote code (1-4): '))
        if vote == 1:
            votes[1] += 1
        elif vote == 2:
            votes[2] += 1
        elif vote == 3:
            votes[3] += 1
        elif vote == 4:
            print(f'Vote of "Veto" was cast by country number: {i}.')
            return

    print('Number of "Agree" votes:', votes[1])
    print('Number of "Against" votes:', votes[2])
    print('Number of "Abstain" votes:', votes[3])
# ex4()



# ********page 37********

# def ex1():



def ex2():
    for i in range(1, 101):
        number = int(input('Choose a number: '))
        factorial = math.factorial(number)
        print(f'The factorial of {number} is {factorial}.')
# ex2()


def ex5():
    number = int(input('Choose a number: '))
    i = number
    while i > 0:
        print(*range(1, i+1))
        i -= 1
# ex5()



# ********page 38********


def ex9():
    for i in range(1, 21):
        row = []
        for j in range(1, 21):
            row.append(i * j)
        print(*row)
# ex9()

def ex12():
    max_salary = float('-inf')
    highest_employee = ''
    highest_month = ''

    for _ in range(200):
        employee_name = input('Enter employee name: ')
        salaries = list(map(int, input('Enter 12 monthly salaries (separated by space): ').split()))

        if max(salaries) > max_salary:
            max_salary = max(salaries)
            highest_employee = employee_name
            highest_month = salaries.index(max_salary) + 1

    print(f'The employee with the highest salary is {highest_employee}.')
    print(f'The highest salary of {highest_employee} is {max_salary}.')
    print(f"The month of {highest_employee}'s highest salary is {highest_month}.")

ex12()
