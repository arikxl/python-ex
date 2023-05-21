grades = [51, 92, 76, 88, 99, 12, 78, 0, 38, 92, 100, 50, 47, 91, 92, 89, 95, 92, 84, 93, 92, 96, 88, 92, 95, 50, 92, 86, 32, 64, 91, 92, 89, 72, 97, 90, 82, 95, 42, 88, 92, 94, 91, 92, 89, 92, 95, 90, 92, 86, 92, 94, 91, 92, 89, 92, 97, 90, 92, 95, 92, 88, 92, 94, 91, 92, 89, 92, 95, 90, 92, 86, 92, 94, 91, 92, 89, 92, 97, 90, 12, 95, 2, 88, 92, 0, 91, 82, 89, 22, 95, 90, 92, 86, 72, 34, 91, 62, 89, 42, 97, 100, 52, 95]
grades1= [1,95,3,4,90,1,2,3,4,90]

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
        if len(grades_above_eighty) == 5 or i == len(grades)-1:
            if len(grades_above_eighty)==0:
                print('didnt find any grades above 80')
            else:
                print(grades_above_eighty)
                break
# ex2()


def ex3():
    grade_distribution = [0] * 101
    for grade in grades:
        grade_distribution[grade] += 1

    for grade in sorted(range(len(grade_distribution)), reverse=True):
        count = grade_distribution[grade]
        if count > 0:
            print(f'{grade}: {count}')
# ex3()


def ex4():
    grade_distribution = [0] * 101
    total_students_above_fifty = 0
    for grade in grades1:
        grade_distribution[grade] += 1

    for grade in range(len(grade_distribution)):
        count = grade_distribution[grade]
        if grade > 49:
            total_students_above_fifty +=count
            print(f'{grade}: {count}')


            # if total_students_above_fifty >0:
            #     percentage =  (count / total_students_above_fifty) * 100
                # print(percentage)
                # print(f'{grade}: {percentage:.2f}%')
            # print(f'{grade}: {(count / total_students_above_fifty) * 100}')
    print(total_students_above_fifty)
    # percentage = (count_above_50 / total_students) * 100
    # print(total_students_above_fifty)

ex4()