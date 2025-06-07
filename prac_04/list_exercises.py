"""
Write a program that prompts the user for 5 numbers and then stores each of these in a list called `numbers`.
The program should then output various interesting things,
"""


def main():
    print("____________________________________________")
    print("This is Task 1")
    numbers = []
    while True:
        number = int(input("Enter {}-th number: ".format(len(numbers) + 1)))
        if number >= 0:
            numbers.append(number)
        elif number < 0:
            break
        else:
            print("Please enter a valid number.")
    print("The list has:", len(numbers), "elements")
    print("The first number is ", numbers[0])
    print("The last number is ", numbers[-1])
    print("The smallest number is ", min(numbers))
    print("The largest number is ", max(numbers))
    print("The average of the numbers is ", sum(numbers) / len(numbers))
    print("____________________________________________")

    print("This is Task 2")
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = input("What is your name? ")
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")
    print("____________________________________________")


main()
