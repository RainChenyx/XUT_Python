"""
write a new function that takes in the user’s score as a parameter and returns the result to be
printed. The function should not print it.
"""

import random


def main():
    score = __get_score__()
    print("The random score is {}".format(score))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score > 90:
            print("Excellent")
        elif score > 50:
            print("Passable")
        else:
            print("Bad")


def __get_score__():
    score = random.randint(0, 100)
    return score


main()
