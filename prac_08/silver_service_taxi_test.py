from prac_08.silver_service_taxi import SilverServiceTaxi

car1 = SilverServiceTaxi("car1",100,2)
print(car1)
car1.drive(18)
print(car1)
print("${}".format(car1.get_fare()))
hummer = SilverServiceTaxi("Hummer",200,4)
print(hummer)
hummer.drive(20)
print(hummer)
print("${}".format(hummer.get_fare()))
