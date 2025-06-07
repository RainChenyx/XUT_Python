"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    while True:
        score = int(input("Enter score: "))
        if score < 0 or score > 100:
            print("Invalid score")
        else:
            break
    result = __get_result__(score)
    print("the score is {},and it is {}.".format(score, result))
    # Now add a new part that generates a random score and prints the result.
    score = random.randint(0, 100)
    result = __get_result__(score)
    print("This is the newly generated score and its result")
    print("the random score is {},and it is {}.".format(score, result))


def __get_result__(score):
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
