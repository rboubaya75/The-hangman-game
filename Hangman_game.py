
from random import choice
from unidecode import unidecode

def word():
    f = open('mot.txt', 'r' )
    contenu = f.readlines()
    return unidecode(choice(contenu)).upper().replace('\n','')


def underscore(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]


def Input():
    letter = input('Please enter a letter : ')
    if letter =="" or len( letter ) > 1 or ord(letter) < 65 or ord(letter) > 122:
        return Input()

    else:
        return letter.upper()
    

#si la lettre est trouvée


def hangman(tries):
    stages = [  
        
                   """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """
    ,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """,
    """
    GAME OVER !
    """
    ]
    return stages[tries]


    
Already_used_letters = []
word_to_find =word()
display = underscore(word_to_find)

nb_errors = 0
trie=6
while '_' in display and nb_errors < 6:
    letter = Input()

    
   
    if letter not in Already_used_letters :
        Already_used_letters+=[letter]

    if letter not in word_to_find:

        nb_errors +=1
        trie -= 1
        print(hangman(nb_errors ))

    if  letter in Already_used_letters:
        print('WORD ALREADY USED,TRY AGAIN')
        
    display = underscore(word_to_find , Already_used_letters  )
    print( '\n Word to be guessed : ' , display , ' '*6 , word_to_find, 'Number of remaining tries:' , 6-nb_errors )
    
    if nb_errors==6:
        print("GAME OVER, YOU ARE HANGED !")
        break

else:
    print("GOOD JOB MAN, YOU DID IT")