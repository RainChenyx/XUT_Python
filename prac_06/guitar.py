"""
Write a Guitar class  that allows you to store one guitar with those.
"""
import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.old = None
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"Name: {self.name}({self.year}) : $ {self.cost:.2f}"

    def get_age(self):
        self.old = datetime.datetime.now().year - self.year
        return self.old

    def is_vintage(self):
        self.get_age()
        if self.old >= 50:
            return True
        else:
            return False
