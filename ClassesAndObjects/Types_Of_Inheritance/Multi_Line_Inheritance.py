class A:
    a = 5
    b = 2

    def add(self):
        print("class A -> Add")

class B( A ):
    def add(self):
        print("class B -> Add")

    def super_add(self):
        print( "Class B -> Super_add() " )
        super().add()

    def sub(self):
        print( "class B -> Sub" )

class C( B ):

    def add(self):
        print("class C -> Add")

    def super_add(self):
        print( "Class C -> Super_add() " )
        super().super_add()

    def super_sub(self):
        print( "Class C -> Super_sub() " )
        super().sub()

    def sub(self):
        print( "class C -> Sub" )

obc = C()

obc.super_add()
obc.super_sub()