#CS 101 Lab
#Program 3
#Lily Dang
#ldkvd@mail.umkc.edu

#Problem: Create a game that guesses the user's number, given that input the remainder when their number is divided by 3, 5, and 7. 

#Alogrithm:
    #Ask the user to input the remainder when their number is divided by 3.
    #Add a range. Remainder of 3 can only be 0, 1, 2.
    #If the user input is invalid, the program will loop until legal value is entered.
    #If the user input is valid, the program will iterate through each number from 0 - 100 and check for numbers with same remainder as the user input
        #Numbers with same reminder will be stored into a list, in this program, the three_list. 
    #If the user input is valid, then, ask the user to input the remainder when their number is divide by 5.
    #The program will check the three_list for any number with a remainder that is equal to user input and store it into another list called five_list.
    #Then, ask the user to input the remainder when their number is divided by 5.
    #The program will check the five_list for any number with a remainder that is equal to user input and store it into seven_list.
    #Print the user's number. 
    #It will ask if the user wants to play again.
        #If the answer is yes, then it will run through the whole program again until the user answers with no.
        #if the answer is no, then it will stop.

#Error Handling:
    #The reaminder of 3 can only be 0, 1, or 2. If the user enters a number of 3 or greater, "The value entered must be less than 3" will be printed.
    #If the user enters a number less than 0, "The value entered must be 0 or greater" will be printed.
    #Program will loop and ask for an input until legal value is entered.
        
print('Welcome to Flarsheim Guesser!')

play_game = True

#the whole program should be nested under one big while loop 
while play_game:          

    print('\nPlease think of a number between and including 1 and 100.')
    
    #get user input
    user3 = int(input('\nWhat is the remainder when your number is divided by 3 ? '))   

    #error handling
    while (user3 < 0) or (user3 > 2):   
        if user3 < 0:
            print('The value entered must be 0 or greater')
        elif user3 >= 3:
            print('The value entered must be less than 3')
        user3 = int(input('What is the remainder when your number is divided by 3 ? '))

    #make an empty list for numbers of remainders when divided by 3
    three_list = []

    #remainders of 3 can only be 0, 1, 2
    if (user3 == 0) or (user3 == 1) or (user3 == 2):
        for i in range(1, 101):           #for loop to iterate through each number from 0 - 100
            remain3 = i % 3               #check the remainder of each number from 0 - 100
            if (remain3 == user3):        #if the remainder is equal to user input, then it will be put into the three_list
                three_list.append(i)

    #make an empty list for numbers of remainders when divided by 5
    five_list = []

    #get user input
    user5 = int(input('\nWhat is the remainder when your number is divided by 5 ? '))

    #remainders of 5 can only be 0, 1, 2, 3, 4
    if (user5 == 0) or (user5 == 1) or (user5 == 2) or (user5 == 3) or (user5 == 4):
        for i in three_list:              #for loop to iterate through each element in the three_list
            remain5 = i % 5               #check the remainder of each number in list
            if (remain5 == user5):        #if the remainder is equal to user input, then it will be put into the five_list
                five_list.append(i)

    #make an empty list for numbers of remainders when divded by 7
    seven_list = []

    #get user input
    user7 = int(input('\nWhat is the remainder when your number is divided by 7 ? '))

    #remainders of 7 can only be 0, 1, 2, 3, 4, 5, 6
    if (user7 == 0) or (user7 == 1) or (user7 == 2) or (user7 == 3) or (user7 == 4) or (user7 == 5) or (user7 == 6):
        for i in five_list:               #for loop to iterate through each element in the five_list
            remain7 = i % 7               #check the remainder of each number in list
            if (remain7 == user7):        #if the remainder is equal to user input, then it will be put into the seven_list
                seven_list.append(i)

    print('Your number was ', seven_list[0])          #prints their number
    print('How amazing is that?')
    print()

    while True:
        restart = input('Do you want to play again? Y to continue, N to quit ').upper()          #ask user if they want to play again
        if restart == 'Y':
            break
        if restart == 'N':
            play_game = False
            break
        
