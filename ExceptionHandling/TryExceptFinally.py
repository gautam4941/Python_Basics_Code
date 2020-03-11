"""
a = 5
print( b )
"""

"""
try:
    a = 5
    print( "Inside Try" )
    prin( f"a = {a}" )

except:
    print("Error Occured")
    b = 6
    print(b)

finally:
    print("This is Finally Block")
"""

"""
try:
#    import numpy1
    a = 5
    print( f"a = {a}" )
#    print( b )
    print(f"a = {a}")
    d = { 'a' : 1 }
    print( d['b'] )

except ModuleNotFoundError:
    print("We got a Module Not Found Error")

except NameError:
    print("We got a Name Error")

except:
    print("Error Occured")

finally:
    print("This is Finally Block")
"""


try:
    #import nummy
#    print(b)
    a = int( input("Enter one number = ") )
    b = int( input("Enter second number = ") )

#    raise Exception( f"raise : a -> {a} is greater than b -> {b}" )

    assert a>b, Exception("Assert Error Occured")

#    Note :- assert will work when condition will become false.
            #Whereas, raise doesn't need any condition.

except ModuleNotFoundError :
    print( f"Module Error Occured " )

except Exception as pqrs :
    print( f"Exception Occured = { pqrs }" )