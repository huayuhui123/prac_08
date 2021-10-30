from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius",100), SilverServiceTaxi("Limo",100,2), SilverServiceTaxi("Hummer",200,4)]
    menu(taxis)


def menu(taxis):
    print(" Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>>")
    bill = 0.00
    choose_taxi = []
    while choice != "q" and "Q":
        if choice == 'd' and 'D':
            print(" You need to choose a taxi before you can drive")
            print("Bill to date: ${}".format(bill))
            break
        elif choice != 'q' and choice != 'c' and choice != 'd':
            print("Invalid option")
            print("Bill to date: ${}".format(bill))
            break
        elif choice == 'c' and 'C':
            print("Taxis available: ")
            number = 0
            for taxi in taxis:
                if taxi is Taxi:
                    print("taxi")
                elif taxi is SilverServiceTaxi:
                    print("{}-{},fuel={},{}km on current fare, ${}/km plus flagfall of ${}".format(number, taxi.name,
                                          taxi.fuel, taxi.current_fare_distance, taxi.fanciness, taxi.flagfall))
                number = number + 1
            choice_taxi = input("Choose taxi:")
            if choice_taxi not in number:
                print("Invalid taxi choice")
            else:
                distance = input("Drive how far?")
                taxis[choice_taxi].dive(distance)
                print("Your {} trip cost you ${}".format(taxis[choice_taxi].name,taxis[choice_taxi].get_fare))
                bill = bill + taxis[choice_taxi].get_fare
                choose_taxi.append(taxis[choice_taxi])
        print("Bill to date: ${}".format(bill))
    if choice == 'q' and 'Q':
        print("Total trip cost: ${}".format(bill))
        print("Taxis are now:")
        number = 0
        for element in choose_taxi:
            print("{}-{},fuel={},{}km on current fare, ${}/km plus flagfall of ${}".format(number, element.name,
                                          element.fuel, element.current_fare_distance, element.fanciness,
                                                                                           element.flagfall))
            number = number + 1


main()
