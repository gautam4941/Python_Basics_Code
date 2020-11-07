class A:
    a = 5
    b = 6

    def __add__(self, data):
        print( "Inside __add__()" )
        print( f"self = { self } and data = { data }" )
        return self.a + data

    def __sub__(self, other):
        print("Inside __sub__()")
        print(f"self = {self} and other = { other }")
        return self.a - other

ob1 = A()
ob2 = A()

print( f"ob1.a = { ob1.a } and ob2.a = { ob2.a }\n" )

print( ob1 + 2 )        #__add__( self, data ) -> __add__( ob1, 2 ) -> ob1.a( int ) + 2( int )
print()
print( ob1 - 2 )        #__sub__( self, data ) -> __sub__( ob1, 2 ) -> ob1.a( int ) - 2( int )