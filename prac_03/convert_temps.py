"""
Now write a program, convert_temps.py , that uses the functions you made to convert temperatures.
Read the values in temps_input.txt as Fahrenheit values and write the converted Celsius values to
temps_output.txt .
"""


def main():
    out_file_input = open('temps_input.txt', 'r')
    out_file_output = open('temps_output.txt', 'w')
    for line in out_file_input:
        fahrenheit = float(line.strip())
        celsius = __celsius__(fahrenheit)
        print(f"Celsius: {celsius}")
        out_file_output.write(f"{celsius}\n")
    out_file_input.close()
    out_file_output.close()


def __celsius__(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
