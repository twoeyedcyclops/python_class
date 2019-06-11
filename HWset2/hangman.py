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
    letter_is_guessed=[]   #letter_is_guessed is a vector of 1 and 0 based on whether or not each letter is guessed
    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1==char2:
                letter_is_guessed.append(1)
    if sum(letter_is_guessed)==len(secret_word):
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
    i=0
    guessed_word=[]
    for var in range (0,len(secret_word)):
        guessed_word.append('_ ')

    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                guessed_word[i]=char1
        i=i+1            

    guessed_word="".join(guessed_word)
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet=string.ascii_lowercase
    modalphabet=list(alphabet)
    for char1 in alphabet:
        for char2 in letters_guessed:
            if char1==char2:
                if char1 in modalphabet:
                    modalphabet.remove(char1)
    letters_available=''.join(modalphabet)  
    return letters_available
    
    

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
    vowels=['a','e','i','o','u']
    print(secret_word)
    print('Welcome to hangman! buckle up')
    print('I am thinking of a word that is ',len(secret_word),' letters long.')
    no_of_guess=6
    warning=3
    print('You have ',no_of_guess,' guesses to figure out the word.')
    letters_guessed=[]
    unique_letters=0
    while no_of_guess>0:
        print('letter guessed',letters_guessed)
        inword=0
        error=0
        print('You have ',no_of_guess,' guesses left.')
        print('You have ',get_available_letters(letters_guessed),' available to guess')
        user=input('Please guess a letter:')
        if user=='!':
            break
        if user.isalpha() == True:
            for char2 in letters_guessed:
                if char2 == user:
                    if warning>0:
                        warning=warning-1
                        print('Sorry you have already used that letter, you have used a warning, you have ',warning, 'remaining')
                        error=1
                    else:
                        no_of_guess=no_of_guess-1
                        print('Sorry you have already used that letter, and you have used all of your warnings, now you have',no_of_guess,'remaining')
                        error=1
            if error==0:
                letters_guessed.append(user)
                guessed_word=get_guessed_word(secret_word, letters_guessed)
                print(guessed_word)
                for char1 in secret_word:
                    if char1==user:
                        unique_letters=unique_letters+1
                        inword=1
                        print('Nice Guess')
                if inword==0:
                    if user in vowels:
                        no_of_guess=no_of_guess-2
                        print('That letter is not in this word')
                    else:
                        no_of_guess=no_of_guess-1
                        print('That letter is not in this word')
        else:
            if warning>0:
                warning=warning-1
                print('Sorry that is not a valid input, you have used a warning, you have ',warning,' remaining')
            else:
                no_of_guess=no_of_guess-1
                print('Sorry that is not a valid input, and you have used all of your warnings, now you have',no_of_guess,'remaining')
        if is_word_guessed(secret_word, letters_guessed)== True:
            print('Congradulations, you guessed the word correctly, the word was: ',secret_word)
            score=no_of_guess*unique_letters
            print('Your score is',score)
            break
        print()
    if no_of_guess==0:
        print('Sorry you ran out of guesses you are a fucking loser')

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
