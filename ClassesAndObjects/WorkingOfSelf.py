class A:
    x = 6
    y = 12

    def __init__(self):
        print(f"Constructor Addition = {self.x + self.y}" )

    def xyz(self):
        print( self )
        print(f"self.x = {self.x}")
        print( f"self.y = {self.y}" )
        print(f"Sum = { self.x + self.y }")
        print(f"Sub = {self.x - self.y}")
        print(f"Mult = {self.x * self.y}")
        print(f"Div = {self.x / self.y}")

    def __del__(self):
        print(f"Object Has been Deleted = { self }")

ob1 = A()
ob2 = A()

ob1.x = 15
ob2.y = 20

ob1.xyz()

print()
ob2.xyz()

'''
print( f"ob1.x = {ob1.x}" )
print( f"ob1.y = {ob1.y}" )

print( f"ob2.x = {ob2.x}" )
print( f"ob2.y = {ob2.y}" )
print()
ob1.x = 16
ob2.x = 20

print( f"ob1.x = {ob1.x}" )
print( f"ob1.y = {ob1.y}" )

print( f"ob2.x = {ob2.x}" )
print( f"ob2.y = {ob2.y}" )
'''