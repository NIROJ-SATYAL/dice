import random
import sys
print("***************WELCOME TO DICE GAME****************:")
print("To play this game you 1st you need some information about this game")
a=input("press w to continue")
if(a=="w"):
    print("In this article we will create a classic rolling  ")
    print("dice simulator with the help of basic Python knowledge.")
    print(" Here we will be using the random module since we randomize ")
    print("the dice simulator for random outputs.")
    print("\n *****now you can easily play this game:****")
    
else:
    print("sorry!you cannot play this game...try again")
    sys.exit()

x="y"
while x=="y":
    number=random.randint(1,7)
    if number==1:
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    if number==2:
        print("---------")
        print("|   O   |")
        print("|       |")
        print("|   O   |")
        print("---------")
    if number==3:
        print("---------")
        print("|   O   |")
        print("|   O   |")
        print("|   O   |")
        print("---------")
    if number==4:
        print("---------")
        print("|   OO   |")
        print("|        |")
        print("|   OO   |")
        print("---------")
    if number==5:
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    if number==6:
        print("---------")
        print("|   OO  |")
        print("|   OO  |")
        print("|   OO  |")
        print("---------")
    x=input("enter y to roll the dice")

else:
    print("you cannot play this game")
