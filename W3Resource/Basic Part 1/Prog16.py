"""
Write a Python program to get the difference between a given number and 17,
 if the number is greater than 17 return double the absolute difference
"""

num = int( input("Enter a number = ") )

if( num > 17 ):
    print( f"Entered Number is { num } and Diffrence is { num - 17 } and Answer = { ( num -17) * 2 }"  )