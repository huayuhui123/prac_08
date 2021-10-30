from prac_06.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)

    def drive(self, distance):
        super().drive(distance)
        if random.uniform(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            return distance
        else:
            print("reliability is too low!")
