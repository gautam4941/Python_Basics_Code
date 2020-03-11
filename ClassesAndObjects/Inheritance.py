class A:
    a = 5
    b = 2

    def __init__(self):
        print("This is Class A constructor")

    def add(self):
        print("class A -> Add")

    def disp(self):
        print("This is Disp of class A")

    def __del__(self):
        print("This is destructor of Class A")

class B( A ):

    def add(self):
        print("This is Add of class B")

    def sub(self):
        print( "Inside Sub of class B" )

    def a_add(self):
        print(f"This add is of Class A inside B = {super().add()} ")    #A.add()

    def __del__(self):
        print( "INSIDE CLASS B - DESTRUCTOR" )


oba = A()
print( f"oba.a = { oba.a }" )
print( f"oba.b = { oba.b }" )
print( f"oba.__init__() = { oba.__init__() }" )
print( f"oba.add() = { oba.add() }" )
print( f"oba.disp() = { oba.disp() }" )
print( f"oba.__del__() = { oba.__del__() }" )
print()
print()

obb = B()
print( f"obb.a = { obb.a }" )
print( f"obb.b = { obb.b }" )
print( f"obb.__init__() = { obb.__init__() }" )
print( f"obb.add() = { obb.add() }" )
print( f"obb.disp() = { obb.disp() }" )
print( f"obb.__del__() = { obb.__del__() }" )
obb.a_add()