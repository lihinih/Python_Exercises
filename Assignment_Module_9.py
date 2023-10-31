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







