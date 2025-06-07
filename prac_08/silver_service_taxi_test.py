from silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi_1 = SilverServiceTaxi("Hummer", 200, 4)
    print(silver_service_taxi_1)
    print()
    silver_service_taxi_2 = SilverServiceTaxi("New Silver Service Taxi", 200, 2)
    print(silver_service_taxi_2)
    print("After New Silver Service Taxi travelled 18 kilometres")
    silver_service_taxi_2.drive(18)
    print(silver_service_taxi_2)  # Print the taxi’s details
    print(f"The current fare: ${silver_service_taxi_2.get_fare():.2f}")  # Print the current fare


main()
