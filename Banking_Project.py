import sys
class customer:
    '''Customers class with bank operations...'''
    bankname="STATE_BANK_OF_INDIA"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Blance will be added:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("infsufficient Funds..cannot perform this operation")
            sys.exit()
        self.balance=self.balance-amount
print("welcome to",customer.bankname)
name=input("enter your name:")
c=customer(name)
while True:
    print("d-deposit\nw-withdraw \ne-exit")
    option=input("choose your option:").lower()
    if option=="d":
        amount=float(input("enter the deposite amount:"))
        c.deposit(amount)
    elif option=="w":
        while True:
            amount=float(input("enter the withdraw amount:"))
            if not(amount>0 and amount%100==0):
                print("amount multiples of 100's")
            else:
                break
            c.withdraw(amount)
    elif option=="e":
        print("thanks for Banking")
        break
    else:
        print("invalid option...choose valid option")
        
        
        
