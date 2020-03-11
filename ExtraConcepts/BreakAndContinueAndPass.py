"""
i = 1

while( i<8 ):
    print(f"i = { i }")

    if (i == 2):
        print( f"i = 2 and before continue" )
        i = i + 1
        continue      #it will skip the iteration and continue with next iteration


    if( i==3 ):
        print(f"i = 3 and before continue")
        i = i + 1
        continue       #We can write multiple continue but we can't write multiple breaks.

    if( i == 5 ):
        break          #It will break the loop in between when ever condition gets true.

    if( i == 4 ):
        print("Hello inside 4", end = ', ')
        pass               #It is neutral, it will simply pass the flow of loop.
        print("Hi")


    i = i + 1


print( "Hello" )
"""

'''
l = [5, 7, 9, 13, 2, 3, 4]

for i in l:

    if( i > 10 ):      #break Condition
        pass

    print(i, end=', ')
'''

"""
a = int( input("Enter a number = ") )

if( a < 0 ):
    pass

else:
    print(f"{a} is greater than 0")
"""

"""
for i in range( 1, 11,1 ):

    if( i == 3 ):
        continue

    if( i == 8 ):
        break

    print( f"i = { i }" )
    
"""

"""
for j in range( 1, 5 ):

    for i in range(1, 6):
        if( j == 2 ):
            if( i == 2 ):
                continue
            elif( i == 4 ):
                break

        elif( j == 3 ):
            if( i == 3 ):
                continue
            elif( i == 5 ):
                pass

        elif( j == 4 ):
            if( i == 3 ):
                break

        print(f"i = {i}")

    print()
"""