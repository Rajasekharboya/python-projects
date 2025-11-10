#print("Rolling dice game")
'''Total==12 - You won the game
Total==7 - You are having another chance
total <>12,7 -You lost the game'''
import random
while True:
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total=dice1+dice2
    print("Total:",total)
    if total==12:
        print("you won the game")
        break
    elif total==7:
        print("you are having another chance")
    else:
        print("you lost the game")
        break
