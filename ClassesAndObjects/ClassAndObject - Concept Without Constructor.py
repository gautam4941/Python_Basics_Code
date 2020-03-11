class A:
    a = 9
    b = 2

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def add_data(self):
        self.c = int( input("Enter a number = ") )

ob1 = A()
ob2 = A()

#A.add( ob1, 2, 3 )
ob1.add( 2, 3 )

print( f"A.a = { A.a }" )
print( f"A.b = { A.b }" )
print( f"ob1.a = { ob1.a }" )
print( f"ob1.b = { ob1.b }" )
print( f"ob2.a = { ob2.a }" )
print( f"ob2.b = { ob2.b }" )
print()
ob1.add_data()
print( f"A.a = { A.a }" )
print( f"A.b = { A.b }" )
#print( f"A.c = { A.c }" )
print( f"ob1.a = { ob1.a }" )
print( f"ob1.b = { ob1.b }" )
print( f"ob1.c = { ob1.c }" )
print( f"ob2.a = { ob2.a }" )
print( f"ob2.b = { ob2.b }" )
print( f"ob2.c = { ob2.c }" )
