#CS 101 Lab
#Program 2
#Brandon Barber
#bmbct7@umsystem.edu

'''In this problem we will be computing a students weighted grade based on 
the input of their name, and grades for each of the different grading segments.
 We will then be outputting their weighted grade and the letter grade'''

print('**** Welcome to the LAB grade calculator! ****\n')
student_name = input('Who are we calculating grades for? ')
lab_grade = float(input('\nEnter the Labs grade? '))

if lab_grade < 0:
    lab_grade = 0
    print('The lab value should be 0-100, it has been changed to 0.')
elif lab_grade > 100:
    lab_grade = 100
    print('The lab value should be 0-100, it has been changed to 100.')

exam_grade = float(input('\nEnter the EXAMS grade? '))

if exam_grade < 0:
    exam_grade = 0
    print('The exam value should be 0-100, it has been changed to 0.')
elif exam_grade > 100:
    exam_grade = 100
    print('The exam value should be 0-100, it has been changed to 100.')

attendance = float(input('\nEnter the Attendance grade? '))

if attendance < 0:
    attendance = 0
    print('The attendance value should be 0-100, it has been changed to 0.')
elif attendance > 100:
    attendance = 100
    print('The attendance value should be 0-100, it has been changed to 100.')

weighted_lab = lab_grade * 0.7
weighted_exam = exam_grade * 0.2
weighted_attendance = attendance * 0.1

weighted_grade = weighted_lab + weighted_exam + weighted_attendance

print('The weighted grade for {} is {}'.format(student_name, weighted_grade))
if weighted_grade >= 90:
    print(student_name, 'has a letter grade of A')
elif weighted_grade >= 80:
    print(student_name, 'has a letter grade of B')
elif weighted_grade >= 70:
    print(student_name, 'has a letter grade of C')
elif weighted_grade >= 60:
    print(student_name, 'has a letter grade of D')
else:
    print(student_name, 'has a letter grade of F')

print('\n**** Thanks for using the Lab grade calculator ****')