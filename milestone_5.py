import random
import string
import json
from urllib.request import Request, urlopen
class Hangman:
    def __init__(self):
        self.num_letters = 0
        self.num_lives = 0
        self.list_of_guess = []
        self.word_list=['abcdefghijklmnopqrstuvwxyz']
        self.letter_guess=[]

    def asc_for_input(self): 
        print('Guess a letter.')
        guess = input()
        return guess

    def play_game(self,words,num_lives):
        self.word = words
        self.num_lives = 5
        self.letter_guess = set(self.word)
        self.word_list=set(string.ascii_lowercase)
        self.list_of_guess =set()
        self.num_letters=len(self.letter_guess)

        while self.num_letters>0 and self.num_lives>0:
            print( 'You used this letters:',''.join(self.list_of_guess))
            list_of_letter_guessed =[letter if letter in self.list_of_guess else '-'for letter in self.word] 
            print('\n The Curren Word :', ''.join (list_of_letter_guessed))
            use_letter = self.asc_for_input()

            if use_letter in self.word_list-self.list_of_guess:
                self.list_of_guess.add(use_letter)

                if use_letter in self.letter_guess:
                    self.num_letters=self.num_letters-1

                    print('')
                elif use_letter in  self.list_of_guess:
                    self.num_lives=self.num_lives-1

                    print ('n\ You already tried that letter!')
            else:
                print('n\ Invalid letter. Please, enter a single alphabetical character')
        if self.num_lives==0:    
            print('n\You lost. The word is',self.word)
        else:
            print('Congratulations. You won the game! The word is:', self.word)       


if __name__ == "__main__":
    game=Hangman()
    game.play_game('dereje',5)

