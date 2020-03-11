from functools import reduce

"""
#Zip Func()

print("This is Zip Function,")

l1 = [2, 3, 4, 5, 6, 7]
l2 = ['Ram', 'Shyam', 'Mohan', 'Ritu','ABC']
l3 = ['1BM14CS049', '1BM14CS050', '1BM14CS051', '1BM14CS052']

print( f"zip( l1, l2, l3 ) = { zip( l1, l2, l3 ) }" )
print( f"tuple( zip( l1, l2, l3 ) ) = { tuple( zip( l1, l2, l3 ) ) }" )
print( f"list( zip( l1, l2, l3 ) ) = { list( zip( l1, l2, l3 ) ) }" )
"""

"""
#Map Func() without lambda func.


# Traditional

def power( num ):
    return  num**2

l1 = [1, 2, 3, 4, 5, 6]

for i in l1:
    print( f"power( i ) = { power( i ) }" )

print()
print("This is Map Function,")

def power( num ):
    #print( f"Inside Function num**2 = { num**2 }" )
    return  num**2

l1 = [1, 2, 3, 4, 5, 6]

print( f"map( power, l1 ) = { map( power, l1 ) }" )
print( f"list( map( power, l1 ) ) = { list( map( power, l1 ) ) }" )   #typecasting into list and tuple


#Map  = for i in l:
            #function( i )
"""

"""
#Map Func() with lambda func.
print( "\nLambda Function", end = '  ' )
l1 = [1, 2, 3, 4, 5, 6]

print( list( map( lambda num : num**2 , l1 ) ) )
"""

"""
#Reduce Func() without lambda funcs

l1 = [1, 2, 3, 4, 5, 6]

print("This is Reduce Function,")

def add(num1, num2):
    print(f"Inside add(), num1 = { num1 } and num2 = { num2 } and num1+num2 = { num1 + num2 }")
    return num1 + num2

print( f"reduce( add, l1 ) = { reduce( add, l1 ) }" )

#Reduce Func() with lambda func.

print( f"reduce( lambda num1, num2 : (num1+ num2), l1 ) = { reduce( lambda num1, num2 : (num1+ num2), l1 ) }" )
"""

"""
#filter func() without lambda func.

l1 = [1, 2, 3, 4, 5, 6]

def oddeven( num ):
    print( f"Inside oddeven(), num = { num }" )
    return num%2 == 0

print( f"filter( oddeven, l1 ) = { filter( oddeven, l1 ) }" )
print( f"tuple( filter( oddeven, l1 ) ) = { tuple( filter( oddeven, l1 ) ) }" )
print( f"list( filter( oddeven, l1 ) ) = { list( filter( oddeven, l1 ) ) }" )
#filter func() with lambda func.

print(f"Filter lambda Function for odd = {tuple( filter( lambda num : num%2 == 1, l1 ) ) }" )
"""

"""
#*args and **kwargs

def func(a, *args, **kwargs):
    print( f"args = {args}" )
    print( f"kwargs = {kwargs}" )
    sum = 0

    for i in args:
        sum = sum + i

    for i, j in kwargs.items():
        print(f"{i} = {j}")
        sum = sum + j

    print(f"Sum = {sum}")

#Only Value( 6, 7 ) will go to args and key1 = value1, key2 = value2( b = 9, c = 0 ) will go to Kwargs
func( 5, 6, 7, b = 9, c = 0 )
"""

"""
def f1( func ):
    print( "Inside F1" )
    if( func != None ):
        func()
    else:
        print( "func is None" )

def f2():
    print( "Inside F2" )


'''
Note :- #f1( f3 ) is same as 
    @f1
    def f3()
'''

@f1
@f1
@f1
def f3():
    print( "Inside f3" )

#f1( f3 )

def f4():
    print("Inside f4")

print()
f1(f4)
"""

"""
#iterator

l1 = [1, 2, 3, 4, 5, 6]

temp = iter( l1 )
print( f" temp of iter = {temp} " )

print( f"1. next( temp ) = { next( temp ) }" )
print( f"2. next( temp ) = { next( temp ) }" )
print( f"3 next( temp ) = { next( temp ) }" )
print( f"4. next( temp ) = { next( temp ) }" )
print( f"5. next( temp ) = { next( temp ) }" )
print( f"6. next( temp ) = { next( temp ) }" )
#print( f"7. next( temp ) = { next( temp ) }" )

print()
temp = iter( l1 )

for i in range( len(l1) ):
    print( f"next( temp ) = { next( temp ) }" )
"""

#generators

def nums( n ):
    print( "Inside Nums Function" )
    for i in range(1, n+1):
        yield (i)

numbers = nums(5)      #we are storing generator object in numbers variable

print( f"type(numbers) = { type(numbers) }" )
print( f"numbers = { numbers }" )

print( f"list( numbers ) = { list( numbers ) }" )