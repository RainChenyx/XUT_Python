import random


def is_valid_format(word_format):
    all_valid = 'aeioubcdfghjklmnpqrstvwxyz#%'
    for char in word_format:
        if char not in all_valid:
            return False
    return True


def get_random_consonant():
    consonants = 'bcdfghjklmnpqrstvwxyz'
    return random.choice(consonants)


def get_random_vowel():
    vowels = 'aeiou'
    return random.choice(vowels)


def generate_word(word_format):
    word = ""
    for char in word_format:
        if char == '%':
            word += get_random_consonant()
        elif char == '#':
            word += get_random_vowel()
        else:
            word += char
    return word


def main():
    possible_formats = ['%#%', '%#%', '%%#%', '%#%%', '%#%#']
    word_format = random.choice(possible_formats)
    print(f"For exemples: {word_format}, ccvcc, cc%#c ")
    while True:
        user_input = input("Enter a word to generate: (like %re#l or ccvcc，% is consonant，# is vowel): ")
        word_format = user_input.lower()
        is_valid_format(word_format)
        if is_valid_format(word_format) and len(word_format) != 0:
            break
        else:
            print("Please enter a valid word.")
    generated_word = generate_word(word_format)
    print(f"The new word is: {generated_word}")


main()
