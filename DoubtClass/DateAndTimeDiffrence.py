d1 = int( input("Enter the 1st date = ") )
m1 = int( input("Enter the 1st month = ") )
y1 = int( input("Enter the 1st year = ") )

d2 = int( input("Enter the 2nd date = ") )
m2 = int( input("Enter the 2nd month = ") )
y2 = int( input("Enter the 2nd year = ") )


if( y1 > y2 ):
    y = y1 - y2
else:
    y = y2 - y1

if( m1 > m2 ):
    m = m1 - m2
else:
    m = m2 - m1

if( d1 > d2 ):
    d = d1 - d2
else:
    d = d2 - d1

print( f" d1 = { d1 }, m1 = { m1 } and y1 = { y1 }" )
print( f" d1 = { d2 }, m2 = { m2 } and y2 = { y2 }" )
print( f"d = { d }, m = { m } and y = { y }" )

d = d + ( (365/12) *m ) + ( 365*y )

print( f"Total Number of Days Calculated = {d}" )

if( d%1 != 0 ):
    if( d%1 >= 0.5 ):
        d = d // 1
        d = d + 1
    else:
        d = d // 1
        d = d -  1

print( f"Rounder Date = { d }" )