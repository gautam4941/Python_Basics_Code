def start():
    print( "Inside File 1 : start()" )
    a = int( input("Enter a number = ") )
    b = int( input("Enter another number = ") )

    print(f"Sum = {a+b}")

def f1():
    print( "This is f1" )

def f2():
    return "This is f2"


print( f1() )
print("f1 Done")
print( f2() )
print("f2 Done")
print( start() )
print("start Done")
