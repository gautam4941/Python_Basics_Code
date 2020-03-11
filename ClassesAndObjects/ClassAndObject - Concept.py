"""
class Original:
    x = 6
    y = 8

    def add(self, a, b):
        print( "Inside ADD Function -----------------" )
        print( f"self = { self }, a = { a }, b = { b }" )
        return a + b

    def sub(self, a, b):
        print("Inside SUB Function------------------------")
        print(f"a = {a} and b = {b}")
        print(f"a - b = {a - b}")
        print("Leaving SUB Function----------------------------")
        print()

    def mult(self, a, b):
        print("Inside MULT Function------------------------")
        print(f"Arg. a = {a}")
        print(f"Arg. b = {b}")
        print("OUTSIDE MULT Function------------------------")

        return a * b



print( f"Class Add = { Original.add(  Original, 2, 6 ) }" )

obj1 = Original()

print( f"Object add() = { Original.add( obj1, 6, 7 ) }")
print()
print()
print( f"2nd time calling add() = { obj1.add( 8, 9 ) }" )
"""

"""
class ArithmeticOperator:
    x = 8                       #Class Variable
    b = 19                      #Class Variable

    def add(self, a, b):
        print("This is add")
        return a + b

    def change( self ):  # def change( ob1 )
        print( "Inside CHANGE fucntion--------------------------" )
        self.x = self.x + int( input("Enter a number = ") )

        print("Leaving CHANGE fucntion--------------------------")

    def add_variables(self):
        print( f"self = { self }" )
        self.y = int( input("Enter the number for y = ") )

    def sub(self, a, b):
        print( "Inside SUB Function------------------------" )
        print( f"self = { self } and a = { a } and b = { b }" )
        self.new_val = b               #ob2.new_val = 5
        print( f"a - b = { a - b }" )
        print( "Leaving SUB Function----------------------------" )
        print()

    def mult(self, a, b):
        print( "Inside MULT Function------------------------" )
        print( f"self = { self }" )
        print( f"Arg. a = {a}" )
        print( f"Arg. b = {b}" )
        print(f"self.a = {self.a}")
        print(f"self.b = {self.b}")
        print( "OUTSIDE MULT Function------------------------" )

        return a * b


ob1 = ArithmeticOperator()
ob2 = ArithmeticOperator()

#print( f"Outside 1 ob1.new_val = { ob1.new_val }" )
ob1.sub(2, 3)
print( f"Outside ob1.new_val = { ob1.new_val }" )
ob2.sub(5, 10)
print( f"Outside ob2.new_val = { ob2.new_val }" )
print()
ob1.change()
print( f"OutSide, ob1.x = { ob1.x }" )
print( f"OutSide, ob2.x = { ob2.x }" )
"""