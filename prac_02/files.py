"""
the intention is to give you experience using different ways to read files.
"""

name = input("enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)  # It also can use: print(name, file=out_file)
out_file.close()
out_file = open("name.txt", "r")
print(out_file.read())
out_file.close()
out_file = open("numbers.txt", "r")
numbers = []
for i in range(2):
    line = out_file.readline()
    if line:
        numbers.append(int(line.strip()))
result = numbers[0] + numbers[1]
print("The sum of the first two numbers is:", result)
out_file.seek(0)
line_count = 0
for j in out_file:
    line_count += 1
print(f"The total number of lines in the file is: {line_count}")
out_file.close()
