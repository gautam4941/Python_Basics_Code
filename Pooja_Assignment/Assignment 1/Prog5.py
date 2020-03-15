a, b, c = input().split(',')
a = int( a )
b = int( b )
c = int( c )

def F( num ):
    if (num > b):
        return num - c

    else:
        return F(a + F(a + F(a + F(a + num ) ) ) )

sum = 0
for i in range( b+1 ):
    sum = sum + F( i )

print( sum )