'''
a = 1

def func():
    a = 5
    b = 2

    print(f"a inside Func = {a}")
    print(f"b inside Func = {b}\n")

print(f"a outside Func() = {a}\n")
#print(f"b outside Func() = {b}")
func()
print(f"a outside Func() = {a}")
'''
'''
a = 2

def f1():
    a = 5
    print(f"a inside f1 = {a}")

def f2():
    b = 6
    print(f"b inside f2 = {b}")
    print(f"a inside f2 = {a}")

print(f"A Before Calling F1 = {a}")
f1()
f2()
'''
"""
a = 1

if( a == 1 ):

    print(f"a when a = 1 -> {a}")
    b = 6

    if( b == 6):
        print(f"b when b = 6 -> {b}")

        c = 9

        print(f"c when b = 6 -> {c}")

    print(f"c when outside of b -> {c}")

print( f"a = {a}" )
print( f"b = {b}" )
print( f"c = {c}" )
"""
"""
a = 1

for i in range( 0, 5 ):
    b = 6
    print(b)
    for j in range( 0, 3 ):
        c = 1
        print(c, end = ', ')

print(f"\na  = {a}")
print(f"b = {b}")
print(f"c = {c}")

#Note :- Local And Global Scope is only applicable to functions and Classes
"""
"""
In Function and Classes. If we create any variable then,
Then, those Variable follows Local- Global Rule with respect to the
Level.

But, Other than Funtions and classes. If we create any variable then,
Those variable are by default Global.
"""