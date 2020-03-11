"""
@@*
@***
*****
"""

a = 1
b = 0

for i in range( 1, 4, 1 ):

    for j in range( 1, i + a + 1, 1 ):
        print( " ", end = '' )

    for k in range( 1, i + b + 1, 1 ):
        print( "*", end ='' )

    a = a - 2
    b = b + 1

    print()