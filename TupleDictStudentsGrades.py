# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a
# student's name and their grade. For each student print all his/her grades and finally his/her average grade,' \
# ' formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
# The order in which we print the result does not matter.

def avg(values):
    return sum(values)/len(values)


students_number = int(input())
students = {}

for _ in range(students_number):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))
    
for student, grades in students.items():
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    grades_avg = avg(grades)
    print(f'{student} -> {grades_formatted} (avg: {grades_avg:.2f})')
