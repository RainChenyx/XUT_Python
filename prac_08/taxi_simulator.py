from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.00
    number = -1
    print("Let's drive!")
    while True:
        menu()
        choice = get_choice()
        if choice == 'Q':
            quit_taxi(taxis, bill)
            break
        elif choice == 'C':
            number = choose_taxi(taxis)
        elif choice == 'D':
            if 0 <= number <= 2:
                bill += drive_taxi(taxis[number])
            else:
                print("You need to choose a taxi before you can drive")
        print(f"Bill to date: ${bill:.2f}")


def menu():
    """Display menu options"""
    print("(q)quit, (c)choose taxi, (d)drive")


def quit_taxi(taxis, cost):
    """Quit taxi function and print all information including bill and situation of taxis"""
    print(f"Total trip cost: ${cost:.2f}")
    print("Taxis are now:")
    print("0 - ", taxis[0])
    print("1 - ", taxis[1])
    print("2 - ", taxis[2])


def get_choice():
    """This is the function that gets the options"""
    choice = input(">>> ").upper()
    try:
        if choice == 'Q' or choice == 'C' or choice == 'D':
            return choice
        else:
            print("Invalid option")
    except ValueError:
        print("Invalid option")


def choose_taxi(taxis):
    """This is the function used to select the type of taxi"""
    print("Taxis available: ")
    print(f"0 - {taxis[0]}")
    print(f"1 - {taxis[1]}")
    print(f"2 - {taxis[2]}")
    taxi_number = int(input("Choose taxi: "))
    if 0 <= taxi_number <= 2:
        return taxi_number
    else:
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    """This is a function of how far you want the taxi to go"""
    distance = float(input("Drive how far? "))
    if distance < 0:
        print("Invalid distance")
        return 0
    else:
        taxi.start_fare()
        taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${taxi.get_fare():.2f}")
        bill = taxi.get_fare()
        return bill


main()
