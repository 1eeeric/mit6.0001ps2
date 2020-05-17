# Problem Set 2, hangman.py
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

guess_count = 0
warnings_count = 0
my_letters = []
    
#Check 1#
def input_validity_check(user_input, warnings_count, guess_count):
    '''
    Parameters
    ----------
    user_input: letter input by player for guess
    warnings_count: number of warnings left.
    guess_count: number of guesses left
    
    Returns
    -------
    0, 1 or 2 as integers. 0 represents check passed. 1 represents warning deduction. 2 represents guess deduction. 

    '''
    if str.isalpha(user_input) == False or len(user_input) != 1:
        if warnings_count > 0:
            print('Oops! Invalid input! Please key in only ONE alphabet. You have ' + str(warnings_count) + ' warnings left.')
            return 1
        elif warnings_count <= 0: 
            print('Oops! Invalid input! Please key in only ONE alphabet. You have no warnings left so you lose one guess')
            return 2
    else:
        return 0
 
#Check 2#
def repeat_check(user_input, my_letters, secret_word, warnings_count, guess_count):
    '''
    This function is used to check for repeated guessed letters before allowing the guesses to be processed. 
    
    Parameters
    ----------
    user_input : single letter string. 
    secret_word: the answer to the Hangman game that is selected by the computer randomly
    warnings_count: the number of warnings remaining 
    guess_count: the number of guesses remaining 
   
    Returns
    -------
    0, 1 or 2. 0 is a good check. 1 is a warning deduction. 2 is a guess deduction
    '''
    temp = user_input in my_letters
    if temp == True:
        if warnings_count > 0:
            warnings_count -= 1
            temp1 = get_guessed_word(secret_word, my_letters)
            print('Oops! You have already guessed that letter! You have ' + str(warnings_count) + ' warnings left: ' + str(temp1))
            return 1
        elif warnings_count <= 0:
            guess_count -= 1
            temp1 = get_guessed_word(secret_word, my_letters)
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + str(temp1))
            return 2
    elif temp == False:
        return 0

#Check 3#
def game_code(user_input, secret_word, my_letters, guess_count):
    """
    This is the actual checking code for valid inputs. 
   
    Parameters
    ----------
    user_input : TYPE
        DESCRIPTION.
    secret_word : TYPE
        DESCRIPTION.
    my_letters : TYPE
        DESCRIPTION.
    mytempstr1 : TYPE
        DESCRIPTION.
    guess_count : TYPE
        DESCRIPTION.

    Returns
    -------
    0, 1, 2. 0 is a good guess. 1 is a bad vowel guess. 2 is a bad consonant guess. 

    """
#if str.isalpha(myinput1) == True and myinput1 not in my_letters and guess_count > 0:
    if user_input in secret_word and len(user_input) == 1:
        my_letters.append(user_input)
        mytempstr1 = get_guessed_word(secret_word, my_letters)
        print('Good guess: ' + mytempstr1)
        return 0
    elif user_input in ['a','e','i','o','u'] and len(user_input) == 1:
        my_letters.append(user_input)
        mytempstr1 = get_guessed_word(secret_word, my_letters)
        print('Oops! That letter is not in my word: ' + mytempstr1)
        return 1
    elif len(user_input) == 1:
        my_letters.append(user_input)
        mytempstr1 = get_guessed_word(secret_word, my_letters)
        print('Oops! That letter is not in my word: ' + mytempstr1)
        return 2
           
  
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
    #Initialize variables
    guess_count = 6
    warnings_count = 3
    my_letters = []
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+ str(len(secret_word)) +' letter(s) long.')

    for i in range(100):
        print('-'*50)
        #Initial printing of warning and guess count:
        if i == 0:
            print('You have ' + str(warnings_count) + ' warning(s) left.')
            print('You have '+str(guess_count)+' guess(es) left.')
            print('Available characters: ' + get_available_letters(my_letters))
        
        #Input the guess here
        myinput1 = str(input('Please guess a letter: '))
        check1 = input_validity_check(myinput1, warnings_count, guess_count)

        # Validation and game code#
        if check1 == 0: 
            check2 = repeat_check(myinput1, my_letters, secret_word, warnings_count, guess_count)
            if check2 == 0:
                check3 = game_code(myinput1, secret_word, my_letters, guess_count)
                if check3 == 1:
                    guess_count -= 2
                elif check3 == 2:
                    guess_count -= 1        
            elif check2 == 1: 
                warnings_count -= 1
            elif check2 == 2: 
                guess_count -= 1
        elif check1 == 1:
            warnings_count -= 1
        elif check1 == 2:
            guess_count -= 1
   
        #End game conditions#
        if is_word_guessed(secret_word, my_letters) == True:
            score_count = guess_count * len(set(secret_word))
            print('Congratulations, you won!')
            print('Your total score for this game is: ' + str(score_count) + '.')
            break
        if guess_count <= 0:
            print('Sorry you ran out of guesses. The word was ' + secret_word + '.')
            break
        print('You have ' + str(warnings_count) + ' warning(s) left.')
        print('You have '+str(guess_count)+' guess(es) left.')
        print('Available characters: ' + get_available_letters(my_letters))



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word, my_letters):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    secret_word: actual answer to the Hangman game
    my_letters: list of letters already guessed
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and (
                my_word[i] != other_word[i] \
                or my_word.count(my_word[i]) != other_word.count(my_word[i]) \
            ):
                return False
        return True
            
            
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
    words_list = open(WORDLIST_FILENAME, 'r').readline().split()
    possible_matches = []
    for other_word in words_list:
        if match_with_gaps(my_word, other_word, my_letters):
            possible_matches.append(other_word)
    print(' '.join(possible_matches))

