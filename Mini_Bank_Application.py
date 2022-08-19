import sys
class Customer:
    ''' Customer class to describe bank operations '''
    bank_name = 'Vishwakarma Banking and finances'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.amount = amount
        if amount > 0:
            self.balance = self.balance + amount
            print('Update balance after deposit is : Rs.',self.balance)
        else :
            print('Entered amount value is less than 0 kindly enter a value greater than 0 to deposit')
    def withdraw(self,amount):
        if amount < 0:
            print('Entered amount value is less than 0 kindly enter a value greater than 0 to withdraw')
        else:
            self.balance = self.balance - amount
            print('Update balance after withdraw is : Rs,',self.balance)
print('Welcome to Vishwakarma banking and Finances')
name = input('Enter your Name : ')
c = Customer(name)
while True:
    print('Please choose an option from the below : ')
    option = input('D - Deposit \nW - Withdraw \nS-Show Balance \nE-Exit \t')
    if option.lower()=='d':
        amount = float(input('Enter the amount you want to deposit : Rs,'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount = float(input('Enter the amount you want to withdraw : Rs,'))
        c.withdraw(amount)    
    elif option.lower()=='e':
        print('Thanks for banking with us')
        sys.exit()
    else:
        print('Invalid option selected, Please Enter a valid choice!!')



    