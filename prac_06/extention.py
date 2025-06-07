"""
Create a Date* class, storing the fields: day, month, year.
This function is used to add any number of days to change the year, month, and day in the Date class.
This file is created for the Date class
"""


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def add_days(self, n):
        self.day = self.day + n
        max_day = 0
        while self.day > max_day:
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                max_day = 31
                if self.day > 31:
                    self.day = self.day - 31
                    self.month = self.month + 1
                    if self.month > 12:
                        self.month = self.month - 12
                        self.year = self.year + 1
            elif self.month in [4, 6, 9, 11]:
                max_day = 30
                if self.day > 30:
                    self.day = self.day - 30
                    self.month = self.month + 1
                    if self.month > 12:
                        self.month = self.month - 12
                        self.year = self.year + 1
            else:
                if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
                    max_day = 29
                    if self.day > 29:
                        self.day = self.day - 29
                        self.month = self.month + 1
                else:
                    max_day = 28
                    if self.day > 28:
                        self.day = self.day - 28
                        self.month = self.month + 1

    def __str__(self):
        return f'day:{self.day}\nmonth:{self.month}\nyear:{self.year}'
