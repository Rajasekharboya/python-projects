#Guess_Number_Game:
#You have Guessing 3 chances.
#if you guessing correctly uou won the game.
#if you 3 chances gueesing wrong .
#After completed 3 chances if still interested to continue the game say (Yes).
#"otherwise say (NO) then to stop the game.
print("*"*10,"Guess_Number_Game","*"*10)
import random
while True:
    i=1
    fix=random.randint(1,9)
    while i<=3:
        guess=int(input("Guess Number:"))
        if fix ==guess:
            print("you won the game:")
            break
        else:
            print("wrong Guess")
        i=i+1
    else:
        print("you lost the game")
    ch=input("Do you want to play again(yes/no):").lower()
    if ch=="no":
        break
print("Game over")
        

    
