"""
Create an electricity bill estimator to calculate the estimated electricity bill.
"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
bill = 0.00
print("Electricity bill estimator 2.0")
number_tariff = int(input("Which tariff? 11 or 31: "))
daily_use = float(input("Enter daily use in kWh: "))
number_day = int(input("Enter number of billing days: "))
if number_tariff == 11:
    bill = TARIFF_11 * daily_use * number_day
if number_tariff == 31:
    bill = TARIFF_31 * daily_use * number_day
print(f"Estimated bill: ${bill:.2f}")
