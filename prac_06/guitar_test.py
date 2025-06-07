"""
Now write a program with at least enough code to test that the last two methods work as expected.
This file is using the guitar class.
"""

from guitar import Guitar


def main():
    guitars1 = Guitar("Gibson L-5 CES", 1922, 16035.4)
    guitars2 = Guitar("Another Guitar", 2013, 16035.4)
    print(f"Gibson L-5 CES get_age() - Expected 102. Got {guitars1.get_age()}")
    print(f"Another Guitar get_age() - Expected 11. Got {guitars2.get_age()}")
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitars1.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {guitars2.is_vintage()}")


main()
