"""
Mr. Black the school teacher wants an educational program for his school students to explore the details
of ASCII. He wants the app to allow a student to input a character and see the corresponding ASCII code,
and vice versa. A sample run of the program should look like (where g and 100 are user inputs)
"""
while True:
    character_1 = input("Enter a character: ")
    if len(character_1) == 1:
        if 33 <= ord(character_1) <= 127:
            number_1 = ord(character_1)
            print("The ASCII code for {} is {}".format(character_1, number_1))
            break
    else:
        print("Please enter a valid character")
while True:
    number_2 = int(input("Enter a number between 33 and 127: "))
    if 33 <= number_2 <= 127:
        character_2 = chr(number_2)
        print("The character for {} is {}".format(number_2, character_2))
        break
    else:
        print("Please enter a valid number")
for i in range(33, 128):
    print("{}\t {}".format(i, chr(i)))
