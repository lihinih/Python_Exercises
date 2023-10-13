"""Module_5"""

#5.1

import random

dice_roll = int(input("How many dice to roll? "))
sum = 0
for dice in range(dice_roll):
    dice_face = random.randint(1,6)
    print(f"Roll: {dice_face}")
    sum += dice_face


print(f"Total sum: {sum}.")



#5.2
number = []

while True:
    user = input('Enter a no: ')
    if user == "":
        break
    try:
        user_int = int(user)
        number.append(user_int)
    except:
        print('Enter an integer')

for elements in number:
    number.sort(reverse=True)
print(number[0:5])



#5.3

user_input = int(input("Enter an integer: "))

if user_input <= 1:
    print(f"{user_input} is not a prime number.")
else:
    for i in range(2, int(user_input**0.5) + 1):
        if user_input % i == 0:
            print(f"{user_input} is not a prime number.")
            break
    else:
        print(f"{user_input} is a prime number.")



#5.4

cities = []

for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    cities.append(city)

print("Cities entered:")
for city in cities:
    print(city)


