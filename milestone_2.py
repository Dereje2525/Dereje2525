import random
def list_website_links():
    website_list = ["2019","2020"]
    link  = "http://link="
    newlinks = []
    for element in website_list:
     newlinks.append(link)
    return  random.choice (newlinks)

def choice_link ():
    link_choice = input('Enter your link choice')
    if len(link_choice)==1:
       print('Good gess')
    else:
        print('Not valid input')
choice_link()



    
    