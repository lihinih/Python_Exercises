#1
import random
def dice_roll():
    rolls = 6

    for roll_num in range(rolls):
        result = random.randint(1, 6)
        print(f"Roll: {roll_num + 1}: {result}")
        if result == 6:
            break
    else:
        print(f"Congratulatons! It took {rolls} rolls to get a 6")

dice_roll()

#2

import random

def roll_until_max(max_number):
    rolls = 0

    while True:
        result = random.randint(1, max_number)
        rolls += 1
        print(f"Roll {rolls}: {result}")
        if result == max_number:
            break

    print(f"Congratulations! It took {rolls} rolls to get a {max_number}.")

number = int(input("Enter a number: "))
roll_until_max(number)

#3

def get_volume(vol_galloon):
    liters = galloon * 3.78541
    if vol_galloon < 0:
        print("Entered invalid amount!!!")

    else:
        print(f"galloon in liters: {liters} l")


galloon = int(input("Enter volume in galloons: "))
get_volume(galloon)

#4

def get_integer(integer_num):
    sum = 0
    for items in integer_num:
        sum += items
    return sum

my_list = [1,2,3,4,5,6]
result = get_integer(my_list)
print(f"The sum of the numbers in the list is: {result}")

#5
list_b = []
def get_list (numbers):
    for i in numbers:
        if i % 2 == 0:
            list_b.append(i)

original_list = [1,2,3,4,5,6]
get_list(original_list)
print(original_list)
print(list_b)

#6

import math
def unit_price_per_square_meter(diameter, price):
    area = math.pi *(diameter/2) ** 2
    pizza_area_m2 = area/10000
    unit_price_per_m2 = price/pizza_area_m2
    return unit_price_per_m2

diameter_pizza1 = float(input("Enter the diameter of the pizza 1 in cm: "))
diameter_pizza2 = float(input("Enter the diameter of the pizza 2 in cm: "))
pizza1_price = int(input("Enter the price of the pizza 1 in centimeters: "))
pizza2_price = int(input("Enter the price of the pizza 2 in centimeters: "))

unit_price1 = unit_price_per_square_meter(diameter_pizza1, pizza1_price)
unit_price2 = unit_price_per_square_meter(diameter_pizza2, pizza2_price)

print(f"Unit price per square meter for the first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price per square meter for the first pizza: {unit_price2:.2f} euros/m²")

if unit_price1 < unit_price2:
    print("\nThe first pizza provides better value for money.")
elif unit_price2 < unit_price1:
    print("\nThe second pizza provides better value for money.")
else:
    print("\nThe two pizzas have the same unit price per square meter.")

