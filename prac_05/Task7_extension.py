"""
Convert parallel lists into a dictionary.
3.	Write a function that takes two parallel lists as input parameters and returns a dictionary
where keys are from the first list and the values are from the second. Use the above example as a test case.
"""


def main():
    names = []
    dates_of_birth = []
    file = open('names.txt', 'r')
    for line in file:
        line = line.strip()
        names.append(line)
    file.close()
    file = open('births.txt', 'r')
    for line in file:
        line = line.strip().split(",")
        dates_of_birth.append(line)
    file.close()
    name_birth = switch_dictionary(names, dates_of_birth)
    for key, value in name_birth.items():
        print(f"{key}: {value[0]}/{value[1]}/{value[2]}")
    choice = input("Do you need to add a new list Y/N: ").upper()
    if choice == 'Y':
        name_add = input("What is name: ")
        file = open('names.txt', 'a')
        file.write("\n")
        file.write(name_add)
        file.close()
        birth_add = input("What is births(day, month, year): ")
        file = open('births.txt', 'a')
        file.write("\n")
        file.write(birth_add)
        file.close()
    elif choice == 'N':
        print("Bye Bye!")


def switch_dictionary(names, dates_of_birth):
    name_birth = {}
    for i in range(len(names)):
        name_birth[names[i]] = dates_of_birth[i]
    return name_birth


main()
