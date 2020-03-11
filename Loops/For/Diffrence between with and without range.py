l =  list( range( 100, 300, 3 ) )
print( l )


count_even = 0
count_odd = 0
"""
for i in range( 0, len( l ) ):
    if( l[i]%2 == 0 ):
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1

print( f"Even numbers = { count_even }" )
print( f"Odd numbers = { count_odd }" )
"""


for i in l:
    if ( i%2 == 0):
        count_even = count_even + 1
    else:
        count_odd = count_odd + 1

print( f"Even numbers = { count_even }" )
print( f"Odd numbers = { count_odd }" )