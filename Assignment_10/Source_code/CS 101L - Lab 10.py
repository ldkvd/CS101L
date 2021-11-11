#############################################################################
##
## CS 101 Lab
## Lab 10
## Lily Dang
## ldkvd@mail.umkc.edu
##
## PROBLEM:
##      Create a program that asks user for a text file to read. Then output
##      the top ten words that are used most, the number of words that appear
##      only once, and the number of unqiue words.
##
## ALGORITHM:
##      1. Start.
##      2. Define functions and variables.
##      3. Input from user the file to open. Try and except.
##         Keep prompting until file is valid.
##      4. Read file and split contents of the file into a list.
##      5. Remove any puncutations from the words in the list.
##      6. Output the the top ten words with the most
##         frequency, the total number of words that only appear once, and
##         the total number of unqiue words.
##      7. Stop
##
## ERROR HANDLING:  
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
##############################################################################


def open_file():
    while True:
        try:
            filename = input('Enter the name of the file to open ==> ')
            open_file = open(filename)
            main_file = open_file.read()
            words = main_file.split()
            return words
        except FileNotFoundError:
            print('Could not open file', filename, '\nPlease try again\n')
        except IOError:
            print('There is an IO Error', filename)

def remove_punc(word):
    '''Returns the word with the the puncutations removed'''
    punctuations = '.?!,:;'
    for char in word:
        if char in punctuations:
            word = word.replace(char, "")
    return word

def get_word_count(list1):
    '''Counts and returns a dictionary of word (key) and the number of time
    the word appears in the file (value)'''
    word_dict = {}
    for word in list1:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def get_top_10(word_dict):
    '''Sort the dictionary and print the top ten words and number of times
    they occur in the text file.'''
    sorted_dict = {}
    sorted_key = sorted(word_dict, key=word_dict.get, reverse = True)[:10]

    for i in sorted_key:
        sorted_dict[i] = word_dict[i]

    print('\nMost frequently used words')
    print('{:>2}{:>15}{:>20}'.format('#', 'Word', 'Freq'))
    print('=' *37)

    count = 0
    for key, value in sorted_dict.items():
        count += 1
        print('{:>2}{:>15}{:>20}'.format(count, key, value))

def get_occur_once(word_dict):
    '''Returns the number of words that occur only once'''
    once = []
    for k, v in word_dict.items():
        if v == 1:
            once.append(k)
        else:
            continue
    count = len(once)
    return count

def get_unique(list1):
    '''Returns the number of words that are unqiue'''
    unique = []
    for i in list1:
        if i not in unique:
            unique.append(i)
        else:
            continue
    count = len(unique)
    return count


word_list = open_file()

clean_list = [remove_punc(x) for x in word_list]
clean_list = [x.lower() for x in clean_list]

for i in clean_list[:]:
    if len(i) <= 3:
        clean_list.remove(i)

word_count = get_word_count(clean_list)

freq_word = get_top_10(word_count)

occur_once = get_occur_once(word_count)
print('\nThere are {} words that only occur once'.format(occur_once))

unique_words = get_unique(clean_list)
print('There are {} unqiue words in the document'.format(unique_words))
