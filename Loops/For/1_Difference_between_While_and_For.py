"""
i = 0
while( i<= 5 ):
    print( "Before Increment, i -> ", i )
    if( a[i]%2 == 0 ):
        print( a[i] )
        i = i + 2
    else:
        i = i + 1

    print( "After Increment, i -> ", i )
"""

"""
a = [6, 5, 7, 8, 9, 10 ]

for i in range( 0, 6, 1 ):
    print("Before Increment, i -> ", i)  #i=0, 1
    if (a[i] % 2 == 0):
        print(a[i])
        i = i + 2
    else:
        i = i + 1                   #i = 2

    print("After Increment, i -> ", i) #i = 2, # i = 2
    
    #i = 3, i = 3

print( "i -> ", i )
"""

"""
for i in range( 1, 6, 1 ):   # i = 1, i < 6, i = i + 1
    print( i )
#i = 6
print()
for i in range( 1, 4, 1 ):   #i = 1, i < 4, i = i + 1
    print( i )
"""

"""
for i in range( 1, 4, 1 ):
    print( i )

print()
for i in range( 1, 4 ):   #by default increment is 1
    print( i )

print()
for i in range( 4 ):      #by default start is 1
    print( i )

"""

"""
import  random

a = []

for i in range( 1, 1000000, 1 ):
    a.append( random.randrange( 1, 100, 1 ) )

print( a )
print( "len(a) = ", len( a ) )
print( "len(a) - 1 = ", len( a ) - 1 )
print( "a[ len( a ) - 2 ] = ", a[ len( a ) - 2 ] )

for i in range( 0, len( a ) ):
    print( "i = ", i, "a[i] = ", a[i] )
    
"""