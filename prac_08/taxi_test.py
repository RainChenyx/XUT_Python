from taxi import Taxi


def main():
    taxi = Taxi("Prius1", 100)
    taxi.drive(40)
    print(taxi)  # Print the taxi’s details
    print(f"The current fare: ${taxi.get_fare():.2f}")  # Print the current fare
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)  # Print the taxi’s details
    print(f"The current fare: ${taxi.get_fare():.2f}")  # Print the current fare


main()
