"""
Create scores.py and copy in only your function from broken_score.py above. Now write a main program 
that uses this function:
"""

import random


def main():
    while True:
        numbers = int(input("Enter numbers of score: "))
        if numbers > 0:
            break
        else:
            print("Invalid number!")
    out_file = open("results.txt", "w")
    for i in range(numbers):
        score = __get_score__()
        result = __result__(score)
        print("the {}-th score is {},and it is {}.".format(i+1, score, result))
        out_file.write(str(score) + " is " + result + "\n")
    out_file.close()


def __get_score__():
    score = random.randint(0, 100)
    return score


def __result__(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"


main()
