# Ana 1.

class bankAccount():
    
    def __init__(self, ownerName, balance):
        self.ownerName = ownerName
        self.balance = balance
    
    def bankAccountDetails(self):
        print("Account Holder :", self.ownerName)
        print("Available Balance :", self.balance)
    
    def deposit(self):
        depositMoney = int(input("Enter amount to be deposited : "))
        self.balance += depositMoney
        print("Available Net Balance :", self.balance)
    
    def withdraw(self):
        withdrawMoney = int(input("Enter amount to be Withdrawn : "))
        if self.balance >= withdrawMoney:
            self.balance -= withdrawMoney
            print("Withdrawn Money :", withdrawMoney)
            print("Avalable Balance :", self.balance)
            print("Transaction Successful !!!")
        else :
            print("Insufficient Balance")
    
    def bankingServices(self):
        transaction = "n"
        cashDeposit = "n"
        cashWithdraw = "n"
        transaction = input("Start the transaction [Y/N] - ")
        while transaction.lower() == "y":
            while cashDeposit.lower() != "y":
                details.deposit()
                cashDeposit = input("End the transaction [Y/N] - ")
            while cashWithdraw.lower() != "y":
                details.withdraw()
                cashWithdraw = input("End the transaction [Y/N] - ")
                print("Thankyou for using our banking services")

details = bankAccount("Abhi",5000)
details.bankAccountDetails()

details.deposit()
details.withdraw()

details.bankingServices()

# Ans 2.

import math

class cone(parameters):
    
    def __init__(self, radius, height):
        parameters.__init__(self, "Cone")
        self.radius = radius
        self.height = height
    
    def volume(self):
        print("Volume of cone :", math.pi * (self.radius * self.radius) * self.height // 3)
    
    def surfaceArea(self):
        print("Surface Area of Cone :", math.pi * self.radius * math.sqrt(self.radius * self.radius + self.height * self.height))

abc = cone(5,10)

abc.volume()
abc.surfaceArea()