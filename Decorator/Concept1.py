def deco( func ):
    print("We are using decorator")

    def returnfunc():
        func()

    return returnfunc

@deco
def func1():
    print("This is func1")

@deco
def func2():
    print("This is func2")

print("Calling func1() = ", end= '' )
func1()
#1) deco( func1() )   #Passing function variable as parameter

#2) After @deco symbol, decorated functions will get called automatically.
print()
deco( func1 )()
deco( func2 )