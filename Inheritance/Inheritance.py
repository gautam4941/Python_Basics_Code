class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x+self.y

    def sub(self):
        return self.x-self.y
    
    def mult( self):
        return self.x*self.y

    def div(self):
        return self.x//self.y

class B( A ):
    def __init__(self, x, y):
        A.__init__(self, x, y)
        
    def checkoddeven( self, x ):
        if(x%2 == 0):
            print(f"{x} is even")
        else:
            print(f"{x} is odd")

class C(B):

    def disp(self):
        print("This is Disp Function")

obb = C(2, 3)

print(f"Add is = {obb.add() } " )
print(f"Sub is = {obb.sub() } " )
print(f"Mult is = {obb.mult() } " )
print(f"Div is = {obb.div() } " )

print(obb.x)
print(obb.y)

obb.checkoddeven( obb.y )
obb.disp()
