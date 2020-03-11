"""
*@@@@@*
**@@@**
***@***
*******
***@***
**@@@**
*@@@@@*
"""

#To Print above pattern
b = 4

for i in range( 1, 5, 1 ):
    if( i == 4 ):
        print( '*'*7 )

    else:

        for j in range( 1, i + 1, 1 ):
            print( '*', end='' )

        for k in range( 1, i + b + 1, 1 ):
            print( '@', end= '' )

        for l in range( 1, i + 1, 1 ):
            print( '*', end='' )

        b = b - 3
        print()

d = 2
e = 0

for i in range( 1, 4, 1 ):
    for j in range( 1, i + d + 1, 1 ):
        print( '*', end='' )

    for k in range( 1, i + e + 1, 1 ):
        print( '@', end= '' )

    for l in range( 1, i + d + 1, 1 ):
        print( '*', end='' )

    d = d - 2
    e = e + 1
    print()

print()
#Now to print for n number of rows dynamically,

"""
Enter the number of rows = 15

*@@@@@@@@@@@@@*
**@@@@@@@@@@@**
***@@@@@@@@@***
****@@@@@@@****
*****@@@@@*****
******@@@******
*******@*******
***************
*******@*******
******@@@******
*****@@@@@*****
****@@@@@@@****
***@@@@@@@@@***
**@@@@@@@@@@@**
*@@@@@@@@@@@@@*
"""

n = int( input("Enter the number of rows = ") )         #9
b = n-3                                                #6
print()

for i in range( 1, (n//2) + 2, 1 ):            #1, .., 5
    if( i == ( (n//2) + 1 ) ):                     #i == 5
        print( '*'*n )

    else:
        for j in range( 1, i + 1, 1 ):
            print( '*', end='' )

        for k in range( 1, i + b + 1, 1 ):
            print( '@', end= '' )

        for l in range( 1, i + 1, 1 ):
            print( '*', end='' )

        b = b - 3
        print()

d = (n//2) - 1
e = 0

for i in range( 1, (n//2) + 1, 1 ):                #1,
    for j in range( 1, i + d + 1, 1 ):
        print( '*', end='' )

    for k in range( 1, i + e + 1, 1 ):
        print( '@', end= '' )

    for l in range( 1, i + d + 1, 1 ):
        print( '*', end='' )

    d = d - 2
    e = e + 1
    print()