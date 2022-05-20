#Trying to build number guessing game!

import random
upperbound=int(input("Enter the upperbound : "))
randomnumber=random.randrange(1, upperbound)
def greet():
    print(f"Good, you guessed right number in {count} chance(s).")
def enter_smaller_number():
    print("Try entering smaller number!")
def enter_larger_number():
    print("Try entering larger number!")
ask=None
count=0
while ask!=randomnumber:
    ask=int(input("\nGuess the number : "))
    count+=1
    if ask>randomnumber:
        enter_smaller_number()
    elif ask<randomnumber:
        enter_larger_number()
    else:
        greet()
        break
else:
    greet()

""""
Date : 09/05/2022
Feeling fantastic after completion of writing code ♥

"""
