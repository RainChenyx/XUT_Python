"""
Write a program to count how many times words exist in a string.
The program should ask the user for a string, then print the counts of how many of each word are in the string.
"""
from operator import itemgetter


def main():
    word_count = {}
    sentence = input("Enter a string: ").strip(" ").split(" ")
    for word in sentence:
        try:
            word_count[word] += 1
        except KeyError:
            word_count[word] = 1
    sorted_word_count = sorted(list(word_count.items()), key=itemgetter(0))
    space = max([len(value) for value in sentence])
    for key, value in sorted_word_count:
        print(f"{key:{space}}: {value}")


main()
