

student_result = []

for i in range(int(input('Number: '))):
    name = input('Name: ')
    score = float(input('Score: '))
    student_result.append([name, score])


unique_grades = sorted(set([score for name,score in student_result]))


second_lowest = unique_grades[1]

second_lowest_students = [name for name, score in student_result if score == second_lowest]

second_lowest_students_sorted = sorted(second_lowest_students)

for i in second_lowest_students_sorted:
    print(i)