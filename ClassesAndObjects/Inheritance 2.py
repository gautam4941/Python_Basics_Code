class A:

    def __init__(self):
        print("This is Class A constructor")

    def add(self, x, y):
        print(f"x+y = {x+y}")

    def disp(self):
        print("This is Disp of class A")

    def __del__(self):
        print("This is destructor of Class A")


#Note :- Syntax to User Super()

#super().add()


class B( A ):

    def __init__(self):
        print("This Constructor of Class B")

    def add(self, a, b, c):
 #      print(f"This add is of Class A = { super().add() } ")
        print(f"This is add of class B = { a+b+c }")
        super().add(a, b)

    def __del__(self):
        super().__del__()
        print("This is Class B Destructor")


obb = B()
print()
obb.add( 2, 3, 4 )
print()
obb.disp()
print()