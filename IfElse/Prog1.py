'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one qunatity price will be of cost 100.
Judge and print total cost for user.
'''

print("Enter the Quantity = ", end = '')
quantity = input()
quantity = int( quantity )

total = quantity * 100

if(total > 1000):
    discount = 0.1 * total
    total = total - discount
    print(f"total = { total }")
    print(f"Discount = { discount }")

else:
    print(f"total = { total }")
