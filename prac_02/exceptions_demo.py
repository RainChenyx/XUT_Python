"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

'''
Q1: When the value entered cannot be converted to an integer (if the user enters a letter, symbol, or empty string).
Q2: When the denominator entered by user is 0.
Q3: Here is the modified code
try:  
    numerator = int(input("Enter the numerator: "))  
    denominator = int(input("Enter the denominator: "))  

    if denominator == 0:  
        print("Cannot divide by zero!")  # The tip cannot be zero  
    else:  
        fraction = numerator / denominator  
        print(f"Result: {fraction}")  

except ValueError:  
    print("Numerator and denominator must be valid numbers!")  
# Remove the except ZeroDivisionError section
print("Finished.")
'''