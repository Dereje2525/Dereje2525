   
import random
import string
import json
from word_generet import word_creat

def get_words():
    palabras = word_creat()
    palabra = random.choices(palabras)
    while '-' in palabra or ''in palabra:
        palabra =random.choices(palabras)
    return palabra


def game():
    advinar_palabra = get_words()
    letera_advinar = set(advinar_palabra)
    alfabet=set(string.ascii_lowercase)
    leteras_usadas =set()            
    chance = 6

    while len (letera_advinar)>0 and chance>0:
        print( 'You used this letters:',''.join(leteras_usadas))
        lista_de_palabras=[leter if leter in leteras_usadas else '-'for leter in advinar_palabra] 
        print('\n The Curren Word :', ''.join (lista_de_palabras))  

        usar__letra = input ('Guess one letter:').lower()
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

#if__name__== '__main__':        
game() 
    
            
        
    
    
