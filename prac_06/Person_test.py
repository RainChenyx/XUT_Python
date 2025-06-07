"""
Similar to the practice question with friends' names and addresses in prac 5, create a program that uses a list of **
Person** objects.  Each Person object records the first-name, last-name and age.  The user can type in the details of
any number of people. The code generates a table formatted with the first-names,last-names, and ages of the
people (perhaps sort the people into order based on their ages).
This file is made using the Person class
"""

from Person import Person


def main():
    persons = []
    while True:
        __menu__()
        choice = input("Choose a letter: ").upper()
        if choice == 'Q':
            break
        elif choice == "A":
            persons = __add__(persons)
        elif choice == "D":
            __display__(persons)
        else:
            print("Invalid choice")
    print("Bye")


def __menu__():
    print("Menu:\nA - Add new person\nD - Display persons\nQ - Quit")


def __add__(persons):
    i = 0
    while True:
        first_name = input("Enter first-name, and enter empty to quit: ").strip()
        if first_name != "":
            last_name = input("Enter last-name: ").strip()
            age = get_age()
            persons.append(Person(first_name, last_name, age))
            i = i + 1
        else:
            break
    persons.sort(key=lambda x: x.age)
    return persons


def get_age():
    while True:
        try:
            age = int(input("Year: "))
            if age > 0:
                return age
            else:
                print("Age must be > 0.")
        except ValueError:
            print("Please enter a valid number.")


def __display__(persons):
    print("*" * 50)
    print(f"*first-name          *last_name           *age   *")
    print("*" * 50)
    for person in persons:
        print(f"*{person.first_name:<20}*{person.last_name:<20}*{person.age:<6}*")
    print("*" * 50)


main()
