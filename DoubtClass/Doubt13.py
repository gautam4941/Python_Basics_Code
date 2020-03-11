x = 8

def add(a, b):
    print(f"This is add, a = {a} and b = { b }")
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

b = int(input("Enter the value of b = "))

print("Hello")
a = b+2
print(f"a = {a}")

print( f"Sum = { add(a, b) }" )
print( sub( a, b ) )