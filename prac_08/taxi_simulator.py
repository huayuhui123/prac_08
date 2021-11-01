from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius",100), SilverServiceTaxi("Limo",100,2), SilverServiceTaxi("Hummer",200,4)]
    menu(taxis)


def menu(taxis):
    global choice_taxi
    print(" Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>>")
    bill = 0.00
    choose_taxi = []
    while choice != "q" and choice != "Q":
        if choice == 'c' or choice == 'C':
            print("Taxis available: ")
            for index, taxi in enumerate(taxis):
                if taxi.fanciness != None:
                    print("{}-{},fuel={},{}km on current fare, ${}/km plus flagfall of ${}".format(index, taxi.name,
                                          taxi.fuel, taxi.current_fare_distance, taxi.fanciness, taxi.flagfall))
                else:
                    print("{}-{},fuel={},{}km on current fare, ${}/km".format(index, taxi.name,
                                          taxi.fuel, taxi.current_fare_distance, taxi.price_per_km))
            choice_taxi = int(input("Choose taxi:"))
            if choice_taxi < 0 or choice_taxi > (len(taxis)-1):
                print("Invalid taxi choice")
            else:
                choose_taxi.append(taxis[choice_taxi])
        elif choice == 'd' and 'D':
            if len(choose_taxi) == 0:
                print(" You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far?"))
                taxis[choice_taxi].drive(distance)
                print("Your {} trip cost you ${}".format(taxis[choice_taxi].name,taxis[choice_taxi].get_fare()))
                bill = bill + taxis[choice_taxi].get_fare()
        else:
            print("Invalid option")
        print("Bill to date: ${}".format(round(bill,2)))
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>>")
    if choice == 'q' or 'Q':
        print("Total trip cost: ${}".format(round(bill,2)))
        print("Taxis are now:")
        for index,taxi in enumerate(choose_taxi):
            if taxi.fanciness != None:
                print("{}-{},fuel={},{}km on current fare, ${}/km plus flagfall of ${}".format(index,taxi.name,
                                                                                               taxi.fuel,
                                                                                   taxi.current_fare_distance,
                                                                                               taxi.fanciness,
                                                                                               taxi.flagfall))
            else:
                print("{}-{},fuel={},{}km on current fare, ${}/km".format(index, taxi.name,
                                                                          taxi.fuel, taxi.current_fare_distance,
                                                                          taxi.price_per_km))


main()
