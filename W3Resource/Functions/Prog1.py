#1. Write a Python function to find the Max of three numbers.

def maxof3( a, b, c ):

    if( a > b ):

        if( a > c ):
            #print( f"{a} is greater than {b} and {c}" )
            return a
        else:
            #print(f"{c} is greater than {a} and {b}")
            return c

    else:
        if( b > c ):
            #print(f"{b} is greater than {a} and {c}")
            return b
        else:
            #print(f"{c} is greater than {a} and {b}")
            return c

a = int( input("Enter 1st number = ") )
b = int( input("Enter 2nd number = ") )
c = int( input("Enter 3rd number = ") )

a = ( (a + 5) * 8 )/2
b = ( (b + 5) * 8 )/2
c = ( (c + 5) * 8 )/2

print( f"a = { a }, b = { b } and c = { c }" )

max = maxof3(a, b, c )

print( f"Max = { max }" )

def increment( a ):
    return a+10

max = increment( max )
print( f"Max = { max }" )