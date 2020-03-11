class A:
    def add(self):
        print( "Class A -> add() " )

    def sub(self):
        print( "Class A -> sub() " )


class B(A):
    def add(self):
        print("Class B -> add() ")

    def mult(self):
        print("Class B -> mult() ")


class C( A ):
    def sub(self):
        print( "Class C -> sub()" )

    def div(self):
        print("Class C -> div() ")

obb = B()
obc = C()

obb.add()
obb.mult()
obb.sub()
print()
obc.sub()
obc.div()
obc.add()