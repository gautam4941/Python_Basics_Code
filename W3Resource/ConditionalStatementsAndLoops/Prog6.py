"""
Write a Python program to count the number of even and odd numbers from a series of numbers.
"""

start = 10
end = 1

if( start > end ) :
    temp = start       #temp = 10
    start = end        #start = 1
    end = temp          #end = 10

while( start <= end ):
    if( start%2 == 0 ):
        print( f"Even = { start }" )

    else:
        print( f"Odd = { start }" )

    start = start + 1
    start = start + 1