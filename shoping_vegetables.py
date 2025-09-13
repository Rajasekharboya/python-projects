print("x"*10,"market","*"*10)
print("apple")
print("bannana")
print("orange")
print("*"*10,"cart","*"*10)
print("1.add")
print("2.remove")
print("3.display")
print("4.exit")
print("*"*10,"fruit","*"*10)
cart=[]
while True:
    ch=int(input("choose one option:"))
    if ch==1:
        fruit=input("enter fruit name:")
        if fruit not in cart:
            cart.append(fruit)
            print("fruit is added to cart")
        else:
            print("fruit is already avalible")
    elif ch==2:
        fruit=input("enter fruit name:")
        if fruit in cart:
            cart.remove(fruit)
            print("fruit is removed from cart")
        else:
            print("fruit is not avalible")
    elif ch==3:
        print("dipslay all cart in fruits")
        for x in cart:
            print(x,end='')
        print()
    elif ch==4:
        print("thanks for choosing")
        break
    else:
        print("choose correct option:")
