"""
CP1404/CP5632 Practical
Car class
"""
from prac_06.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, price_per_km):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round(self.price_per_km * self.current_fare_distance,1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


prius = Taxi('Prius 1', 100, 1.23)
prius.drive(40)
print(prius)
prius.start_fare()
prius.price_per_km = 2
prius.drive(100)
print(prius)
print(prius.get_fare())
