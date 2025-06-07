"""
Write a program that stores users’ emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
"""


def main():
    email = get_email()
    display_email(email)


def get_email():
    email = {}
    email_address = input("Please enter your email address, and enter empty to quit: ").strip()
    email_name = email_address.split('@')
    while email_address != "":
        while True:
            is_correct = input(f"Is the name '{email_name[0]}' correct? (Y/n) ").upper()
            if is_correct == "Y" or is_correct == "YES" or is_correct == " ":
                email[email_address] = email_name[0]
                break
            elif is_correct == "N" or is_correct == "NO":
                name = input("Please enter your name: ").strip()
                email[email_address] = name
                break
            else:
                print("Please enter a value between Y and N.")
        email_address = input("Please enter your email address, and enter empty to quit: ").strip()
        email_name = email_address.split('@')
    return email


def display_email(email):
    for key, value in email.items():
        print(f"{value} ({key})")


main()
