# Hangman
The game is played by guessing letters to complete a hidden word. The player has a limited number of guesses before the game is over(6 attempted). The hidden word is displayed as a series of dashes representing each letter in the word. As the player guesses correct letters, the corresponding dashes are replaced with the correct letters.
Usage


Example:

Word: _ _ _ _ _ _ _ _    Guesses left: 6

Player guesses "e"

Word: _ _ _ _ _ _ _ _    Guesses left: 5

Player guesses "a"

Word: _ _ _ A _ _ _ _    Guesses left: 5

Player guesses "i"

Word: _ _ _ A _ _ I _    Guesses left: 5

Player guesses "r"

Word: _ _ R A _ _ I _    Guesses left: 5

Player guesses "t"

Word: _ _ R A _ _ I _    Guesses left: 4

Player guesses "s"

Word: _ _ R A S _ I _    Guesses left: 4

Player guesses "p"

Word: _ _ R A S _ I _    Guesses left: 3

Player guesses "l"

Word: _ _ R A S _ I _    Guesses left: 2

Player guesses "c"

Word: _ C R A S _ I _    Guesses left: 2

Player guesses "n"

Word: _ C R A S N I _    Guesses left: 2

Player guesses "o"

Word: _ C R A S N I _    Guesses left: 1

Player guesses "u"

Word: _ C R A S N I _    Guesses left: 0
You lose! The word was RUBY.

## Technologies
Payton 3.12

### Requirimentes
Payton 3.12

#### Launch 
  
The game logic is separated into three file metodos. This file defines functions for initializing the attributes, Inputing guess wordes and presenting list of letter guessed an the game state

Here is a brief overview of the functions defined in hangman.js:

    def __init__() : initializing the atriubites
    
    def asc_for_input(): Inputing guess wordes
       
    def play_game():presenting list of letters guessed and the game state
    
  
  code sample
  
```
	while self.num_letters>0 and self.num_lives>0:
            print( 'You used this letters:',''.join(self.list_of_guess))
            lista_de_palabras=[leter if leter in self.list_of_guess else '-'for leter in self.word] 
            print('\n The Curren Word :', ''.join (lista_de_palabras))
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
```


##### Instalation

gh repo clone Dereje2525/Dereje2525

