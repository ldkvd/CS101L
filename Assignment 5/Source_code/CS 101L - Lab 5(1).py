########################################################################
##
## CS 101 Lab
## Lab 5
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM : To come up with a new library card numbering system for students that
##           includes the students grades and school. 
##
## ALGORITHM : 
##      1. Start
##      2. Print the heading. 
##      3. Have user enter library card number. 
##      4. Run through the various functions and verify the card:
##              a. check if the length of the card is 10 characters
##              b. check if the first 5 characters are A-Z
##              c. check if the sixth character is 1, 2, or 3
##              d. check if the seventh character is 1, 2, 3, or 4
##              e. check if the eighth, ninth, and tenth characters are an
##                 integer between 0 and 9 and if the eighth matches the 
##                 calculated value.
##      5. If valid, print "Library card is valid" and the respective outputs.
##      6. If invalid, print "Library card is invalid" and the error.
##      7. Stop
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string


def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    char_int = ord(char)
    if char_int > 64:
        char_int -= 65
    else:
        char_int -= 48
    return char_int
    
def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    sum_value = 0
    for i in range(len(idnumber)):
        value = character_value(idnumber[i])
        sum_value = sum_value + value * (i+1)
    return sum_value % 10

def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    

def verify_check_digit(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    if len(idnumber) != 10:
        return (False, 'The length of the number given must be 10')
    for i in range(5):
        if idnumber[i] < 'A' or idnumber[i] > 'Z':
            return (False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(i, idnumber[i]))
    for i in range(7, 10):
        if idnumber[i] < '0' or idnumber [i] > '9':
            return(False, 'The last 3 characters must be 0-9, the invalid character is at {} is {}'.format(i, idnumber))
    if (idnumber[5].isdigit() == False) or (int(idnumber[5]) not in range (4)):
        return(False, 'The sixth character must be 1 2 or 3')
    if (idnumber[6].isdigit() == False) or (int(idnumber[6]) not in range (5)):
        return(False, 'The seventh character must be 1 2 3 or 4')
    if get_check_digit(idnumber) != int(idnumber[9]):
        return(False, 'Check Digit {} does not match calculated value {}.'.format(idnumber[9], get_check_digit(idnumber)))
    return(True, "")

def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if idnumber[5] == '1':
        return 'School of Computing and Engineering SCE'
    if idnumber[5] == '2':
        return 'School of Law'
    if idnumber[5] == '3':
        return 'College of Arts and Sciences'
    if idnumber[5] != '1' or '2' or '3':
        return 'Invalid School'
  
def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    if idnumber[6] == '1':
        return 'Freshman'
    if idnumber[6] == '2':
        return 'Sophomore'
    if idnumber[6] == '3':
        return 'Junior'
    if idnumber[6] == '4':
        return 'Senior'
    if idnumber[6] == '5':
        return 'Invalid Grade'
   

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        
