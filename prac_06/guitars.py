"""
The program should use a list to store all the user's guitars (keep inputting until they enter a blank name), then print
their details.
"""

from guitar import Guitar


def main():
    guitars = []
    i = 1
    print("My guitars!")
    while True:
        guitar_name = input("Name: ")
        if guitar_name != '':
            guitar_year = int(input("Year: "))
            guitar_cost = float(input("Cost: "))
            guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
            print(f"{guitar_name} ({guitar_year}) : ${guitar_cost} added.")
        else:
            break
        i += 1
    print("These are my guitars:")
    j = 1
    for guitar in guitars:
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print(f"guitar {j}: {guitar.name:>20}({guitar.year}), worth $ {guitar.cost:10.2f} {vintage_string}")
        j = j + 1


main()
