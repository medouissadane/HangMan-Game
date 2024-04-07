import random
HANGMANPICS = ['''
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

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#***************make random word***********
random_word=random.choice(words)
# print (random_word)


#***************replace number letters***********

letter_palce=[]
for letter in random_word:
    letter_palce+="_"
print(" ".join(letter_palce))
# print("_ "*len(random_word))


tryes=0



while True:


    #***************ask for latter***********
    user_letter=input("\nEnter a letter: ").lower() 
    
    #***************check***********
    if user_letter in random_word:
        # for pos in range (len(random_word)):
        #     if random_word[pos]==user_letter:
        #         letter_palce[pos]=user_letter
                
        print(" ".join(letter_palce)) 
        # index_letter=random_word.index(user_letter)
        # letter_palce[index_letter]=user_letter

        
    else:
        tryes+=1
        print(HANGMANPICS[tryes-1])
        print(" ".join(letter_palce))


    if "".join(letter_palce) == random_word:
        print('''
              ************
              You win  (:
              ************
              ''')
        break


    if tryes==7:
        print('''
              ************
              You lose  ):
              ************
              ''')
        break



    

