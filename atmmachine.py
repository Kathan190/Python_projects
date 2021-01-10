balance = 1000
chances = 0
print("Welcome to my Atm.")
print("Here, Below these are some instruction.")
print("You have to enter Your first name and everything shows up on the screen.")

dict1 = {'kathan':"sheth, Acc-no: 121212",
'Atik':'Sindha, Acc-no: 212121',
'Darshan':'Dabhi, Acc-no: 313131',
'Krunesh':'Patel, Acc-no: 414141'}

first_name = str(input("First Name: "))
print(dict1[first_name])

pin = int(input("Enter your four digit pin number: "))
if (pin == 1234):
    print("There are four options for you.\n ")
    print("1. Display Balance. ")
    print("2. Deposit the Cash. ")
    print("3. Cash Out. ")
    print("4. Reset the Pin. ")
    options = str(input("Select the number: "))
    while (options == "1"):
        print("Your main balance is ",balance)
        break
    if (options == "2"):
        print("How much You want to Deposit Cash. ")
        deposit = int(input("Enter the Amount here: "))
        if (deposit <= 1000):
            print("You successfully deposit the amount. ")
            amount = deposit + balance
            print("Your main balance is: ",amount)
        else:
            print("You can not deposit over 1000 Pound. ")
            
       

    