from car import Car
import random


class UnreliableCar(Car):
    """A dedicated version of the car including reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.name = name
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        """Drive like a Car, but consider the probability of whether it can drive."""
        random_int = random.randint(0, 100)
        if random_int < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = super().drive(0)
            return distance_driven
