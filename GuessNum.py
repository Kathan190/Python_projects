import random

guess_taken = 0 

print("Enter Your Name here Please:")
my_name = str(input())

number = random.randint(1,20)
print("Well " + my_name + " I am a thinking a number between 1 to 20.")

while guess_taken < 6:
    guess = input()
    guess = int(guess)

    guess_taken = guess_taken + 1

    if guess < number:
        print("You guess lower number.")

    if guess > number:
        print("You guess higher number.")
    
    if guess == number:
        break

if guess == number:
    guess_taken = str(guess_taken)
    print("You took " + guess_taken + "chances.")

if guess != number:
    number = str(number)
    print("Nope, i was not thinking " + number + " number")


