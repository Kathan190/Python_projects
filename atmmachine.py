import sys
import math
import random

balance = 1000
total = 0
print("Welcome to my ATM. ")
print("Instuctions")
print("1. Machine will give you unique number as a pin. ")

number = random.randint(1, 100)
print("Your number is ",number)

num = int(input("Enter your pin number: "))
if num == number:
    print("You Have successfully login. \n")
    print("1. Display the balance. ")
    print("2. Deposit the cash. ")
    print("3. Withdraw the money. \n")
    options = input("Please select the number: \n")
    if options == "1":
        print("Your Main balance is ",balance)
    elif options == "2":
        deposit = int(input("Enter the deposit amout in to the machine: "))
        total = deposit + balance
        print("\n")
        print("Your amaount is successfully deposit. ")
        print("Total balance is ",total)
else:
    print("You have entered wrong pin number. ")
    print("Please try again. ")