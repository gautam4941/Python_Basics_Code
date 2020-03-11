a = 1500
count = 0

for i in range( 1500, 2701 ):

    if( a%7 == 0 and a%5 == 0 ):
        print( a, end = ', ' )
        count = count + 1

    a = a + 1

print()
print(f"Count = { count }")
