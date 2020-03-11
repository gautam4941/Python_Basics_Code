"""
Write a Python program which accepts the radius of a circle from the user and compute the area
"""

radius = float( input("Enter the Radius of a circle = ") )    #6 -> input() -> '6'

#O/p :- The Radius of Circle is ? and Area = ?

print( f"The Radius of Circle is { radius } and Area = { 3.14 * radius * radius }" )
print()
print( f"The Radius of Circle is { radius } and Area = { 3.14 * radius ** 2 }" )