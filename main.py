#!/bin/python3

''' This is a hackerrank question '''

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    newGr = []
    for i in range(len(grades)):
        if grades[i] < 38:
            newGr.append(grades[i])
        else:
            if grades[i] % 5 == 0:
                newGr.append(grades[i])
            elif (5 - (grades[i] % 5)) < 3:
                newGr.append((grades[i] // 5 + 1) * 5)
            else:
                newGr.append(grades[i])
    return newGr[::]

if __name__ == '__main__':
    

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
