class A:
    def __init__(self):  #Constructor, It will get called automatically when object gets construct.
        print(f"This is default Constructor and Object Detail = { self }")

    def disp(self):
        print(f"This is Disp and Object Detail = { self }")

    def message(self):
        print("This is message")

    def __del__(self):  #destructor, It will get called automatically when object gets destruct.
        print(f"This is Destructor and Object Detail = { self }")

obj1 = A()
print()
obj1.disp()
print()
obj2 = A()
print()
del obj1
print()
obj2.disp()
obj1.message()    #It will give Error.