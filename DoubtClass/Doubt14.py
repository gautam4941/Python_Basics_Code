class A:

    a = 5
    b = 2

    def calc(self):
        print("This Calc is Of Class A")
        try:
            print( self.a/0 )

        except:
            print("Error For Divisibility By 0")

        finally:
            print("Exception Occured")

        print("Hello")

    def disp(self):
        print("This is Class A DISP")

class B( A ):

    def calc(self):
        print("This Calc is Of Class B")
        super().calc()

    def disp(self):
        print("This is CLass B DISP")

obb = B()

obb.disp()
print()
obb.calc()