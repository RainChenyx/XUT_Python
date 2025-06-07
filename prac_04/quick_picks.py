"""
Write a program that asks the user how many "quick picks" they wish to generate.
The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as `CONSTANTS`.
"""

import random


def generates():
    line = []
    while True:
        if len(line) == 6:
            break
        else:
            number = random.randint(1, 45)
            if number not in line:
                line.append(number)
    line.sort()
    return line


def main():
    while True:
        try:
            times = int(input("How many quick picks would you want to generate: "))
            if times > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input, please enter an integer.")
    for i in range(0, times):
        line = generates()
        print(line)


main()
