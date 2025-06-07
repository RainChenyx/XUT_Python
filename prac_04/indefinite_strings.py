"""
until an empty string is entered - then prints all the strings that were entered more than once.
"""


def main():
    user_string = []
    repeated_strings = []
    while True:
        entered_string = input('Enter a string, or enter empty to quit: ')
        if entered_string != "":
            if entered_string in user_string:
                repeated_strings.append(entered_string)
            else:
                user_string.append(entered_string)
        else:
            break
    print(user_string)
    if len(repeated_strings) > 0:
        print("Repeated strings:", repeated_strings)
    else:
        print("No repeated strings entered")


main()
