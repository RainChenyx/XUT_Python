"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for score in score_values[i]:
            print(score)
        print("Max:", max(score_values[i]))
        print()
    print("____________________________________________")
    print("This is the fixed code as required")
    for i in range(len(subjects)):
        print(subjects[i], "Everyone's score:")
        max1 = 0
        min1 = 100
        total = 0
        for j in range(len(score_values)):
            print("the {}-th personal score is {}".format(j + 1, score_values[j][i]))

            total += score_values[j][i]
            if max1 < score_values[j][i]:
                max1 = score_values[j][i]
            if min1 > score_values[j][i]:
                min1 = score_values[j][i]

        print("The highest score in the course is {}".format(max1))
        print("The lowest score for the course is {}".format(min1))
        print("The average score of this course is {}".format(total/10))
        print()


main()
