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
print(ex1())

