"""
One very common programming task is to make menus by combining looping (repeat the program until
the user quits) with selection (let the user decide what to do).
The general pattern of a menu-driven program is as follows.
"""
name = str(input("Enter name: "))
choice = input("(H)ello\n(G)oodbye\n(Q)uit:\n>>> ").strip().upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit:\n>>> ").strip().upper()
print("Finished.")
