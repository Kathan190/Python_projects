print("Welcome To My Simple Calculator!")
print("Enter the First number:")
num1 = int(input())
print("Enter the Second number:")
num2 = int(input())
print("Please Select desing +,-,/,*")
num3 = str(input())
if(num3 == "+"):
    add = num1 + num2
    print(add)
elif(num3 == "-"):
    sub = num1 - num2
    print(sub)
elif(num3 == "*"):
    mul = num1 * num2
    print(mul)
elif(num3 == "/"):
    div = num1 / num2
    print(div)
else:
    print("Error! You have entered wrong input, please restart the application")