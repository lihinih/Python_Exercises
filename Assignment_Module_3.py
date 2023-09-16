"""Module 3"""
"""3.1"""
zander = float(input("Enter the length of a zander in centimeters: "))
size = 42 - zander
if zander < 42:
    print(f"Zander is {size} cm below the size and release it back to the lake.")

else:
    print("Congratulations!!! you cought within the size.")

"""3.2"""

cabin_class = input("Enter the cabin class:")

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")

elif cabin_class == "A":
    print("above the car deck, equipped with a window.")

elif cabin_class == "B":
    print("windowless cabin above the car deck.")

elif cabin_class == "C":
    print("windowless cabin below the car deck.")

else:
    print("Invalid cabin class.")

"""3.3"""

gender = input("Enter the biological gender male/female:")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":

    if 117 <= hemoglobin <= 155:
        print("Hemoglobin level is normal for adult females.")
    elif hemoglobin < 117:
        print("Hemoglobin level is low for adult females.")
    else:
        print("Hemoglobin level is high for adult females.")

if gender == "male":
    if 134 <= hemoglobin <= 167:
        print("Hemoglobin level is normal for adult males.")
    elif hemoglobin < 134:
        print("Hemoglobin level is low for adult males.")
    else:
        print("Hemoglobin level is high for adult males.")

"""3.4"""

year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")