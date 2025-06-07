from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fancy and flag fall"""
    flagfall = 4.50

    def __init__(self, name, fuel, fancy):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fancy

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        string = super().__str__() + f" plus flagfall of ${self.flagfall:.2f}"
        return string

    def get_fare(self):
        """Return the price for the Silver Service Taxi trip."""
        total_fare = self.flagfall + super().get_fare()
        return total_fare
