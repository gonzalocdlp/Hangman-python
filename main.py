import random
import art
import wordlist



def script():
    #Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    print(art.logo)
    randword= random.choice(wordlist.word_list)
    counter=len(randword)
    underscore = []
    for i in range(0, counter):
        underscore += "_"
        
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    print("welcome to Hangman")
    print(underscore)
    score=0
    t=7
    guessed="!"
    win=underscore.count('_')
    while score<7 and win!=0 :
        win=underscore.count('_')
        if t<7:
            print(art.stages[t])
        guess=input("guess a letter\n").lower()
        
        g=0
        if score==7:
            print("too many guesses you lost")
            script()
        for past in guessed:
            if guess==past:
                g=g+1
        if g>0:
            print(f"you guessed the letter {guess} already. Try another")
            print(underscore)
        else:
            guessed=guessed+guess    
            x=0
            y=""
            for letter in randword:
                x=x+1
                if letter==guess:
                    y=(x)
                    underscore[x-1] = guess
                    print(underscore)
                    win=underscore.count('_')
                    if win==0:
                        print ("you won")
            if y=="":
                    t=t-1
                    
                    print("wrong guess")
                    score=score+1
                    print(underscore)        
                    if score==7:
                        print("he's hung :(")
                        print(art.stages[t])
    end=input('type y to restart or n to end').lower()
    if end=="y":
        script()
    else:
        exit()
    
script()            
    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
