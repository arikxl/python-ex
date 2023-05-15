import math

# ********page 35********

def ex1():
    num = float('-inf')
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
ex2()