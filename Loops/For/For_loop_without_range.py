"""
for i in range( 0, 10, 1 ):
    print( 1, end = ', ' )

print( f"i = { i }" )

for i in range( 0, 10 ):
    print( 1, end = ', ' )

print( f"i = { i }" )

for i in range( 10 ):
    print( 1, end = ', ' )

print( f"i = { i }" )
"""

"""
#Diffrence between while loop and for loop,  Increment in loop variable at mid is not possible in
#for loop whereas, it is possible in while loop.

i = 1
while( i <= 10 ):
    if( i%2 == 1 ):
        print( 1, end='Odd, ' )
        i = i + 1

    else:
        print( 1, end = 'Even, ' )
        i = i + 2

print()

for i in range( 1, 11 ):
    if( i%2 == 1 ):
        print( 1, end = ', ' )
        i = i + 1

    else:
        print(1, end=', ')
        i = i + 2
        
"""

"""
#High to Low

i = 10

while( i >= 1 ):
    print( i, end = ', ' )

    i = i - 3

print()
for i in range( 10, 0, - 3):
    print( i, end=', ' )
"""