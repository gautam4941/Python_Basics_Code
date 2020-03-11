"""
    *
   **
  ***
 ****
*****

a = 3

for i in range( 1, 6 ):

    for j in range( 1, i+ a + 1 ):
        print( ' ', end='' )

    for k in range( 1, i+ 1 ):
        print( '*', end = '' )

    print()

    a = a - 2
"""

b = 3

for i in range( 1, 6 ):

    for j in range( 1, i + 1 ):
        print( '*', end = '' )

    for k in range( 1, i+b+1 ):
        print( '@', end = '' )

    print()
    b = b - 2
