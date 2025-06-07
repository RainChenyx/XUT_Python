"""
A school teacher requires a small program that would allow primary school students to learn about
various number sequences. The teacher is interested in a simple menu-driven program that has the
following choices (where x and y are inputs the user enters once at the start of the program).
"""
print("Simple menu-driven program")
print("1. Show the even numbers from x to y")
print("2. Show the odd numbers from x to y")
print("3. Show the squares from x to y")
print("4. Exit the program")
x = 0
y = 0
'''
while True:
    choice = int(input("Enter your choice: "))
    if 0 < choice <= 4:
        if choice != 4:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
        break
    else:
        print("Invalid number of choice,Please enter a valid number.")
'''
while True:
    choice = int(input("Enter your choice: "))
    if 0 < choice < 4:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
    if choice == 1:
        print("the even numbers from x to y : ")
        if x % 2 == 0:
            for i in range(x, y + 1, 2):
                print(i, end=" ")
        else:
            for i in range(x + 1, y + 1, 2):
                print(i, end=" ")
        print()
    elif choice == 2:
        print("the odd numbers from x to y : ")
        if x % 2 == 0:
            for i in range(x + 1, y + 1, 2):
                print(i, end=" ")
        else:
            for i in range(x, y + 1, 2):
                print(i, end=" ")
        print()
    elif choice == 3:
        print("the squares from x to y: ")
        for i in range(x, y + 1, 1):
            print(i * i, end=" ")
        print()
    elif choice == 4:
        print("Finished.Thank you for your use.")
        break
    else:
        print("Invalid number of choice,Please enter a valid number.")
