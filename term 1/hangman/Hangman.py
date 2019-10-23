#Hangman Game

#Max Virkus
#10/19

#the classic game of hangman.
#the computer picks a random word
#and the player trys to guess it,
#one letter at a time.  If the player
#can't guess the word in time, the little
#stick figure gets hanged.

import random

HANGMAN = ['''
  +---+
   |      |
          |
          |
          |
          |
=========''', '''
  +---+
   |      |
  O     |
          |
          |
          |
=========''', '''
  +---+
   |      |
  O     |
   |      |
          |
          |
=========''', '''
  +---+
   |      |
  O     |
 /|       |
          |
          |
=========''', '''
  +---+
   |      |
  O     |
  /|\     |
          |
          |
=========''', '''
  +---+
   |      |
  O     |
  /|\     |
  /       |
          |
=========''', '''
  +---+
   |      |
  O     |
  /|\     |
  / \     |
           |
=========''']

MAX_WRONG = len(HANGMAN) - 1

#Word bank of animals
WORDS = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
#initialize variables
word = random.choice(WORDS)# the word to be guessed
so_far = "-" * len(word)#one dash for each letter in word to be
wrong = 0#number of wrong guesses player has made
used = [ ]# letters already guessed

print("Welcome to Hangman.    Have Fun Loosing!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess:  ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("\n\nEnter your guess:  ")
        guess = guess.upper()

    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,",guess, "isn't in the word.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou' guessed it!")
print("\nThe word was", word)
input("\n\nPress the enter key to exit.")
input("\n\nPress X to start again.")

                  

#Things that need to be in the program.
#Think of a word(Randomized)
#How many tries required
#Ascii art(graphical output)[noose, gallose, number of letter placements]
#How many players there are[2+]
#Where the letters are going to sit
#Formatting of the guessed letters
#How many lives there are
#Ask for a guess
#Where wrong letters will go(list)
#Allows an input
#Add to the UI
#Check to see if letter guessed is in word
#Updating the Gallows per guess
#Created a guessed letters list
##Created a guessed wrong list
#Output (“--- is not in the word”)
#Create a correct letter list
#What happens if you guess the same letter
#Correct same letter guesses
#Loop until word is guessed or person is hung
#Display death or win
#Case-Sensitivity
#It puts in every letter in the word, checks to see how many letters are in it
#Handle, allow, and display spaces
#Case sensitivity(Make it all lower or capitalized)
#Don't allow special characters
#Update ascii art, or reprint(list) [if ___ goes up, increase ascii art]
#Display How many guesses are left or how high the difficulty is
#Difficulty
#Menu option
#Play again?
#Quit?
#Win (Guess word)/ Lose conditions(Man hung)
#Startup Intro
#Death scene (Mario Game Over)
#Win/Lose Conditions and alternative outcomes.(How they broke the loop)
