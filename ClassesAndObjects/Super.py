#Note :- Syntax to User Super()

#ob1.add()
#super().add()

class A:

    def __init__(self):
        print("This is A")

    def disp(self):
        print("Disp of Class A")

class B:

    def __init__(self):
        print("This is B")

    def disp(self):
        print("Disp of class B")

class C(B, A):

    def __init__(self):
        super().__init__()
        print("This is C")
        super().disp()

    def show(self):
        print("Hi")

obc = C()