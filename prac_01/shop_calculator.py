"""
CP1404
Pseudocode for Shop Calculator
"""

total_price = 0
new_total_price = 0
num_items = int(input("Please Enter the number of items: "))

while num_items < 0:
    num_items = int(input("Please Re-Enter the number of items: "))

for i in range(num_items):
    item_price = float(input("Please Enter price of item: "))
    total_price += item_price

if total_price <= 100:
    print("Total price for " + str(num_items) + " items is " + str(total_price))
else:
    new_total_price = total_price * 0.9
    print("Total price for " + str(num_items) + " items is " + str(new_total_price))

