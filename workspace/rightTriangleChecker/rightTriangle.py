import math

print("This is Alexander Baker's Right Triangle solver program:")
print("\nThis program works pretty straight forward.\nYou enter the three sides and i'll tell wether its a right triangle or not!\n(dont worry i'll show my work)")
print("I am using Pythagorean theorem. A^2 + B^2 = C^2")
quit = 0

#this section contains the two functions that determine whether the information inputed create a right triangle
def hypotenuse(sideOne, sideTwo, sideThree):
    side = {'A': 0,'B': 0,'C': 0, 'equal': 0}
    
    if sideOne > sideTwo & sideOne > sideThree:
        side['C'] = sideOne**2
        side['B'] = sideTwo**2
        side['A'] = sideThree**2
        
    elif sideTwo > sideThree & sideTwo > sideOne:
        side['C'] = sideTwo**2
        side['B'] = sideOne**2
        side['A'] = sideThree**2
        
    elif sideThree > sideTwo & sideThree > sideOne:
        side['C'] = sideThree**2
        side['B'] = sideOne**2
        side['A'] = sideTwo**2
        
    else:
        oneANDtwo = sideOne**2 + sideTwo**2
        print("All of the sides are equal. Therefore this cannot be a right triangle")
        print("{} + {} = {}").format(sideOne, sideTwo, sideThree)
        print("{} + {} = {}").format(sideOne**2, sideTwo**2, sideThree**2)
        print("{} = {}").format(oneANDtwo, sideThree**2)
        side['equal'] = 1
        
    return side

def determineRightTriangle(a, b, c):
    AandB = a + b
    
    if AandB == c:
        print("\nYOU HAVE A RIGHT TRIANGLE HERE!!! Let me show you")
        print("{} + {} = {}").format(math.sqrt(a), math.sqrt(b), math.sqrt(c))
        print("{} + {} = {}").format(a, b, c)
        print("{} = {}").format(AandB, c)
    else:
        print("\nSorry. You don't a right triangle maybe another type though.")
        print("{} + {} = {}").format(a, b, c)
        print("You see A^2 and B^2 do not equal C^2")

#=====================================================

while quit == 0:
    
    #there is still a problem with the input i need to some how allow it to handle strings and allow it to ask the user 
    #to input the numbers again
    
    #this is where the triangle is determined within the program while loop.
    while True: 
        print("\nAlright I am read for you to enter the three sides!\nREMEMBER no letters! I only accept numbers!!!")
        
        one = int(raw_input("side one: "))
        two = int(raw_input("side two: "))
        three = int(raw_input("side three: "))
        
        if type(one) is int and type(two) is int and type(three) is int:
            break
        else:
            print("\nOPPS it appears one of the sides you gave me isn't a NUMBER!\nPlease re-enter the sides again and make sure that their all numbers.")
    
    sides = hypotenuse(one, two, three)
    
    if sides['equal'] == 0:
        determineRightTriangle(sides['A'], sides['B'], sides['C'])
    
    #this section deals with whether or not the program will repeat itself. It's designed to catch mistakes 
    # and force the user to correct them.
    quit = input("\nSo now you know if you got a right triangle or not :) would you like to exit now?\nEnter 1 to exit or 0 to reuse the program: ")
    
    if quit == 1:
        print("Alright see you later :)!")
        
    elif quit == 0:
        print("YES! I have more triangles to solve for!")
        
    else:
        while True:
            
            print("\nOPPS you didnt enter 1 or 0. I don't know what to do.\nI am only a computer program not a smarty pants human ;) :P")
            quit = input("Would you like to leave or stay (enter 1 or 0): ")
            
            if quit == 1 or quit == 0:
                break
