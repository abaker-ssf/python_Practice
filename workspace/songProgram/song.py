print("This is Alex Baker's lovely song program.")

bottles = 99


while True:
    
    if bottles == 1:
        print("{} bottle of beer on the wall.\n{} bottle of beer").format(bottles, bottles)
        bottles = bottles - 1
        print("Take one down pass it around.\n{} bottles of beer on the wall\n").format(bottles)
        break
        
    else:    
        print("{} bottles of beer on the wall.\n{} bottles of beer").format(bottles, bottles)
        bottles = bottles - 1
        print("Take one down pass it around\n{} bottles of beer on the wall\n").format(bottles)
    