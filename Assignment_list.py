list = []
while True:
    number = int(input("Enter a Number:"))

    if number < 0:
        break

    list.append(number)
print("Numbers Entered by the user")
print(list)