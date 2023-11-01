#1,2,3


class Elevator:
    def __init__(self,top_floor,bottom_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
           self.current_floor += 1
           print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
           self.current_floor -= 1
           print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, destination_floor):
        while self.current_floor < destination_floor:
            self.floor_up()
        while self.current_floor > destination_floor:
            self.floor_down()

h = Elevator(5,0)
h.go_to_floor(5)
h.go_to_floor(0)


class Building:
    def __init__(self,top_floor,bottom_floor,no_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(no_elevators)]


    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            h = self.elevators[elevator_num]
            print(f'Running elevator {elevator_num} to floor {destination_floor}')
            h.go_to_floor(destination_floor)
        else:
            print(f'Elevator {elevator_num} does not exist in the building.')

    def fire_alarm(self):
        for i,elevator in enumerate(self.elevators):
            elevator.go_to_floor(self.bottom_floor)
            print(f"Elevator {i} is on the bottom floor.")
            print("Fire alarm!!!.All elevators move to down.")


building = Building(0, 10, 3)
building.run_elevator(1, 5)
building.run_elevator(2,1)
building.fire_alarm()

#4
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

class Race:
    def __init__(self,name,distance,car):
        self.name = name
        self.distance = distance
        self.car = car

    def hour_pass(self):
        for car in self.car:
            car.accelerate(random.randint(-15,10))
            car.drive(1)

    def print_status(self):
        print("-" * 60)
        print(f"Race: {self.name} | Distance: {self.distance} km")
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Car", "Max Speed (km/h)", "Current Speed (km/h)",
                                                          "Distance Traveled (km)", "Status"))
        for car in self.car:
            status = "Finished" if car.travelled_distance >= self.distance else "In Progress"
            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(car.registration_number, car.maximum_speed,
                                                              car.current_speed, car.travelled_distance, status))
        print("-" * 60)
    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.car)

new_car = Car("ABC-123", 142)

import random

car = []

for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100,200)
    car_number = Car(registration_number, maximum_speed)
    car.append(car_number)

grand_derby = Race("Grand Demolition Derby", 8000, car)

hours = 0
while not grand_derby.race_finished():
    grand_derby.hour_pass()
    if hours % 10 == 0:
        grand_derby.print_status()
    hours += 1

grand_derby.print_status()
print("Race finished after", hours, "hours.")


