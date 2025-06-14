# n = int(input("If you start game so press 0::  "))
# while n==0:
while True:

    import random

    """

    1 for snake
    -1 for water 
    0 for gun 

    """

    computer = random.choice([1,-1,0])
    youstr = input("Enter your choice: ")
    yourdict = {"s": 1 ,"w":-1 , "g" : 0}
    reversedict = { 1 : "Snake" , -1 : "Water " , 0 : "Gun"}
    you = yourdict[youstr]

    print(f"Your chose is {reversedict[you]} \ncomputer chose is {reversedict[computer]}")

    if(computer == you):
        print("Its a draw")

    else:

        if(computer == -1 and you == 1):
            print("You win")

        elif(computer == -1 and you == 0):
            print("You lose")

        elif(computer == 1 and you == -1):
            print("You lose")

        elif(computer == 1 and you == 0):
            print("You win")

        elif(computer == 0 and you == -1):
            print("You win")

        elif(computer == 0 and you == 1):
            print("You lose")

        else:
            print("Somthing went Wronge!")

    print("This Game is formed by \"Engr. Muhammad Javed\"")

    # n = int(input("If you start game so press 0::  "))