"""
A shop requires a small program that would allow them to quickly work out the total price for a number of 
items, each with different prices.
"""
sum_price = 0.00
total_price = 0.00
while True:
    number_items = int(input("Number of items: "))
    if number_items >= 0:
        break
    else:
        print("Invalid number of items,Please enter a valid number.")
for i in range(0, number_items, 1):
    price_items = float(input("Price of item: "))
    sum_price += price_items
if sum_price > 100:
    total_price = sum_price * 0.9
else:
    total_price = sum_price
print(f"Total price for 3 items is ${total_price:.2f}")
