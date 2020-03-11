class A:
    def add(self):
        print( "Class A -> add() " )

    def sub(self):
        print( "Class A -> sub() " )


class B:
    def add(self):
        print("Class B -> add() ")

    def mult(self):
        print("Class B -> mult() ")


class C( A, B ):
    def div(self):
        print("Class C -> div() ")

obc = C()
obc.add()
obc.mult()
obc.sub()