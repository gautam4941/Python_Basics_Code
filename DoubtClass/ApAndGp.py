print("Welcome to AP Programs,")

a = int( input("Enter the First Number = ") )
n = int( input("Number of n =") )
d = int( input("Enter the Value of d = ") )

t = a + ( n - 1 ) * d

print(f"( n - 1 ) = { ( n - 1 ) }")
print(f"( n - 1 ) * d = {( n - 1 ) * d}")
print( f"t = {t}\n" )

sum = ( (a+t) * n ) / 2

print(f"a+t = {a+t}")
print(f"(a+t) * n = {(a+t) * n}")
print( f"Sum from {a} to {t} with Diffrence of {d} = {sum}" )