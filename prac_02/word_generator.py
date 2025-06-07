"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
word_format = ""
word_user = input("Enter a word to generate: ").lower()
for i in range(len(word_user)):
    if word_user[i] in VOWELS:
        choice = random.choice(['v', '*'])
        word_format += choice
    else:
        choice = random.choice(['c', '*'])
        word_format += choice

word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    elif kind == "v":
        word += random.choice(VOWELS)
    else:
        if random.choice([True, False]):
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
print(word)
