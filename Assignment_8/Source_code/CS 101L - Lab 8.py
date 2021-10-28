############################################################################
##
## CS 101 Lab
## Lab 8
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM : 
##
## ALGORITHM : 
##      1. Start
##      2. Define multiple functions so that we can call the same piece of
##         code to run multiple times, rather than writing.
##      3. Use a while loop, so that the program runs until the user chooses
##         an input that quits the program.
##      4. Print the menu.
##      5. Ask user to input their choice.
##      6. Using the if-elif statements, compare user's choice to the options
##         on the menu.
##      7. Depending on the user's choice, call and run the respective function(s).
##      8. If user inputs 'Q', quit the program.
##      9. Stop
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
############################################################################

import math

def menu():
    menu = '\n{:^30}\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit'.format('Grade Menu')
    return menu

def add_test():
    while True:
        try:
            test_score = float(input(('\nEnter the new Test score 0-100 ==> ')))
            if test_score < 0:
                print('Test score cannot be a less than 0.')
                return add_test()
            else:
                test.append(test_score)
                break
        except ValueError:
            print('Not a valid input.')
            return add_test()
    
def remove_test():
    remove_test = float(input(('\nEnter the Test to remove ==> ')))
    if remove_test in test:
        test.remove(remove_test)
    else:
        print('Could not find that score to remove.')

def clear_test():
    test.clear()

def add_assignment():
    while True:
        try:
            assignment_score = float(input(('\nEnter the new Assignment score 0-100 ==> ')))
            if assignment_score < 0:
                print('Assignment score cannot be a less than 0.')
                return add_assignment()
            else:
                assignment.append(assignment_score)
                break
        except ValueError:
            print('Not a valid input.')

def remove_assignment():
    remove_assignment = float(input(('\nEnter the Assignment to remove ==> ')))
    if remove_assignment in assignment:
        assignment.remove(remove_assignment)
    else:
        print('Could not find that score to remove.')


def clear_assignment():
    assignment.clear()

def display_scores():
    print('\n{:<15}{:^10}{:^10}{:^10}{:^10}{:>5}'.format('Type', '#', 'min', 'max', 'avg', 'std'))
    print('=' * 60)
    print('{:<15}{:^10}{:^10}{:^10}{:^10}{:>5}'.format('Test', len1(test), min1(test), max1(test), avg(test), std(test)))
    print('{:<15}{:^10}{:^10}{:^10}{:^10}{:>5}'.format('Test', len1(assignment), min1(assignment), max1(assignment), avg(assignment), std(assignment)))

    weight()

def len1(list_type):
    '''Find the total number of tests or assignments'''
    try:
        return len(list_type)
    except:
        return 'n/a'

def min1(list_type):
    '''Find the min'''
    try:
        return '{:.1f}'.format(min(list_type))
    except:
        return 'n/a'

def max1(list_type):
    '''Find the max'''
    try:
        return '{:.2f}'.format(max(list_type))
    except:
        return 'n/a'


def avg(list_type):
    '''Calculate the average'''
    try:
        avg = sum(list_type) / len(list_type)
        return '{:.2f}'.format(avg)
    except:
        return 'n/a'

def std(list_type):
    '''Calculate the standard deviation'''
    try:
        summation = 0
        list_avg = sum(list_type) / len(list_type)
        for score in list_type:
            num = (score - list_avg) ** 2
            summation += num
        std = math.sqrt((summation) / len(list_type))
        return '{:.2f}'.format(std)
    except:
        return 'n/a'

def weight():
    '''Calculate the total weight of the tests and assignments'''
    test_weight = 0
    test_weight = 0

    # for when their is no value in the test list or assignment list, assign 0 as the weight for the list with no values
    if avg(test) == 'n/a':
        test_weight = 0
    if avg(assignment) == 'n/a':
        assignment_weight = 0

    if avg(test) != 'n/a': # test accounts for 60% of a student's grade
        test_weight = float(avg(test)) * 0.60
    if avg(assignment) != 'n/a': # assignment acounts accounts for 60% of a student's grade
        assignment_weight = float(avg(assignment)) * 0.40

    
    if test_weight == 0: # for when the test weight is 0, set the total weight to the assignment_weight 
        total_weight = assignment_weight
    elif assignment_weight == 0: # for when the assignmetn weight is 0, set the total weight to the test_weight 
        total_weight = test_weight
    else: # calculate the total weighted grade
        total_weight = test_weight + assignment_weight
        
    print('\nThe weighted score is {:.2f}'.format(total_weight))

test = []
assignment = []
run = True
while run:
    print(menu())
    user_choice = input('\nEnter your choice ==> ')
    if user_choice == '1': # add test
        add_test()
    elif user_choice == '2': # remove test
        remove_test()
    elif user_choice == '3': # clear test
        clear_test()
    elif user_choice == '4': # add assignment
        add_assignment()
    elif user_choice == '5': # remove assignment 
        remove_assignment()
    elif user_choice == '6': # clear assignment
        clear_assignment()
    elif (user_choice == 'D') or (user_choice == 'd'): # display scores
        display_scores()
    elif (user_choice == 'Q') or (user_choice == 'q'): # quit program 
        run = False
    else: # invalid cholice 
        print('\nYou must select a valid choice. Enter 1, 2, 3, 4, 5, 6, D, or Q')
