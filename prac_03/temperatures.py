"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = __fahrenheit__(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = __celsius__(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def __fahrenheit__(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def __celsius__(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
