#Comment Types
#Above value is a, b, c and d

#Type Casting = Type( Data Type( int, float, bool, str ) ) + Casting( conversion of any object
#                                                             from one state to another).
#Type Casting = Conversion of datatype of any value from one datatype to another datatype.

#Type Casting Functions,

#Syntax for Type Casting :-

#Situation -> When to Type Cast,

#if( current_data_type != Desired_datatype ):
#    Then, TypeCasting

#How To Type Cast,
#    Current_data_type -> desired_data_type( data ) ->Desired_data_type

#Ex :- '5'-> int( '5' ) -> 5( int )
#i) int()
#ii) float()
#iii) Str()
#iv) bool()

"""
a = -6
b = 7.6
c = True
d1 = 'Hello'
d2 = '5'

print(7)
print('7')

print( type( 7 ) )
print( type( '7' ) )
print()
print( f"a = { a }" )
print( type( a ) )
print( str(a) )  #a = -6 -> str( -6 ) -> '-6' -> print('-6') -> -6
print( f"type(a) = { type(a) }" )
a = str(a)  ##a = -6 -> str( -6 ) -> '-6' -> a    ; a != -6, a = '-6'
print( f"type( a ) = { type( a ) }" )
print()

print( f"b = { b }" )
print( f"type(b) = { type(b) }" )
print( f"str(b) = { str(b) }" )  #7.6 -> str(7.6) -> "7.6"
print( f"type(b) = { type(b) }" )
z = str(b)     #z = '7.6' , b = 7.6
print( f"type(b) = { type(b) }" )
print( f"type(z) = { type(z) }" )
#b = 7.6
#z = "7.6"

print()

print( f"c = { c }" )
print( type(c) )
print( str(c) )     #True ->str(True) -> 'True'
print( type(c) )
c = str(c)
print( type( c ) )
print()
"""

#Any Datatype to int
"""
print( int( True ) )
print( int( False ) )
print( int( 5.6756 ) )
print( int( "123" ) )
print( int( "123abcadw" ) )         #it will convert String data to Integer only when String
                                            #has digits otherwise, It will give error
print( int( "Hellasdsadsa" ) )
"""


#Any Datatype to float
"""
print( float(True) )
print( float(False) )
print( float(5) )
print( float(898) )
print( float('121232') )
print( float("1.23") )
print( float( "142abc" ) )              #-> Error
print( float( "1.42abc" ) )             #-> Error
print( float( "abc" ) )                 #-> Error
"""

#Any Datatype to bool
"""
print( bool(123213) )       #Non - Zero -> True
print( bool(0) )            #0 -> bool() -> False
print( bool(13.12312) )     #Non - Zero -> True
print( bool(0.0) )          #0.0 -> bool() -> False
print( bool("11321") )      #non-empty string -> bool() -> True
print( bool("12321abc") )
print( bool("abc") )
print( bool("") )           #Empty String -> bool() -> False
print( bool(" ") )
"""

#Any Datatype to bool
#str( value ) = "value" or 'value'
"""
print( str( 2342432 ) )         #2342432 -> str() -> '2342432'
print( str( 0 ) )
print( str( 123124.42342 ) )
print( str( 0.0 ) )
print( str( True ) )            #True -> str(True) -> 'True'
print( str( False ) )
"""

"""
Note : boolean and String can change any datatype to any data type where
bool() changes the value and string doesn't change value and add the quotes( ' or " )
"""
