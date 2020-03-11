'''
#Errors :- Errors is something which can terminate the programs in mid of statements because, incorrect ways of writing
#            the statements.

#There are 2 types of Errors,
#1) Syntax  Error
#2) Logical Error,

#Ex :- print(1/0), import nummy

#Exception Handling = Exception is the event when error occurs.
#                       Exception Handling is The way of handling the Exception.


try :
    print( 1 )
    print( 2+ 3 )
    print( 1/0 )            #Error Occured
    print("Hello")          #Statement couldn't executed
    print("Hi")             #Statement couldn't executed

except:
    print("Error Occcured")

finally:
    print("Hello, Gautam")
    print("Hi, Prasant")
'''

d = { 'a' : 1, 'b' : 2, 'c' : 3, 'e' : 4 }

try:
#    import nummy           #Import Error
#    print( d['z'] )        #KeyError
#    print(c)                # Name Error

    a= int( input("Enter the value of a = ") )
    x = int( input("Enter the value of x = ") )

#    assert a>x, "Hello, I am assert Exception"     #asset will work when condition is false.

#raise

#Syntax :- raise Exception( Message )

    if( a<x ):
        raise Exception("Hello, I am Raise Exception")
#    b="hello how are you"
#    print( a+b )            #Type Error

#    print(a/0)              #Zero Division Error
#    print( int(b) )


except IOError:         #This Error Occurs while opening any file which is not present at that path
    print("This is IOError")

except ImportError:
    print("This is Import Error")

except KeyError:
    print("This is Key Error")

except TypeError:
    print("This is Type Error")

except ZeroDivisionError:
    print("This is Zero Division Error")

except ValueError:
    print("This is Value Error")

except :
    print( "Default Except Block" )

finally:
    print("Finally Block - Your Code Executed Properly")

print("Hello")
