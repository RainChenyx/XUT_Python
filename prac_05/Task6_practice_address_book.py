"""
Write a program that uses a dictionary to store
and look up your friends’ names and addresses. Assume you don’t have many friends.
"""


def main():
    print("Welcome to friends address book!")
    friends = {}
    __menu__()
    choice = get_choice()
    while choice != "Q":
        if choice == "A":
            add_friend(friends)
        elif choice == "C":
            change_address(friends)
        elif choice == "P":
            display_friend(friends)
        else:
            print("Bye Bye!")
            break
        __menu__()
        choice = get_choice()


def __menu__():
    print("A - Add a new contact name and address.")
    print("C - Change an address for an existing entry.")
    print("P - Print the address for a name you choose.")
    print("Q - Quit.")


def get_choice():
    """ Check menu function choice whether the input is one of A, C, D, and Q. """
    while True:
        try:
            choice = input(">>> ").upper()
            if choice == "A" or choice == "C" or choice == "P" or choice == "Q":
                return choice
            else:
                print("Please enter A or C or P or Q.")
        except ValueError:
            print("Please enter a valid choice.")


def add_friend(friends):
    name = input("What is your friend's name: ")
    address = input("What is your friend's address: ")
    friends[name] = address
    print(f"Your {name}'s name and address have been added.")
    return friends


def change_address(friends):
    name = input("Which friend's existing entry you want to change: ")
    try:
        if name in friends:
            address = input("What is your friend's new address: ")
            friends[name] = address
            print(f"Your {name}'s address has been changed.")
        else:
            print("That name is not in the friends dictionary.")
    except ValueError:
        print("Please enter a valid string.")
    return friends


def display_friend(friends):
    for key, value in friends.items():
        print(f"{key}'s address is {value}.")


main()
