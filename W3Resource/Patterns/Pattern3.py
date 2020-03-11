"""
        *
      * *
    * * *
  * * * *
* * * * *
"""

a = 3
i = 1
while( i<= 5 ):
    j = 1
    while( j <= i + a ):
        print( ' ', end = ' ' )
        j = j + 1

    j = 1
    while( j <= i ):
        print( '*', end =' ' )

        j = j + 1

    print()

    i = i + 1
    a = a - 2