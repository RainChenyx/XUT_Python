"""
GPS (Gopher Population Simulator)
Write a program that simulates a population of gophers over a ten-year period and displays each
year’s population size. The output should look something like this (it’s random, so yours won’t be the
same)
"""

import random


def main():
    population = 1000  # initial population size is 1000
    print("Welcome to the Gopher Population Simulator!\nStarting population: 1000")
    for year in range(1, 11):
        birth_rate = random.uniform(0.1, 0.2)
        birth_number = population * birth_rate
        death_rate = random.uniform(0.05, 0.25)
        death_number = population * death_rate
        population = population + birth_number - death_number
        print(f"Year {year}\n")
        print(f"{birth_number:.0f} were born. {death_number:.0f} were died.")
        print(f"Gophers Population: {population:.0f}")


main()
