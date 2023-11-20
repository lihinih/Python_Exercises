#1
print("---11.1---")
class Publications:
    def __init__(self, name):
        self.name = name


class Book(Publications):
    def __init__(self, name,author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(f"Name: {self.name}\nAuthor: {self.author}\nPage Count: {self.page_count} ")

class Magazine(Publications):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_info(self):
        print(f"Name: {self.name}\nChief Editor: {self.chief_editor} ")

book = Book("Compartment No. 6","Rosa Liksom", 192)
magazine = Magazine("Donald Duck","Aki Hyppa")

book.print_info()
print("\n")
magazine.print_info()
print("\n")
print("---11.2---")


#2

import random
class Car():

    def __init__(self,registration_number,maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.brake=-200
    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

class ElectricCar(Car):
    def __init__(self,registration_number,maximum_speed,battery_capacity):
        super().__init__(registration_number,maximum_speed)
        self.battery_capacity = battery_capacity

    def print_info(self):
        print(f"Registration Number: {self.registration_number}\nMaximum Speed: {self.maximum_speed}km/h"
              f"\nBattery Capacity: {self.battery_capacity}kWh"
              f"\nElectric Car Kilometer Counter: {electric_car.travelled_distance}km")
class GasolineCar(Car):
    def __init__(self,registration_number,maximum_speed,tank_volume):
        super().__init__(registration_number,maximum_speed)
        self.tank_volume = tank_volume

    def print_info(self):
        print(f"Registration Number: {self.registration_number}\nMaximum Speed: {self.maximum_speed} km/h"
              f"\nBattery Capacity: {self.tank_volume} l"
              f"\nGasoline Car Kilometer Counter: {gasoline_car.travelled_distance}km")

new_car = Car("ABC-123", 142)

print(
    f"CAR INFORMATION.\nRegistration Number: {new_car.registration_number}\nMaximum speed: {new_car.maximum_speed} km/h\nCurrent speed: {new_car.current_speed} \nTravelled distance: {new_car.travelled_distance}.")

new_car.accelerate(30)
print(f"The speed of the car is: {new_car.current_speed} km/h")
new_car.accelerate(70)
print(f"The speed of the car is: {new_car.current_speed} km/h")
new_car.accelerate(50)
print(f"The speed of the car is: {new_car.current_speed} km/h")

new_car.brake
print(f"Final speed after emergency brake: {new_car.current_speed} km/h")

new_car.drive(1.5)
print(f"Updated travelled distance: {new_car.travelled_distance}km.")

import random

car = []

for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100,200)
    car_number = Car(registration_number, maximum_speed)
    car.append(car_number)

race_finished = False
hours = 0

while not race_finished:
 for c in car:
     c.accelerate(random.randint(-15, 10))
     c.drive(1)
     if c.travelled_distance >= 10000:
         race_finished = True
         break
hours += 1
print("-" * 30)
for c in car:
    print(f"Registration Number:", c.registration_number)
    print(f"Maximum Speed:", c.maximum_speed, " km/h")
    print(f"Current Speed:", c.current_speed, " km/h")
    print(f"Travelled Distance:", c.travelled_distance, " km")
    print("-" * 30)
    print(f'Race finished {hours} hour')
print("\n")

electric_car = ElectricCar("ABC-15", 180,52.5)
gasoline_car = GasolineCar("ACD-123",165,32.3)

electric_car.accelerate(40)
electric_car.accelerate(30)

for _ in range(3):
    electric_car.drive(1)
    gasoline_car.drive(1)

electric_car.print_info()
print("\n")
gasoline_car.print_info()






