class A:

    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, other):
        return self.num1 + other.num1

    def __sub__(self, other):
        return self.num1 - other.num1

ob1 = A(2)
ob2 = A(5)

print( ob1 + ob2 )
print( ob1 - ob2 )