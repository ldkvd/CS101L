########################################################################
##
## CS 101 Lab
## Lab 4
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM : Stimulate a slot machine.
##
## ALGORITHM : 
##      1. Start
##      2. Ask user how many chips they want to start off with.
##      3. Check if user input is in between 1 - 100.
##              a. If user input is invalid, the program will keep looping until a legal value is enter.
##              b. If user input is invalid, print the respected message. 
##      4. Ask user how many chips they want to wager.
##              a. If user input is invalid, the program will keep looping until a legal value is enter.
##              b. If user input is invalid, print the respected message. 
##      5. Generate random reel 1, reel 2, and reel 3.
##      6. Ouput the total number of matches.
##      7. Output the payout based on the number of matches and the wager.
##              a. If 3 matches, the payout is 10 times the wager.
##              b. If 2 matches, the payout is 3 times the wager.
##              c. If 0 matches, the payout is the negative of the wager.
##      8. Output the amount of money remaining.
##      9. Repeat Steps 4 - 8 until their is no money left to wager.
##      10. Ask user if they want to play again.
##              a. If "YES" or "Y", then loop again.
##              b. If "NO" or "N", then, go on to the step 11.
##      11. Stop
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        play_again = input('Do you want to play again? ').upper()
        if play_again == 'N' or play_again == 'NO': 
            return False                 
        if play_again == 'Y' or play_again == 'YES':
            return True
        print('You must enter Y/YES/N/NO to continue. Please try agian.')
    
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    amt_chips = int(input('How many chips do you want to wager? '))
    if (amt_chips <= 0):    # if user input is less than 1
        print('The wager amount must be greater than 0. Please enter again.')
        return get_wager(bank)
    elif (amt_chips > bank):    # if user input is greater than what they have
        print('The wager ammount cannot be greater than how much you have. {}'.format(bank))
        return get_wager(bank)
        
    return amt_chips

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reel1 = random.randint(1, 10)   # generates random reel 1
    reel2 = random.randint(1, 10)   # generates random reel 2
    reel3 = random.randint(1, 10)   # generates random reel 3

    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb == reelc):   # if 3 matches
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):  # if 2 matches
        return 2
    else:   # if 0 matches
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    amt_chips = int(input('How many chips do you want to start with? '))
    if (amt_chips > 100):   # if user input greater than 100
        print('Too high a value, you can only choose 1 - 100 chips.')
        return get_bank()
    elif (amt_chips <= 0):  # if user input less than 1
        print('Too low a value, you can only choose 1 - 100 chips.')
        return get_bank()
    return amt_chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10 - wager
    elif matches == 2:
        return wager * 2 - wager
        
    return wager * -1     

if __name__ == "__main__":

    playing = True
    while playing:
        
        bank = get_bank()
        amt_chips1 = bank
        most_amt = bank
        i = 0   # to count the number of spins it takes to lose all their money

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            i += 1

            if most_amt < bank:
                most_amt = bank
            if bank < 1:
                break
            
        print("You lost all", amt_chips1, "in", i, "spins")
        print("The most chips you had was", most_amt)
        playing = play_again()
