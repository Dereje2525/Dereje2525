import random
def word_creat(): 
    word=[]
    palabra =[]
    lista_alfabet =list ('abcdefghijklmnopqrstuvwxyz')
    for i in range(0,100):
        p=''
        for j in range(5):
            p+=lista_alfabet[random.randint(0,25)]
            palabra.append(''.join(p))
        return sorted(palabra)  
  
word_creat()