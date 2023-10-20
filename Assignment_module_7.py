
#1
seasons = ("Spring","Summer","Autumn","Winter")
month = int(input("Enter the month number to view the season: "))
if month <= 3:
    print(f"This is {seasons[0]} season.")
elif month <= 6:
    print(f"This is {seasons[1]} season.")
elif month <= 9:
    print(f"This is {seasons[2]} season.")
elif month <= 12:
    print(f"This is {seasons[3]} season.")
else:
    print("You have entered an invalid month number.")

#2

names = set()
all_names = []
while True:
    name = input("Enter a name or press enter to done: ")
    if name == "":
        break

    if name in names:
        print("Existing name.")
    else:
        print("New name.")

    for name in names:
        print(names)
        names.add(name)
    all_names.append(name)

print("\nList of names entered:")
for name in all_names:
    print(name)


#3

airport_data = []

def add_airport():
    ICAO_code = input("Enter the ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airport_data.append((ICAO_code, airport_name))
    print(f"Airport {ICAO_code} ({airport_name}) has been added to the database.")


def fetch_airport():
    ICAO_code = input("Enter the ICAO code of the airport: ")
    found = False
    for ICAO, name in airport_data:
        if ICAO == ICAO_code:
            print(f"The name of the airport with ICAO code {ICAO_code} is {name}.")
            found = True
            break
    if not found:
        print(f"Airport with ICAO code {ICAO_code} not found in the database.")


# Main program loop
while True:
    print("Airport Data Program")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Please choose an option (1/2/3): ")

    if choice == "1":
        add_airport()
    elif choice == "2":
        fetch_airport()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3).")