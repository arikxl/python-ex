grades = [15, 92, 76, 88, 25, 92, 78, 0, 38, 92, 100, 92, 47, 91, 92, 89, 95, 92, 84, 93, 92, 96, 88, 92, 95, 50, 92, 86, 92, 64, 91, 92, 89, 72, 97, 90, 82, 95, 92, 88, 92, 94, 91, 92, 89, 92, 95, 90, 92, 86, 92, 94, 91, 92, 89, 92, 97, 90, 92, 95, 92, 88, 92, 94, 91, 92, 89, 92, 95, 90, 92, 86, 92, 94, 91, 92, 89, 92, 97, 90, 12, 95, 92, 88, 92, 0, 91, 92, 89, 22, 95, 90, 92, 86, 92, 34, 91, 92, 89, 42, 97, 100, 92, 95]

def ex1():
    max_grade = max(grades)
    count_max_grade = grades.count(max_grade)
    print(f'The max grade is: {max_grade}')
    print(f'{count_max_grade} students got the max grade ({max_grade})')
# ex1()

def ex2():
    grades_above_eighty =[]
    for i in range(len(grades)):
        if grades[i] > 80:
            grades_above_eighty.append(i)
        if len(grades_above_eighty) == 5:
            print(grades_above_eighty)
            break
ex2()