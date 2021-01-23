import sys
import random
import math

balance = 1000
number = random.randint(1000, 2000)

def about_menu():
    print("1. Check your Balance.")
    print("2. Cash out.")
    print("3. Deposit the Cash.")
    input("Push Enter for going for main menu. ")

def menu():
    while True:
        number = random.randint(1000, 2000)
        print("Your four digit random number is ",number)
        print("Enter this number as a pin.")
        pin = int(input("Enter the four digit number: "))
        if pin == number:
            print("You have succesfully entered. ")
            print("Please select this options.")
            about_menu()
        else:
            print("Try again.")
            break

    


if __name__ == '__main__':
    menu()