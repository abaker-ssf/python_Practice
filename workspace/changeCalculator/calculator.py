
print("Welcome to Alex Baker's first python program. This is a Change Calculator. \n")

#variables are located here 
coins = {'pennies': 0.01, 'nickels': 0.05, 'dimes': 0.1, 'quarters': 0.25}
numberOfCoins = {'pennies': 0, 'nickels': 0, 'dimes': 0, 'quarters': 0}
quit = 0

def calculatingChange(change, coinVal, coin):
    incrementor = 0
    while change >= coinVal:
        incrementor += 1
        change = change - coin
    output = (change, incrementor)
    return output

#main body of program
while quit == 0:
    price = input ("What is the price of the item: ")
    cashGiven = input("How much cash did the customer give you: ")

    change = cashGiven - price
    report = change
    
    if change < 0:
        print("Opps the customer didnt give you enough cash to pay for the item. Ask for more money")
        change = input("\nHow much money has the customer given you?: ")
  
    elif change == 0:
        print("No Change. And Dont forget to tell the customer to have a nice day :) !!!!")
   
    else:
        if change >= 0.25:
            reciever = calculatingChange(change, coins['quarters'], coins['quarters'])
            change = reciever[0]
            numberOfCoins['quarters'] = reciever[1]
        
        if change >= 0.1:
            reciever = calculatingChange(change, coins['dimes'], coins['dimes'])
            change = reciever[0]
            numberOfCoins['dimes'] = reciever[1]
        
        if change >= 0.05:
            reciever = calculatingChange(change, coins['nickels'], coins['nickels'])
            change = reciever[0]
            numberOfCoins['nickels'] = reciever[1]
           
        if change >= 0:
            reciever = calculatingChange(change, 0, coins['pennies'])
            change = reciever[0]
            numberOfCoins['pennies'] = reciever[1]
    
        #output form:
        
        print("\nSummary of calculations:")
        print("Total Change Due: %s" % report)
        print("%d Quarters" % numberOfCoins['quarters'])
        print("%d Dimes" % numberOfCoins['dimes'])
        print("%d Nickels" % numberOfCoins['nickels'])
        print("%d Pennies" % numberOfCoins['pennies'])
        
        numberOfCoins = {'pennies': 0, 'nickels': 0, 'dimes': 0, 'quarters': 0}
        quit = input("\nWould you like to exit the program? Enter 1 for yes or 0 for no: \n")
