#CS 101 Lab
#Program Week 2
#Lily Dang
#ldvkd@mail.umkc.edu

#problem: calulate grades based on a weighted system

#alogrithm:
    #1 ask user to input who the grade is being calulated for
    #2 ask user to input grades for each category
    #3 calulate the indivual weighted grade for each category
    #4 calulate total grade by adding up all the indivual weighted grade
    #5 determine grade letter based on the range the total grade falls within
    #5 print the user's total weighted grade and grade letter

#error handling:
    #if user inputs grade above 100, change the grade to 100
    #if user inputs grade below 0, change the grade to 0
    

print('**** Welcome to the LAB grade calculator! ****\n')

#weights
labs = 0.7
lab_exams = 0.2
attendance = 0.1

name = input('Who are we calulating grades for? ')

print()

labs_grade = float(input('Enter the Labs grade: '))
if labs_grade > 100:
    print('The lab value should have been 100 or less. It has been change to 100.')
    labs_grade = 100 #changing inputed grade to 100
elif labs_grade < 0:
    print('The lab value should have been 0 or greater. It has been change to zero.')
    lab_grade = 0 #changing inputed grade to 0
print()

exam_grade = float(input('Enter the Exams grade: '))
if exam_grade > 100:
    print('The exam value should have been 100 or less. It has been change to 100.')
    exam_grade = 100 #changing inputed grade to 100 
elif exam_grade < 0:
    print('The exam value should have been 0 or greater. It has been change to zero.')
    exam_grade = 0 #changing inputed grade to 0
print()

attendance_grade = float(input('Enter the Attendance grade: '))
if attendance_grade > 100:
    print('The attendance value should have been 100 or less. It has been change to 100.')
    attendance_grade = 100 #changing inputed grade to 100
elif attendance_grade < 0:
    print('The attendance value should have been 0 or greater. It has been change to zero.')
    attendance_grade = 0 #changing inputed grade to 0
print()

#grades x weights
labs_wg = labs * labs_grade #weighted lab grade
exam_wg = lab_exams * exam_grade #weighted exam grade
attendance_wg = attendance * attendance_grade #weighted attendance grade

#weighted grade
total = labs_wg + exam_wg + attendance_wg #sum of the weighted lab, exam, and attendance grade

print('The weighted grade for', name, 'is {:.1f}'.format(total))

if (total >= 90) and (total <= 100): #percent range for grade letter A
    letter = 'A'
elif (total < 90) and (total >= 80): #percent range for grade letter B
    letter = 'B'
elif (total < 80) and (total >= 70): #percent range for grade letter C
    letter = 'C'
elif (total < 70) and (total >= 60): #percent range for grade letter D
    letter = 'D'
else:
    letter = 'F' #grade letter F
print(name, 'has a letter grade of', letter)
print()
print('**** Thanks for using the LAB grade calculator! ****')
