"""
The program should then print asterisks as long as the word.
Add password check program
"""


def main():
    """Program to get and check a user's password."""
    MIN_LENGTH = 6
    i = 0
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH)
    password = input("> ")
    while not is_valid_password(password, MIN_LENGTH):
        print("Invalid password!")
        password = input("> ")
    for i in range(len(password)):
        print("*", end="")


def is_valid_password(password, MIN_LENGTH):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH:
        return False
    else:
        return True


main()
