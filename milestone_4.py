import random
#from word_generet import word_creat
import string
import json
from urllib.request import Request, urlopen


class Hangman:
    def __init__(self):
        self.words = []
        self.num_letters = 0
        self.num_lives = 5
        self.list_of_guess = []
        self.word_list=[]
        self.letter_guess=[]
        #self.use_letter = str

    def check_guess(self):
        url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode('utf-8')
        first500 = webpage.split("\n")[:500]
        f = random.sample(first500, 10)
        palabra= random.choices(f)
        while '-' in palabra or ''in palabra:
            palabra =random.choices(f)
        return palabra
         
    #print(f)

    def ask_for_input(self):
        self.words = self.check_guess()
        self.letter_guess = set(self.words)
        self.word_list=set(string.ascii_lowercase)
        self.list_of_guess =set()
        self.num_letters=len(self.letter_guess)



        while self.num_letters>0 and self.num_lives>0:
            print( 'You used this letters:',''.join(self.list_of_guess))
            lista_de_palabras=[leter if leter in self.list_of_guess else '-'for leter in self.words] 
            print('\n The Curren Word :', ''.join (lista_de_palabras))
            use__letter = input ('Guess one letter:').lower()
            if use__letter in self.word_list-self.list_of_guess:
                self.list_of_guess.add(use__letter)

                if use__letter in self.letter_guess:
                    self.letter_guess.remove(use__letter)
                    self.num_letters=self.num_letters -1

                    print('')

                elif use__letter in  self.list_of_guess:
                    self.num_lives=self.num_lives-1

                    print ('n\ You already tried that letter!')

            else:
                print('n\ Invalid letter. Please, enter a single alphabetical character')
        if self.num_lives==0:
            print('n\You fineshed your chances. The word is',self.words)
        else :
            print( 'You gess the letter!!!!. The word is',self.words)
    
play_game=Hangman()
play_game.check_guess()
play_game.ask_for_input()
