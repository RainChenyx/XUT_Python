"""
In Python, the + operator concatenates lists.
Write a function, `add_memberwise`, that takes two lists,
and returns the list that contains the sum of elements that are in the same index in the two lists
"""


def add_memberwise(list1, list2):
    list3 = []
    for i in range(max(len(list1), len(list2))):
        val1 = list1[i] if i < len(list1) else 0
        val2 = list2[i] if i < len(list2) else 0
        list3.append(val1 + val2)
    return list3


def main():
    array_1 = []
    array_2 = []
    print("Enter the value of the first array")
    while True:
        user_input = input('Enter a number, or enter quit to quit:')
        if user_input.lower() == 'quit':
            break
        try:
            number = int(user_input)
            array_1.append(number)
        except ValueError:
            print("Invalid input, please enter an integer.")
    print("Enter the value of the second array")
    while True:
        user_input = input('Enter a number, or enter quit to quit:')
        if user_input.lower() == 'quit':
            break
        try:
            number = int(user_input)
            array_2.append(number)
        except ValueError:
            print("Invalid input, please enter an integer.")
    array_3 = add_memberwise(array_1, array_2)
    print("the finally result is: ", array_3)


main()
