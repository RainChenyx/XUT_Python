"""
Electricity bill estimator 2.0
Now create a version of the above electricity program
that uses a dictionary to store the tariffs and the corresponding cost.
"""


def main():
    tariff = {"TARIFF_11": 0.244618, "TARIFF_31": 0.136928, "TARIFF_51": 0.126328, "TARIFF_71": 0.116948,
              "TARIFF_91": 0.106528}
    for key, valve in tariff.items():
        print(f"{key} is {valve}")
    while True:
        final_number_tariff = int(input("Which tariff(only number): "))
        final_tariff = "TARIFF_" + str(final_number_tariff)
        day_use = float(input("Enter daily use in kWh: "))
        try:
            if final_tariff in tariff.keys() and day_use > 0:
                break
        except ValueError:
            print("Please enter a valid number.")
    cost = day_use * 90 * tariff[final_tariff]
    print(f"Enter number of billing days: 90 Estimated bill: ${cost:.2f}")


main()
