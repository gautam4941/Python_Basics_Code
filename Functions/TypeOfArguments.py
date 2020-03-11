#1) Required argument,

def func( a, b ):       #Recieving argument = Formal Parameter
    print("Required Argument")
    print(a+b)

#func(2 ) #Sending argument = Actual Parameter

#func( 2, 3 )

#func( 2, 3, 4 )

#No of sending argument( AP ) = No of recieving argument( FP ) -> Function will be executed

#if, #No of sending argument( AP ) > No of recieving argument( FP ) -> Error

#if, #No of sending argument( AP ) < No of recieving argument( FP ) -> Error


"""
#2) Keyword Argument

def func( a, b ):
    print("Keyword Argument")
    print(f"a = {a} and b = {b}")
    a = a+2
    b = b*4
    print(f"a = {a} and b = {b}")
    print(a+b)

func( 2, 3 )
print()
func( 3, 2 )
print()
func( b = 3, a = 2 )   #We are giving keyword at Actual Parameter Side.
print()
func( 2, b = 3 )
#Merit :- We can give and change the position of our Recieving parameter at Sending
#Side( Actual Parameter )while sending values/varible

#De-Merit :- We can not give the name of few parameters and leave other prameters.
#We will have to give all the names of recieving parameter. Even if we have to write
# the name only for one argument.
"""

"""
#3) Default Parameter

#a = -5
#print(f"A value is  = {a}")

#a = 10
#print(f"A value is  = {a}")

def func( a = 2, b = 3 ):
    print(f"a = {a}")
    print(f"b = {b}")
    print(a+b)
    print()

func( 7, 1 )
func(7)
func( b = 7 )
func( b = 7, a = 8 )
func()


#Merit :- Even if we don't send arguments from sending side( Main to Function ), default values works.
#and If we send argument value then, Argument value will get updated.

#De-Merit :- We can not give the name of few variable and leave other variable.
#We will have to give all the values to all recieving parameter( Main to Function ).
# Even if we want to give the value to only for one argument.
"""

#4) Variable Length Argument

def func( a, b = 5 , *c, d = 0 ):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")
    print(f"type(a) = { type(a) } ")
    print(f"type(b) = {type(b)} ")
    print(f"type(c) = {type(c)} ")
    print(f"type(d) = {type(d)} ")


func( 2, 6, 8, d = 9 )
func( 2, 6, 8, 7, d = 19)
func( 2, 6, 8, 7, 'Raj', True, [ 2, 6, 7], 3.6, d = 9)
func( 2 )
func( d = 6, a = 2 )


"""
def func( a, b, *x, d = 0, **c ):
    print(f"a = {a}")
    print(f"b = {b}")
    print( f"x = { x }" )
    print(f"c = { c }")
    print(f"d = { d }")

    print(f"type(a) = { type(a) } ")
    print(f"type(b) = {type(b)} ")
    print(f"type(x) = {type(x)} ")
    print(f"type( c ) = {type( c )} ")
    print(f"type( d ) = {type( d )} ")

#func( a, b, *x, name, **c )   -> Formal Parameters

func( a = 'Mango', b = 2.5 )
print()
func( 'Mango', 2.5, 'Ram', 45, 25000, d = 21, salary = 15000 )
print()
func( a = 'Mango', b = 2.5, name = 'Ram', id = 45, salary = 25000 )
"""

"""
def func( a, b, *args, d, **kwargs ):

    print(f"a = {a} and type(a) = { type(a) }")
    print(f"b = {b} and type(b) = { type(b) }")
    print(f"args = {args} and type(args) = { type(args) }")
    print(f"kwargs = {kwargs} and type(kwargs) = { type(kwargs) }")
    print()


func( 1, 7, 2, 0, 9, 6, f = 3, g = 10 )
func( 1, 7, 2, 0, 9, 6, 5, 9, f = 3, g = 10 )


# Note :- *args accepts values 0 or more. **kwargs accepts values in the form
# of key value pair. It look like keyword Argument but It Doesn't behave like
# keyword Arguments because, those Actual arguments are not formal argument.
#
# We always write **kwargs at the last. Otherwise, It Gives Error.
# We can write *args anywhere but it will accept only values.
"""

"""
def func( a, b, *args, d = 0 ,e = 0, **kwargs ):

    print(f"a = {a} and type(a) = { type(a) }")
    print(f"b = {b} and type(b) = { type(b) }")
    print(f"args = {args} and type(args) = { type(args) }")
    print(f"d = {d} and type(d) = { type(d) }")
    print(f"e = {e} and type(e) = { type(e) }")
    print(f"kwargs = {kwargs} and type(kwargs) = { type(kwargs) }")

    sum = a + b

    for i in args:
        sum = sum + i

    sum = sum + d + e

    for i in kwargs.keys():         # i = 'f', 'g'
        sum = sum + kwargs[i]              #kwargs[ 'f' ], kwargs['g']

    print(f"Sum = {sum}")

#func( a, b, *args, d = 0 ,e = 0, **kwargs )
func( 1, 7, 2, 0, 9, 6, 5, 9, f = 3, g = 10 )
print()
func( 1, 7, 2, 0, 9, 6, d = 5, e = 9, f = 3, g = 10 )
"""