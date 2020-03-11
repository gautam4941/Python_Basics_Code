"""
#Case 1 :-
19+10 = 29
19-10 = 9

#Case 2 :-
5+2 = 7
5-2 = 3

#address of 2 = 1064
#address of 0 = 1000
#diffrence of address = 64
#address of 5 = 1160 + diffrence of address -> 1160 + 64 = 1224 -> 7
"""

"""
#Arithmetic Operator -> +, -, *, /, %, //, **

#Input :- Numbers
#Output Data :- Number

print( 2+3 )
print( 2-3 )
print( 2*3 )
print( 2/3 )
print( 2//3 )
print( 2%3 )
print( 15/4 )
print( 199/100 ) #Divide the both operand but shows integer part + decimal part( Deciaml Division ).
print( 199//100 ) #Divide the both operand but shows only integer part( Integer Divison ).
print( 5 * 5 )
print( 5**5 ) 
#Power Operator ( ** )
#Syntax of power( ** ) operator is ,
#base ** power
"""


#Comparision Operator -> >, <, >=, <=, ==, !=

#Input :- Numbers
#Output Data :- Boolean

# > or < --> Opening Side should be bigger and closing side should be smaller
#Bigger > Smaller -> True or Smaller < Bigger -> True
#otherwise, False

#eX:-
#5>2 -> True
#2>5 -> False

#>= or <=  --> ( Bigger>Smaller or Bigger = Smaller ) or ( Smaller<Bigger or Smaller = Bigger ) -> True
#otherwise, False

#Ex :-
#5>= 2 -> True
#5>5 -> False
#5>=5 -> True
#2<2 -> False
#2<=2 -> True
#2<=5 -> False

# == --> left_side_number should be equals to right_side_number
#EX :-
#2 == 2 -> True
#2 == 3 -> False
#3 == 2 -> False

# != --> left_side_number should not be equals to right_side_number( Opposite of == operator )
#EX :-
#2 != 2 -> False
#2 != 3 -> True
#3 != 2 -> True
"""
a = 5
b = 6
c = 5

print( f"a = { a }" )
print( f"b = { b }" )
print( f"c = { c }" )
print( f"a>b = { a>b }" )
print( f"b>a = { b>a }" )
print( f"a>c = { a>c }" )
print( f"a<c = { a<c }" )
print( f"b>c = { b>c }" )
print( f"b<c = { b<c }" )
print( f"a>=b = { a>=b }" )
print( f"a<=b = { a<=b }" )
print( f"a<=c = { a<=c }" )
print( f"a>=c = { a>=c }" )
print( f"b>=c = { b>=c }" )
print( f"b<=c = { b<=c }" )

print( f"a==b = { a==b }" )
print( f"a!= b = { a!= b }" ) 
print( f"a!=c = { a!=c }" )
print( f"a==c = { a==c }" )
print( f"b==c = { b==c }" )
print( f"b!=c = { b!=c }" )
"""

"""
#Logical Operator -> and , or

#Input :- Comaprisions/Boolean
#Output Data :- Boolean

#We Use Logical Operator only we have to combine more than one Comaprision statements.

a = 1
b = 2
c = 3


#print( ( a>b ) and (a>c) ),

#print( ?1 ), ?1 = ( a>b ) and (a>c) -> ?2 and ?3 ,?2 -> False, ?3 -> False
#?1 = False and False -> False
#print( False ) -> False

print( f"True and False = { True and False }" )
print( f"True and True = { True and True }" )
print( f"False and False = { False and False }" )
print( f"False and True = { False and True }" )
print( f"True or False = { True or False }" )
print( f"True or True = { True or True }" )
print( f"False or False = { False or False }" )
print( f"False or True = { False or True }" )
print( f"a = { a }" )
print( f"b = { b }" )
print( f"c = { c }" )
print( f"a>b  = { a>b  }, a>c = { a>c  }, ( a>b ) and (a>c) = { ( a>b ) and (a>c) }" )
print( f"( a>c ) and (a>b) = { ( a>c ) and (a>b) }" )
print( f"( b>a ) and (b>a) = { ( b>a ) and (b>a) }" )
print( f"( a>=b ) and (a>=c) = { ( a>=b ) and (a>=c) }" )
print( f"( a>b ) and (a<=c) = { ( a>b ) and (a<=c) }" )
print( f"( a>=b ) and (a>c) = { ( a>=b ) and (a>c) }" )
print( f"( a<=b ) and (a<=c) = { ( a<=b ) and (a<=c) }" )
print( f"( a==b ) and (a==c) = { ( a==b ) and (a==c) }" )
print( f"( a!=b ) and (a!=c) = { ( a!=b ) and (a!=c) }" )
print( f"( a!=b ) and (a==c) = { ( a!=b ) and (a==c) }" )
print( f"( a==b ) and (a!=c) = { ( a==b ) and (a!=c) }" )
print( f"( a<=b ) and (a<=c) = { ( a<=b ) and (a<=c) }" )
print( f"( a<=b ) and (a==c) = { ( a<=b ) and (a==c) }" )

print( f"( a>b ) = { a>b } or (a>c) = { a>c } -> { ( a>b ) or (a>c) }" )
print( f"( a>c ) or (a>b) = { ( a>c ) or (a>b) }" )
print( f"( b>a ) or (b>a) = { ( b>a ) or (b>a) }" )
print( f"( a>=b ) or (a>=c) = { ( a>=b ) or (a>=c) }" )
print( f"( a>b ) or (a<=c) = { ( a>b ) or (a<=c) }" )
print( f"( a>=b ) or (a>c) = { ( a>=b ) or (a>c) }" )
print( f"( a<=b ) or (a<=c) = { ( a<=b ) or (a<=c) }" )
print( f"( a==b ) or (a==c) = { ( a==b ) or (a==c) }" )
print( f"( a!=b ) or (a!=c) = { ( a!=b ) or (a!=c) }" )
print( f"( a!=b ) or (a==c) = { ( a!=b ) or (a==c) }" )
print( f"( a==b ) or (a!=c) = { ( a==b ) or (a!=c) }" )
print( f"( a<=b ) or (a<=c) = { ( a<=b ) or (a<=c) }" )
print( f"( a<=b ) or (a==c) = { ( a<=b ) or (a==c) }" )
"""