#Check 1 for version with hints#
def input_validity_check_with_hints(secret_word, user_input, warnings_count, guess_count):
    '''
    Parameters
    ----------
    secret_word: actual answer to the Hangman game
    user_input: letter input by player for guess
    warnings_count: number of warnings left.
    guess_count: number of guesses left
    
    Returns
    -------
    0, 1, 2, 3 as integers. 0 represents check passed. 1 represents warning deduction. 2 represents guess deduction. 3 represents when the hint wildcard is called. 

    '''
    if user_input == "*":
        return 3
    elif (str.isalpha(user_input) == False or len(user_input) != 1):
        if warnings_count > 0:
            print('Oops! Invalid input! Please key in only ONE alphabet. You have ' + str(warnings_count) + ' warnings left.')
            return 1
        elif warnings_count <= 0: 
            print('Oops! Invalid input! Please key in only ONE alphabet. You have no warnings left so you lose one guess')
            return 2
    else:
        return 0
 

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
    
    #Initialize variables
    guess_count = 6
    warnings_count = 3
    my_letters = []
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+ str(len(secret_word)) +' letter(s) long.')

    for i in range(100):
        print('-'*50)
        #Initial printing of warning and guess count:
        if i == 0:
            print('You have ' + str(warnings_count) + ' warning(s) left.')
            print('You have '+str(guess_count)+' guess(es) left.')
            print('Available characters: ' + get_available_letters(my_letters))
        
        #Input the guess here
        myinput1 = str(input('Please guess a letter: '))
        
     
        check1 = input_validity_check_with_hints(secret_word, myinput1, warnings_count, guess_count)

        # Validation and game code#
        if check1 == 3:
            temp2 = get_guessed_word(secret_word, my_letters)
            show_possible_matches(temp2)
        elif check1 == 0: 
            check2 = repeat_check(myinput1, my_letters, secret_word, warnings_count, guess_count)
            if check2 == 0:
                check3 = game_code(myinput1, secret_word, my_letters, guess_count)
                if check3 == 1:
                    guess_count -= 2
                elif check3 == 2:
                    guess_count -= 1        
            elif check2 == 1: 
                warnings_count -= 1
            elif check2 == 2: 
                guess_count -= 1
        elif check1 == 1:
            warnings_count -= 1
        elif check1 == 2:
            guess_count -= 1

   
        #End game conditions#
        if is_word_guessed(secret_word, my_letters) == True:
            score_count = guess_count * len(set(secret_word))
            print('Congratulations, you won!')
            print('Your total score for this game is: ' + str(score_count) + '.')
            break
        if guess_count <= 0:
            print('Sorry you ran out of guesses. The word was ' + secret_word + '.')
            break
        print('You have ' + str(warnings_count) + ' warning(s) left.')
        print('You have '+str(guess_count)+' guess(es) left.')
        print('Available characters: ' + get_available_letters(my_letters))
    pass

    
'''
BUGS
- Number of iterations in for loop to be troubleshooted. Now it is at a fixed number
- Input small letter conversion
- Update docstrings
'''



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
