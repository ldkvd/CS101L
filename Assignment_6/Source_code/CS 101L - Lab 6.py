########################################################################
##
## CS 101 Lab
## Lab 6
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM : Create a program that encodes and decodes a cipher. 
##
## ALGORITHM : 
##      1. Start
##      2. Prints the main menu and choices.
##      3. Ask user to input their choice.
##      4. Ask user to enter the message they would like to encode/decode.
##      5. Ask user to enter the number to shifts the letter.
##      6. Run the chopic (function) that the user inputed.
##      7. Print the encryted or decryted message.
##      8. Print the main menu and choices.
##          a. if user inputs quit, then continue to step 9.
##          b. if user inputs encode or decode, repeat steps 4-7
##      9. Stop
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string 

def Encrypt(string_text, int_key): 
    '''Caesar-encrypts string using specified key.'''
    
    encrypted_message = ''
    for character in string_text:
        if character.isalpha():
            chipher = ord(character) + int_key
            if chipher > ord('Z'):
                chipher -=26
            final = chr(chipher)
            encrypted_message += final
        else:
            encrypted_message += character
    return encrypted_message

def Decrypt(string_text, int_key): 
    ''' Decrypts Caesar-encrypted string with specified key. '''

    decrypted_message = ''
    for character in string_text:
        if character.isalpha():
            chipher = ord(character) - int_key
            if chipher > ord('Z'):
                chipher -=26
            final = chr(chipher)
            decrypted_message += final
        else:
            decrypted_message += character
    return decrypted_message   
    
 
def Get_input(): 
    '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
    selection = input('Enter your selection ==> ')
    return selection

def Print_menu():
    '''Prints menu. No user interaction. '''
    return 'MAIN MENU: \n1) Encode a string \n2) Decode a string \n3) Quit'

def main(): 
    Again = True 
    while Again:
        print(Print_menu())
        Choice = Get_input() 
        if Choice == '1': 
          Plaintext = input("\nEnter (brief) text to encrypt: ").upper() 
          Key = int(input("Enter the number to shift letters by: "))
          Ciphertext = Encrypt(Plaintext, Key)
          print("Encrypted:", Ciphertext)
          print()
          
        elif Choice == '2': 
          Ciphertext = input("\nEnter (brief) text to decrypt: ").upper() 
          Key = int(input("Enter the number to shift letters by: "))
          Plaintext = Decrypt(Ciphertext, Key)
          print("Decrypted:", Plaintext)
          print()

        else: 
          print("Have an ordinary day.") 
          Again = False 
    
# our entire program:
main()