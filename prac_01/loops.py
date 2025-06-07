"""
Add this for loop that displays all the odd numbers between 1 and 20 with a space between each one.
"""
print("Here are the results of the odd numbers between 1 and 20")
for i in range(1, 21, 2):
    print(i, end=" ")
print()
print()

print("Here are the results of the loops.a")
for i in range(0, 101, 10):
    print(i, end=" ")
print()
print()

print("Here are the results of the loops.b")
for i in range(20, 0, -1):
    print(i, end=" ")
print()
print()

print("Here are the results of the loops.c")
star_number = int(input("Enter number of stars : "))
print("Number of stars: ", star_number)
for i in range(1, star_number + 1, 1):
    print("*", end="")
print()
print()

print("Here are the results of the loops.d")
for i in range(1, star_number + 1, 1):
    print(i * "*")
