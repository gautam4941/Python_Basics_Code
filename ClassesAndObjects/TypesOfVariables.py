class A:
    a = 1                       #class_variable

    def __init__(self):
        self.b = 2              #Instance/Object Variable

    def show(self):
        print( f"A.a = { A.a }" )
        print(f"self.a = {self.a}")
        #print( f"A.b = { A.b }" )         #Error because, It is not class variable
        print( f"self.b = { self.b }" )    #This will work as this is object variable

ob1 = A()
ob1.show()
