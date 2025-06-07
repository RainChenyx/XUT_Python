"""
Similar to the practice question with friends' names and addresses in prac 5, create a program that uses a list of **
Person** objects.  Each Person object records the first-name, last-name and age.  The user can type in the details of
any number of people. The code generates a table formatted with the first-names,last-names, and ages of the
people (perhaps sort the people into order based on their ages).
This file is to create the Person class.
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'
