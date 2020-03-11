"""
#Abstract Class
class A:
    a = 6
    b = "Hello"

    def disp(self):
        pass

    def show(self):
        pass

    def __del__(self):
        pass

oba = A()
oba.disp()
oba.show()
"""


#Note :- if a class has 100% empty function then, only class is known as abstract class.
#In abstract class, variable are allowed.


class Shape:        #abstract class

    def disp1(self):        #abstract function
        pass

    def disp2(self):        #abstract function
        pass

class Circle:

    def disp1(self):
        print("This is Circle")

    def disp2(self):
        print("This is Disp2 of Class Circle")

class Rectangle:

    def disp1(self):
        print("This is Rectangle")

    def disp2(self):
        print("This is Disp2 of Class rectangle")

obs = Shape()
obc = Circle()
obr = Rectangle()

print( f"obs.disp1() = { obs.disp1() }" )
print( f"obc.disp1() = { obc.disp1() }" )
print( f"obr.disp1() = { obr.disp1() }" )
print()
print( f"obs.disp2() = { obs.disp2() }" )
print( f"obc.disp2() = { obc.disp2() }" )
print( f"obr.disp2() = { obr.disp2() }" )