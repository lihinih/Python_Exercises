
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

smallest = None
largest = None

while True:
    user_input = input("Enter a number: ")

    if user_input == "":
        break

    number = float(user_input)

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

if smallest is not None and largest is not None:
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")

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

correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:

    username = input("Enter username: ")
    password = input("Enter password: ")


    if username == correct_username and password == correct_password:
        print("Welcome")
        break

    print("Invalid credentials. Please try again.")
    attempts += 1

if attempts == 5:
    print("Access denied")

"""4.6"""

s