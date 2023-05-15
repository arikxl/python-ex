# ********page 35********

def ex1(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            # print(i)
            return 'Not Sorted'
    return 'Sorted'

print(ex1([1,2,9,4,5,6,7,8]))
print('****')
print(ex1([1,2,3,4,5,6,7,8]))