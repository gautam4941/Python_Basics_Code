'''
def deco( func ):   #function1, function2, func3

    print("This is Deco")
    func()

    return str

@deco
def function1():
    print("Hello")
    print("Func 1")

@deco
def function2():
    print("Func 2")

def function3():
    pass

deco( function3 )   #Last Priority.
'''

def deco( func ):       # func1, func2, func3
    print("This is decorator")

    def returnfunc():
        print("This is return func")
        func()

    return returnfunc
@deco
def func1():
    print("Func1")

@deco
def func2():
    print("Func2")

def func3():
    print("func3")

deco( func3 )()