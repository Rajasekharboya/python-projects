print("*"*10,"CAR GAME","*",10)
print("1.Start")
print("2.Stop")
print("3.Exit")
state="stop"
while True:
    ch=int(input("choose one option:"))
    if ch==1:
        if state=="stop":
            print("car is strated")
            state="start"
        else:
            print("car is already started")
    elif ch==2:
        if state=="start":
            print("car is stop")
            state="stop"
        else:
            print("car is already stopped")
    elif ch==3:
        print("thanks for choosing")
        break
    else:
        print("invalid option please choose correct option")
