""" Hangman
Instructions

    The computer choose a random word and mark stars for each letter of each word.
    Then the player will guess a letter.
        If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
        If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
        The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
        The player can’t guess the same letter twice.

 """
import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

### YOUR CODE STARTS FROM HERE ###

""" HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#%%
'o' in 'lololo'
"lololo".index('o')

#%%

def turn():
    print("_"*len(word))
    letter_guess = input('Enter a letter: ')
    if letter_guess in word:

        return f"{board[:index]}{replacement}{board[index+1:]}"        
        print()

def play():
    print("*** HANGMAN ***")
     """