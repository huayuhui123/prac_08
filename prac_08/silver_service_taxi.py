from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23
    flagfall = 4.50

    def __init__(self,name,fuel,fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name,fuel)
        self.current_fare_distance = 0
        self.odometer = 0
        self.fanciness = fanciness * self.price_per_km

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{},fuel={},odo={},{}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(self.name,self.fuel,
                                                            self.current_fare_distance,self.current_fare_distance,
                                                             self.fanciness, self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return float(self.fanciness * self.current_fare_distance + self.flagfall)

