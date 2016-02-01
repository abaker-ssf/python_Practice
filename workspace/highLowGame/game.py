import random

quit = 1

print("Hi! This is Alexander Baker's Guessing Game! Here are some instructrions: \n")
print("I am going to choice a number from 1 to 100. And your going to guess the number. \nDon't worry I'll keep track of your guesses and give you a hint if the number is \nhigher or lower from your guess.")

def Higher_or_Lower(target, guess, numGuess):
    if target < guess:
        print("You guessed lower than the number i chose.")
    elif target > guess:
        print("You guessed higher than the number i chose.")
    
    numGuess += 1
    return numGuess

while quit == 1:
    
    #prepping the game to run multiple times
    targetNum = random.randrange(1,100)
    numOfGuess = 1
    print("\nAlright i have chosen a number!")
    
    #i need to write a while loop or function here to handle continously repeating need for guesses and response hints
    while True: 
        guess = input("guess a number: ")
        
        if targetNum == guess:
            print("congragulations!!! you guess the number!. I chose %d" % guess)
            print("It took you %d guesses!" % numOfGuess)
            break 
    
        else:
            #this is where the continuly repeating guesses and hints are written
            numOfGuess = Higher_or_Lower(targetNum, guess, numOfGuess)

    quit = input("\nCongrats again :) would you like to play again? (Enter 1 to play again or 0 to stop playing): ")
    
    if quit == 0:
        print("Alright see you later :)!")
    elif quit == 1:
        print("YES! YOUR PLAYING AGAIN! ALRIGHT LET ME THINK OF A NUMBER!!!!")
    else:
        print("OPPS you didnt enter 1 or 0. I don't know what to do.\nI am only a computer program not a smarty pants human ;) :P")
        quit = input("\nWould you like to leave or stay (enter 1 or 0): ")