#Membership Operator -> in and not in.
#It is only applicable when we have a group or anydata type which follows indexing.
#indexing has been explained following,

name = "Hello, Buke and prashant"

#'H', 'e', 'l', 'l', 'o', ...
#'He', 'el', 'll', 'lo', ....
#'Hel', 'ell', ....
#index= 012345678910...
#bracket for indexing -> []

print( f"name = { name }" )
#print( name[ 4 ] )
#print( "Hello, Buke and prashant"[4] )
#print()
print( f" 'H' in name = { 'H' in name }" )
print( f"'He' in name = { 'He' in name }" )
print( f"'llo ' in name = { 'llo ' in name }" )
print( f" 'llo, ' in name = { 'llo, ' in name } " )
print( f"'llo ' not in name ={ 'llo ' not in name }" )
print( 'He' not in name )
print( ',' in name )
print( 'H,' not in name )
print( ' ' in name )
print( '.' in name )
print( ',' not in name )


#Indentity Operator

a = 2
b = 3
c = 2

print( f"a == b -> { a == b }" ) #Check by Value

print( f"id( -2 ) = { id( -2 ) }" )
print( f"id( -1 ) = { id( -1 ) }" )
print( f"id( 0 ) = { id( 0 ) }" )
print( f"id(1) = { id(1) }" )
print( f"id(2) = { id(2) }" )
print( f"id(3) = { id(3) }" )
print( f"a = { a }, b = { b } and c = { c }" )
print( f"id( a ) = { id( a ) }" )
print( f"id( b ) = { id( b ) }" )
print( f"id( c ) = { id( c ) }" )

print( f"id( a ) == id( b ) -> { id( a ) == id( b ) }" )    #Check by Memory Address
print( f"id( a ) == id( c ) -> { id( a ) == id( c ) }" )    #Check by Memory Address

print( f"a is b -> { a is b }" )  #Check by address
print( f"a is c -> { a is c }" )  #Check by address
print( f"b is c -> { b is c }" )  #Check by address
print()
print( f"a is not b -> { a is not b }" )
print( f"a is not c -> { a is not c }" )
print( f"b is not c -> { b is not c }" )


"""
#Bitwise Operator

print( f"bin( 20 ) = { bin( 20 ) }" )
print( f"bin( 25 ) = { bin( 25 ) }" )
print( f"bin( 23 ) = { bin( 23 ) }" )
print( f"bin( 16 ) = { bin( 16 ) }" )
print( f"bin( 79 ) = { bin( 79 ) }" )
print()
print( f"25&79 = { 25&79 }" )
print( f"25|79 = { 25|79 }" )
print()
print( f"20&16 = { 20&16 }" )
print( f"20|16 = { 20|16 }" )
print()
print( f"bin( 20 ) = { bin( 20 ) }" )
print( f"bin( 25 ) = { bin( 25 ) }" )
print( f"20&25 = {20&25}" )
print( f"20|25 = {20|25}" )
print( f"57&25 = {57&25}" )
print()
print( f"25 | 28 = {25 | 28}" )
print( f"25 | 57 = {25 | 57}" )
"""