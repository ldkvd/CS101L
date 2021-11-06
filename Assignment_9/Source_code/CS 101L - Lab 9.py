#############################################################################
##
## CS 101 Lab
## Lab 9
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM : Read a data file containing crime information. Output the month
## that has the highest crime rate, the offense that occurs the most, and
## then ask for an offense and output a formatted report of the zip code and
## how many times that offense occurs in that zip code
##
## ALGORITHM : 
##      1. Start.
##      2. Define functions and variables.
##      3. In the main program, ask user to enter name of the file to be read.
##         Use Try/Except.
##      4. Call the function that returns the month and the highest number
##         of crimes for that month
##      5. Print a message to the user displaying the month with the
##         highest number of crimes.
##      6. Call the function that returns the offense with the highest 
##         number of crimes and the total value.
##      7. Print a message to the user displaying the offense with the highest
##         number of crimes.
##      8. Ask user to input an offense to output the formatted report of the
##         zipcode and how many times the offense occurs in that zip code.
##      9. Stop. 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
##############################################################################

import csv 

def month_from_number(integer):
    '''Takes an integer and returns the month'''
    month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return month_dict[integer]

def read_in_file(my_file):
    '''Returns a list of lines from the file'''
    file = open(my_file, encoding ="utf-8")
    file_csv = csv.reader(file)
            
    new_list = []
    for line in file_csv:
        new_list.append(line)
    del new_list[0]
    file.close()
    return new_list
    
def create_reported_data_dict(my_file):
    '''Returns a dictionary where the key is the date and the value is the total
    crime occurences for that day'''
    crime_count = {}
    for row in my_file:
        if row[1] in crime_count:
            crime_count[row[1]] += 1
        else:
            crime_count[row[1]] = 1
    return crime_count
        
def create_reported_month_dict(my_file):
    '''Returns a dictionary where the key is the month and the value is total
    crime occurences for that month'''
    crime_count = {}
    for row in my_file:
        split_date = row[1].split('/')
        month = split_date[0].replace('0', '')
        month = int(month)
        if month in crime_count:
            crime_count[month] += 1
        else:
            crime_count[month] = 1
    return crime_count
    
def create_offense_dict(my_file):
    '''Returns a dictionary where the key is offense and the value is the
    number of occurences for that offense'''
    offense = {}
    for row in my_file:
        if row[7] in offense:
            offense[row[7]] += 1
        else:
            offense[row[7]] = 1
    return offense
    
def create_offense_by_zip(my_file):
    '''Returns a dictionary where the key is the offense and the value is
    a sub dictionary where the key is the zipcode and the value is the
    number of occruences for that offense'''
    crime_zip = {}
    for row in my_file:
        zipcode = {}
        if row[7] not in crime_zip:
            for row2 in my_file:
                if row2[7] == row[7]:
                    if row2[13] in zipcode:
                        zipcode[row2[13]] += 1
                    else:
                        zipcode[row2[13]] = 1
                    crime_zip[row[7]] = zipcode
    return crime_zip

def get_max_month(my_file):
    '''Returns the month with the most crimes and the total number of crimes
    for that month'''
    max_crimes = max(create_reported_month_dict(my_file).values())
    for k, v in create_reported_month_dict(my_file).items():
        if v == max_crimes:
            max_month = k
    return max_month, max_crimes

def get_max_offense(my_file):
    '''Returns the offense with the most occurences and the total number of
    occurences for that offenseh'''
    max_offenses = max(create_offense_dict(my_file).values())
    for k, v in create_offense_dict(my_file).items():
        if v == max_offenses:
            type_offense = k
    return type_offense, max_offenses

def get_offense(my_file):
    '''Checks if input for offense is valid'''
    validoffense = True
    while validoffense:
        global input_offense
        input_offense = input('Enter an offense ==> ').title()
        offense_key = create_offense_by_zip(my_file)
        if input_offense in offense_key.keys():
            validoffense = False
        else: 
            print('Not a valid offense found, please try again.')

if __name__ == "__main__":

        validfile = True
        while validfile:
            try:
                input_file = input('Enter the name of the crime data file ==> ')
                file_list = read_in_file(input_file)
                validfile = False
            except FileNotFoundError:
                print('Could not found the file specified. {} not found.' .format(input_file))

        max_month, max_crimes = get_max_month(file_list[:])
        month = month_from_number(max_month)        
        print('\nThe month with the highest # of crimes is {} with {} offenses.'.format(month, max_crimes))

        type_offense, max_offenses = get_max_offense(file_list[:])
        print('The offense with the highest # of crimes is {} with {} offenses.\n'.format(type_offense, max_offenses))

        offense_zip = create_offense_by_zip(file_list[:])
        get_offense(file_list[:])

        print('\n{} offenses be Zip Code'.format(input_offense))
        print('{:20}{:10}'.format('Zip Code', '# Offenses'))
        print('=' * 30)

        for k, v in offense_zip[input_offense].items():
            print('{:<20}{:>10}'.format(k, v))
