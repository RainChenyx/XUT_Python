"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "my_car")
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    car_name = input("What's the name of your car: ")
    limo = Car(100, car_name)
    limo.add_fuel(20)
    print("The current fuel level of the vehicle: ", limo.fuel)
    limo.drive(115)
    print("The current car odometer number: ", limo.odometer)
    print(limo)


main()
