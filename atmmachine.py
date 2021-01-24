import sys
import random
import math

balance = 1000
number = random.randint(1000, 2000)

def about_menu():
    print("1. Check your Balance.")
    print("2. Cash out.")
    print("3. Deposit the Cash.")
    

def menu():
    while True:
        number = random.randint(1000, 2000)
        print("Your four digit random number is ",number)
        print("Enter this number as a pin.")
        pin = int(input("Enter the four digit number: "))
        print("\n")
        if pin == number:
            print("You have succesfully entered. ")
            about_menu()
            select_options = str(input("Please select one of this options: "))
            if select_options == "1":
                print("Your main balance is ",balance)
                break
            elif select_options == "2":
                cash = float(input("How much do you want to cash out: "))
                if cash <= 300:
                    print("Please collect your cash. ")
                    amount = balance - cash
                    print("Your main balance after cash out is ",amount)
                    break
                else:
                    print("Your maximum amount is only £300. ")
            elif select_options == "3":
                deposit = float(input("Enter the Deposit cash amount: "))
                if deposit <= 300:
                    print("Your amount has been successfully deposit. ")
                    deposit = balance + deposit
                    print("Your final balance is ",deposit)
                    break
                else:
                    print("Your deposit limit is only £300.")
                
        else:
            print("Try again.")
            break

        


if __name__ == '__main__':
    menu()