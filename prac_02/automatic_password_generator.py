import string
import random

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def generate_password():
    user_length = int(input("Enter length of password: "))
    special_chars_required = input("Do you want special characters in your password? (y/n): ").lower() == 'y'
    while True:
        final_password = ""
        for i in range(user_length):
            number_random = random.randint(1, 4)
            if number_random == 1:
                final_password += random.choice(string.ascii_uppercase)
            elif number_random == 2:
                final_password += random.choice(string.ascii_lowercase)
            elif number_random == 3:
                final_password += random.choice(string.digits)
            elif special_chars_required and number_random == 4:
                final_password += random.choice(SPECIAL_CHARACTERS)
        if is_valid_password(final_password):
            return final_password


def main():
    password = generate_password()
    print("Your {}-character password is : {}".format(len(password), password))


# Using my earlier program’s checker functionality (password_checker.py) to validate the generated password.
def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if "a" <= char <= "z":
            count_lower += 1
        elif "A" <= char <= "Z":
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        else:
            if char in SPECIAL_CHARACTERS:
                count_special += 1
    if count_lower > 0 and count_upper > 0 and count_digit > 0:
        return True
    else:
        return False


main()
