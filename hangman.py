import random
import time

wordlist = open("wordlist.txt")
# imports a list of possible words from a .txt located in the /res/ directory.
wordlist = wordlist.readlines()
alphaChars = "abcdefghijklmnopqrstuvwxyz"
dash = "-"
# used later for determining the validity of a character entered and also whether or not a dash
# in the word exists. Will see full use later.

word = ""
lettersRemaining = None
guessRemaining = None
lettersCorrectGuess = []
lettersIncorGuess = []
dashCheck = None
# initialized variables for the program. lettersRemaining and guessRemaining are assigned to null
# while the list of correct and incorrect guesses are initialized as empty (as there are no guesses
# yet). 

def initvars():
    # function that declares initial variables such as the random word, guesses, and sets
    # the arrays to a default state, allowing for a clean reset for each game of hangman.
    global word, lettersRemaining, guessRemaining, lettersCorrectGuess, lettersIncorGuess, dashCheck
    word = wordlist[random.randint(0,len(wordlist))][:-1]
    # word = wordlist[159][:-1]
    # debug test word as it contains all variables that could be caught

    lettersRemaining = len(word)
    guessRemaining = 6
    dashCheck = False
    lettersCorrectGuess = []
    lettersIncorGuess = []

    print("Welcome to hangman!")
    time.sleep(1)
    print("A word has been selected for you to decipher.")
    time.sleep(1)
    print("The word has " + str(lettersRemaining) + " letters.")
    time.sleep(1)
    # print(word)
    # used for debugging purposes

initvars()
while True:
    if guessRemaining == 0 or lettersRemaining == 0:
        # checks important conditions before allowing player to guess a letter
        if guessRemaining == 0:
            # if they lose
            print("The dude died. Better luck next time.")
            print("The word was: " + word + ".")
        elif lettersRemaining == 0:
            # if the user wins
            print("Congratulations! You guessed the word, which was: " + word + ".")
            time.sleep(1)
        
        if input("Do you want to play again? Type 'yes' or 'no'.").lower() == "yes":
            # if they want to play again, it reinitializes the variables to their default states
            # and selects a new word.
            print("Great! Then let's restart!")
            time.sleep(1)
            initvars()
        else:
            # if they say no or dont care enough to say yes :(
            print("We're sad to see you go. Thanks for playing!")
            break

    for letter in word:
        if letter in lettersCorrectGuess:
            print(letter + " ", end = "")
            # replaces a blank underscore with a letter
        elif letter in dash:
            print("- ", end = "")
            # checks to see if there are any dashes in the words, and replaces them accordingly
            if dashCheck == False:
                lettersRemaining -= 1
                dashCheck = True
            # ensures that a dash isn't counted as a part of lettersRemaining. In prior testing, 
            # the dash counted as a letter but couldn't be guessed due to the establishment of the 
            # alphaChars classifier. Employing dashCheck here ensures that the lettersRemaining 
            # goes down by 1, but doesn't loop, which is why dashCheck changes from "false" to 
            # "true" after checking 1 condition.
        else:
            print("_ ", end = "")
            # creates blanks for the word, which are then replaced by the correct letter should it 
            # be guessed.

    if guessRemaining > 1:
        print("You have " + str(guessRemaining) + " guesses left.")
    else:
        print("You have " + str(guessRemaining) + " guess left.")
        # both prints inform the user as to how many guesses they have left, changing from
        # plural to singular once they reach only one guess.
    time.sleep(1)
    if len(lettersIncorGuess) > 0:
        # if there is more than one unguessed letter remaining in the word
        print("You have already tried the letter(s): " + (", ".join(lettersIncorGuess)) + ".")
        time.sleep(1)
        # notifies the user of their already tried letters

    letterAsk = input("Enter a letter: ").lower()
    if not (len(letterAsk) == 1) or not (letterAsk in alphaChars):
        # exception catch that checks whether the character typed has either 0 chars or 2 or
        # more chars, as well as if the character is in the list defined by "alphacars", meaning
        # only valid alphabetic letters can be used to guess a word
        print("That's not a valid guess!")
    elif letterAsk in lettersCorrectGuess or letterAsk in lettersIncorGuess:
        # ensures that a person doesn't guess a letter multiple times.
        print("Hey buddy. You already guessed that letter.")
    elif letterAsk in word:
        print("Nice guess!")
        time.sleep(1)
        if word.count(letterAsk) > 1:
            print("There are " + str(word.count(letterAsk)) + " " + letterAsk + "'s in the word.")
        else:
            print("There is " + str(word.count(letterAsk)) + " " + letterAsk + " in the word.")
        lettersCorrectGuess.append(letterAsk)
        lettersRemaining -= word.count(letterAsk)
        time.sleep(2)
    else:
        # if they don't guess the correct word
        print("Sorry, that's not a correct guess.")
        guessRemaining -= 1
        lettersIncorGuess.append(letterAsk)
        # adds the incorrect letter guessed to a list to display later (precents user from
        # guessing the same letter again.)
        time.sleep(1)