"""Module 2"""
"""2.1"""

name = input("What is your name?")
print(f"Hello, {name}!")

"""2.2"""
import math
radius = int(input("Enter the radius of a circle:"))
area = math.pi * radius ** 2

print(f"Area of the circle: {area:.2f}")

"""2.3"""
length = int(input("Enter the length of a rectangle:"))
width = int(input("Enter the width of a rectangle:"))

perimeter = (length + width) * 2
area = length * width

print(f"perimeter of the rectangle is: {perimeter}")
print(f"area of the rectangle is: {area}")

"""2.4"""

num1 = int(input("Enter the first integer:"))
num2 = int(input("Enter the second integer:"))
num3 = int(input("Enter the third integer:"))

sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum/3

print(f"The sum of the integers is: {sum}")
print(f"The product of the integers is: {product}")
print(f"The average of the integers is: {average}")

"""2.5"""

talents = float(input("Enter Talents:"))
pounds = float(input("Enter Pounds:"))
lots = float(input("Enter Lots:"))

talents_g = 20 * 32 * 13.3 * talents
pounds_g = 32 * 13.3 * pounds
lots_g = 13.3 * lots

mass = talents_g + pounds_g + lots_g
kg = mass // 1000
kg_int = int(kg)
g = mass % 1000

print(f"The weight in modern units:\n{kg_int} kilograms and {g:.2f} grams")