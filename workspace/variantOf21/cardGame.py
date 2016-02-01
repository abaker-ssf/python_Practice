import math, random

print("Welcome to Alex Baker's variation of Blackjack")

#all of the variables are here
quit = 0

resetting = [{'name': "Ace", 'value': 1, 'numberLeft': 4}, {'name': "Two", 'value': 2, 'numberLeft': 4}, {'name': "Three", 'value': 3, 'numberLeft': 4},
         {'name': "Four", 'value': 4, 'numberLeft': 4}, {'name': "Five", 'value': 5, 'numberLeft': 4}, {'name': "Six", 'value': 6, 'numberLeft': 4},
         {'name': "Seven", 'value': 7, 'numberLeft': 4}, {'name': "Eight", 'value': 8, 'numberLeft': 4}, {'name': "Nine", 'value': 9, 'numberLeft': 4}, 
         {'name': "Ten", 'value': 10, 'numberLeft': 4}, {'name': "Jack", 'value': 10, 'numberLeft': 4}, {'name': "Queen", 'value': 10, 'numberLeft': 4},
         {'name': "King", 'value': 10, 'numberLeft': 4}]

#this section contains all of the functions

def readFile(fileName, mode):
    file = open(fileName, mode)
    return file.read()

#here starts the main program
while quit == 0:
    # variables important for the game to function
    cards = resetting
    gameScore = 100
    round = 1
    
    print("\nWould you like to start playing? Or would you like to look at the rules?\n")
    decisions = input("For instructions enter 1. To start playing Enter 0: ")
    
    if decisions == 1:
        intro = readFile('instructions','r')
        print intro
        
    else:
        print("\nLets start playing! Let round 1 begin!")
        # this section is the beginning of the game running itself 
        while round <= 5:
            
            #this section of the code needs to be thought through again because i am not sure it's optimal
            #Something feels off about the logic structure
            
            roundScore = 0 
            hand = []
            handValue = {'value':0, 'distance':0}
            
            print("\nRound {}").format(round)
            #drawing of the intial hand in the round
            for card in range(0,2):
                hand.append(random.randrange(0,12))
                handValue['value'] = handValue['value'] + hand[card]['value']
            
            handValue['distance'] = 21 - handValue['value']
            print("\nYou have a {0} and {1}").format(hand[0]['name'], hand[1]['name'])
            print("\nThe value of your hand is {0} and it's distance from 21 is {1}\n").format(handValue['value'], handValue['distance'])
            
            drawOrNot = input("\n Would you like to draw another card? If so enter 1 if not enter 0")
            
            if drawOrNot == 1:
                hand.append()
            
            