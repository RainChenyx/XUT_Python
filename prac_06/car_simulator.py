"""
Create a car driving simulator that uses the Car class that works
"""
from car import Car


def main():
    car = Car(100, "The bomb")
    while True:
        __menu__(car)
        choice = input("Enter your choice: ").lower()
        if choice == "d":
            print("How many km do you wish to drive?: ")
            drive = get_number()
            if drive < car.fuel:
                print(f"The car drove {car.drive(drive)}km.")
            else:
                print(f"The car drove {car.drive(drive)}km, and ran out of fuel.")
        elif choice == "r":
            print("Enter the refuel: ")
            refuel = get_number()
            car.add_fuel(refuel)
            print(f"Added {refuel} units of fuel.")
        elif choice == "q":
            break
        else:
            print("Invalid choice")
    print(f"Good bye {car.name}'s driver.")


def __menu__(car):
    print(car)
    print("Menu")
    print("d)drive")
    print("r)refuel")
    print("q)quit")


def get_number():
    while True:
        try:
            number = int(input())
            if number > 0:
                return number
            else:
                print("Number must be > 0.")
        except ValueError:
            print("Please enter a valid number.")


main()
