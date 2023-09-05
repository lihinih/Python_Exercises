"""
list = []
while True:
    number = int(input("Enter a Number:"))

    if number < 0:
        break

    list.append(number)
print("Numbers Entered by the user")
print(list)
"""
items = []
while True:
    shop = input("Enter shopping items: ")
    if shop == 'done':
        break

    items.append(shop)
print("\n Shopping items")
for index, item in enumerate(items, start=1):
    print(f"{index}.{item}")
