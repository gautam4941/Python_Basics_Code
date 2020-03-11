#Constructor Basic Programs,

class A:
    a = 6
    b = 10

    def __init__(self):
        print(f"This is Class A Constructor and Object Detail = { self }")
        self.c = 20             #Object Variable

    def disp(self):
        print(f"self.a = {self.a}")
        print( f"self.b = { self.b }" )

    def __del__(self):
        print(f"This is Class A Destructor and Object Detail = {self}")

ob1 = A()
ob2 = A()
print()
ob1.__del__()
print()
del ob1
print()
ob1.__del__()
ob3 = A()

# ob1 Const
# ob2 Const
# ob1 dest
# ob3 const
# ob2 dest
# ob3 dest