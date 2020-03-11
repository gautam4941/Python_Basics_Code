#Nested Function and passing Function with return

def func():                     #Nested Function
    x = int(input("Enter x value = "))                         #5
    y = int(input("Enter y value = "))                   #6

    def mult(a, b):     #Inner Function_1
        print("Inside mult Function")
        return (a * b)

    def div(a, b):     #Inner Function_2
        print("Inside divide Function")
        print(a // b)

    def add(a, b):     #Inner Function_3
        print("Inside add Function")
        return (a + b)

    def sub(a, b):     #Inner Function_4
        print( "Inside Subtract Function" )
        return (a - b)

    print( f"mult(x, y) = { mult(x, y)}")          #mult( 5, 6 ) -> return 30
    print(f"div(x, y) = {div(x, y)}")              #div( 5, 6 ) -> return 0
    print(f"add(x, y) = {add(x, y)}")              #add( 5, 6 ) -> return 11
    print(f"sub(x, y) = {sub(x, y)}")              #sub( 5, 6 ) -> return -1

    return sub, mult, div

p, q, r = func()    #p = sub, q = mult, r = div
print(f"p = {p}")
print( f"type(p) = {type(p)}" )
"""
p -> 
def p(a, b):
    print( "Inside Subtract Function" )
            return (a - b)
"""

print( f"p = { p(2, 3) } ")               #p( 2, 3 ) => mult(2, 3)
print()
print()
print(f"q = { q }")
print( f"type( q ) = {type( q )}" )
                            #print(f"a = {a}")

"""
q -> 
def q(a, b):     #Inner Function_1
    print("Inside mult Function")
    return (a * b)
"""
print( f"q = { q( 2, 3 ) } ")               #p( 2, 3 ) => mult(2, 3)


print(f"r = { r }")
print( f"type(r) = {type( r )}" )

"""
r -> 
def r(a, b):
    print("Inside divide Function")
    print(a // b)
"""

print( f"r = { r( 2, 3 ) } ")               #p( 2, 3 ) => mult(2, 3)
