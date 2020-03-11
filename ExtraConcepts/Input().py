"""
a = 6
b = 8
c = 9
d = True

print("Followings are Initial values, ")
print(f"This is a = {a}")
print(f"This is b = {b}")
print(f"This is c = {c}")
print(f"This is d = {d}")

a = a + 2                       #action( a + 2 )
print()
print("Followings are the values after action, ")
print(f"This is a = {a}")
print(f"This is b = {b}")
print(f"This is c = {c}")
print(f"This is d = {d}")
"""

"""
a = input("Enter the value for a = ")           #1 -> input() -> '1'
b = input("Enter the value for b = ")           #2.3 -> input() -> '2.3'
c = input("Enter the value for c = ")           #'Hello' -> input() -> 'Hello'
d = input("Enter the value for d = ")           #True -> input() -> 'True'

print("Followings are Initial values, ")
print(f"This is a = {a} and type(a) = { type(a) }")
print(f"This is b = {b} and type(b) = { type(b) }")
print(f"This is c = {c} and type(c) = { type(c) }")
print(f"This is d = {d} and type(d) = { type(d) }")
print()

a = int(a)
b = float( b )

print("Followings are values after typeCasting/ Action, ")
print(f"This is a = {a} and type(a) = { type(a) }")
print(f"This is b = {b} and type(b) = { type(b) }")
print(f"This is c = {c} and type(c) = { type(c) }")
print(f"This is d = {d} and type(d) = { type(d) }")
"""

"""
a = int( input("Enter a number = ") )  #Enter a number = 6, 6 -> input() -> '6' -> int() -> 6 -> a

print( f"a = { a } and type( a ) = { type(a) }" )
"""


"""
a = input("Enter a number = ")  # input() -> 5 -> '5' -> int( input() ) -> int( '5' ) -> 5 -> a
print( f"a = { a } and type(a) = { type(a) }" )


for i in range( 1, 3 ):
    print( a*5+9/45-3232*23 )
    print( a*5+9/45-3232*23-2 )
    print( a*5+9/45-3232*23-2*12 )
    print( a*5+9/45-3232*23-2*12-123 )
"""

"""
#print("Enter the Number := ", end = '')
e = input("Enter the Number :=  ")

print( f"e = {e}" )
print( f"type( e ) = { type( e ) }" )

c = e + 'hi'
print( f"Before Error, in case when e is not integer = {c}" )
d = int( e ) + 2
print(f"c = {c}")
print(fa"d = {d}")
print()
print( f"type( c ) = { type( c ) }" )
print( f"type( d ) = { type( d ) }" )
"""

"""
e = input("Enter a number = ")      # input() -> 89 -> '89' -> e
print( f"e = { e }" )
print( f"type(e) = { type(e) }" )

f = int( e ) + 8    #f = ?1, ?1 -> int(e) + 8 -> int(e) = ?2, ?2 = 7
print( f"f = { f }" )
print( f"type( f ) = { type( f ) }" )
print( f"type(e) = { type(e) }" )
"""

"""
a = input("Enter a number = ")

print( f"a = { a } and type(a) = { type(a) }" )
print()
print( f"int(a) = { int(a) } and type( int(a) ) = {  type( int(a) ) }")         #int('6') -> 6 ->X a
print()
print( f"a = { a } and type(a) = { type(a) }" )
a = int(a)                                                                      #a will drop '6' and take 6
print()
print( f"a = { a } and type(a) = { type(a) }" )


a = int( input("Enter a number = ") )   #console -> 6 -> input() -> '6' -> int() -> int('6') -> 6
"""