"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def display(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for index, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(index+1, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months: "))

    for number_month in range(1, months + 1):
        income = float(input("Enter income for number_month {} : ".format(number_month)))
        incomes.append(income)
    display(incomes)


main()
