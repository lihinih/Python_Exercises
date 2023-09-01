"""Module_4"""
"""4.1"""

number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

"""4.2"""

while True:
    inches = float(input("Enter a number: "))

    if inches < 0:
        print ("program ended.")

    break


num_cm = inches * 2.54
print(f"{inches} inches is equal to {num_cm} centimeters")

"""4.3"""

while True:
    user_input = input("Enter a number: ")

    if user_input == "":
        break  # Exit the loop if the user enters an empty string

    try:
        number = float(user_input)  # Convert user input to a floating-point number
        number.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if number:
    smallest = min(number)
    largest = max(number)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")

"""4.4"""

import random


random_number = random.randint(1, 10)
player_guess = 0

while player_guess != random_number:
    player_guess=int(input("guess a number:"))

    if player_guess > random_number:
        print("you are wrong, it's too high")

    elif player_guess < random_number:
        print("you are wrong, it's too low")

    else:
        print("You are correct")

"""4.5"""