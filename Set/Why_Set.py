a = list( range(1, 1000) )          #1, 2, 3, .., 999

print( f"type(a) = { type(a) } and len(a) = { len(a) }" )
print()

b = list( range( 1, 1000, 2 ) )     #1, 3, 5, .., 999

print( f"type(b) = { type(b) } and len(b) = { len(b) }" )
print()

for i in b:
    a.append( i )

print("After Appending, ")
print( f"type(a) = { type(a) } and len(a) = { len(a) }" )
print( f"type(b) = { type(b) } and len(b) = { len(b) }" )

c = set( a )
print()
print( f"type(a) = { type(a) } and len(a) = { len(a) }" )
print( f"type(b) = { type(b) } and len(b) = { len(b) }" )
print( f"type(c) = { type(c) } and len(c) = { len(c) }" )