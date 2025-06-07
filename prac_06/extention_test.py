"""
Create a Date* class, storing the fields: day, month, year.
This function is used to add any number of days to change the year, month, and day in the Date class.
This file is using the Date class
"""

from extention import Data


def main():
    year = get_number("day")
    month = get_number("month")
    day = get_number("year")
    data = Data(year, month, day)
    print("What number of days do you want to add: ")
    n = int(get_number("add_day"))
    data.add_days(n)
    print("After adding, the now data is:")
    print(data)


def get_number(string):
    while True:
        try:
            number = int(input(f"{string}: "))
            if (number > 0 and string == "year") or (1 <= number <= 12 and string == "month") or (
                    1 <= number <= 31 and string == "day") or (number >= 0 and string == "add_day"):
                return number
            else:
                print(f"{string} must be > 0.")
        except ValueError:
            print("Please enter a valid number.")


main()
