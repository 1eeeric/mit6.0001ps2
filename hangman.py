# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    errorcount = 0
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if (char in letters_guessed) == False:
            errorcount += 1
            break            
    if errorcount == 0:
        return True
    else:
        return False
    
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    output = ''
    for char in secret_word: 
        if char in letters_guessed:
            output += char
        else:
            output += '_ '
    output = str(output)
    return output

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
# Take note that -= does not work on string variables in Python! 
    available_letters = ''
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available_letters += char
        else:
            pass #this is a beginner friendly format but this is not necessary. This is non-pythonic
    available_letters = str(available_letters)
    return available_letters

secret_word_test = 'congratulations' ##TO REMOVE##

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guess_count = 6
    warnings_count = 3
    my_letters = []
    #
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+ str(len(secret_word_test)) +' letter(s) long.')

    for i in range(100):
        print('-'*50)
        #Initial printing of warning and guess count:
        if i == 0:
                    print('You have ' + str(warnings_count) + ' warning(s) left.')
                    print('You have '+str(guess_count)+' guess(es) left.')
                    print('Available characters: ' + get_available_letters(my_letters))
        #
        #Input the guess here
        myinput1 = str(input('Please guess a letter: '))
        #
        #This portion processes warnings
        if myinput1 in my_letters and warnings_count > 0:
            warnings_count -= 1
            print('Oops! You have already guessed that letter! You have ' + str(warnings_count) + ' warnings left.')
            get_guessed_word(secret_word_test, my_letters)
        elif myinput1 in my_letters and warnings_count == 0:
            guess_count -= 1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess")
            get_guessed_word(secret_word_test, my_letters)
        #
        #This portion processes valid guesses
        if myinput1 not in my_letters and myinput1 in secret_word_test and guess_count > 0:
            my_letters.append(myinput1)
            mytempstr1 = get_guessed_word(secret_word_test, my_letters)
            print('Good guess: ' + mytempstr1)
        elif myinput1 not in my_letters and myinput1 not in secret_word_test and guess_count > 0:
            my_letters.append(myinput1)
            mytempstr1 = get_guessed_word(secret_word_test, my_letters)
            print('Oops! That letter is not in my word: ' + mytempstr1)
            guess_count -= 1
#            
#End game conditions whichj break the for loop
        if is_word_guessed(secret_word_test, my_letters) == True:
            print('Congratulations, you won!')
            #print('Your total score for this game is: ')
            break
        if guess_count == 0:
            print('Sorry you ran out of guesses. The word was ' + secret_word_test + '.')
            break
        print('You have ' + str(warnings_count) + ' warning(s) left.')
        print('You have '+str(guess_count)+' guess(es) left.')
        print('Available characters: ' + get_available_letters(my_letters))


    
'''
- Number of iterations in for loop to be troubleshooted. Now it is at a fixed number
<> Multiple guesses consumed on resuming valid guess after a series of bad guesses
- Additional error checks (isalpha checks and ensuring only the first input is taken. Consider LEFT(1) for hard handed approach?
- Score calculation
- Random generation of words
- Convert secret_word_test to actual non test variable


'''





































# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)