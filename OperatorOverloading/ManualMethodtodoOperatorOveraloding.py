class A:

    def __init__(self, num1):
        self.num1 = num1

    def add(self, other1, other2 ):
        print( other1.num1 + other2.num1 )

    def sub(self, other1, other2 ):
        print( other1.num1 - other2.num1 )

ob1 = A(2)
ob2 = A(5)

ob3 = A( 0 )
ob3.add( ob1, ob2 )
ob3.sub( ob1, ob2 )