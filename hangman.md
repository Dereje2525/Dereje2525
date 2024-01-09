# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.
## Technologies
Payton 3.12
###  Requirements
This module requires the following modules:
word_generet.py
#### Launch 
  code sample


    while len (letera_advinar)>0 and chance>0:
        print( 'You used this letters:',''.join(leteras_usadas))
        lista_de_palabras=[leter if leter in leteras_usadas else '-'for leter in advinar_palabra] 
        print('\n The Curren Word :', ''.join (lista_de_palabras))  

        usar__letra = input ('Guess one letter:').upper()
        if usar__letra in alfabet-leteras_usadas:
            leteras_usadas.add(usar__letra)
            if usar__letra in letera_advinar:
                letera_advinar.remove(usar__letra)
                print('')
                
        elif usar__letra in  leteras_usadas:
                print ('n\ you used this letter.Pleas use the new one')
                chance=chance-1
        else:
            print('n\ invalid caracter.Pleas enter a valid caracter')
    if chance==0:
        print('n\You fineshed your chances. The word is',advinar_palabra)
    else :
        print( 'Yo gess the letter!!!!')



##### Instalation

