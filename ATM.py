class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))



Card_number = input("Insert your Card Number:- ")
pin_number  = input("Enter your Pin Number:- ")

new_user =  Atm(Card_number ,pin_number)
print("Choose your activity ")
print("1.Balance Enquriy   2.withdrawl")
activity = int(input("Enter Activity Number :- "))

