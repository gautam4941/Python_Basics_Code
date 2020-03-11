"""
n = int( input("Enter the no of times = ") )  #3

for i in range( 0, n ):             #0, .., 2
    a = int( input("Enter a number = ") )

    if( a%2 == 0 ):
        print(f"{ a } is Even")

    else:
        print(f"{a} is Odd")


m = int( input("Enter the no of times = ") )    #5

for i in range( 0, m ):  #0 , .. , 4
    a = int( input("Enter a number = ") )   #3, 8
    print( f"a = { a } and a+2 = { a+2 }" )

"""

"""
Problem with the Loops, If we want to execute the Odd even program loop then, forcefully python is
    executing the 2nd program. 
    
    Same issue is with 2nd program( If we want to execute 2nd program then, Forcefully python is 
     executing the 1st one( Odd/Even ) program ).
     
Sol :- Make 1st Prog comment and run 2nd one or make 2nd one comment and run 1st one.

Drawback of above given solution,
    It's not a easy task to comment/Uncomment every time to some block of code.
    
Actual Solution : - Functions
"""

"""
def a():
    print("Inside a Function")
    n = int( input("Enter the no of times = ") )

    for i in range( 0, n ):
        a = int( input("Enter a number = ") )
    
        if( a%2 == 0 ):
            print(f"{ a } is Even")
    
        else:
            print(f"{a} is Odd")

def b():
    print("Inside b Function")
    m = int( input("Enter the no of time = ") )    #5

    for i in range( 0, m ):                         #0, .., 4
        a = int( input("Enter a number = ") )   #3, 8
        print( f"a = { a }, i = { i } and a+i = { a+i }" )
    

print("Calling b function 1st time,")
b()
print()
print("Calling b function 2nd time,")
b()
print()
print( "Calling a function 1st time," )
a()
"""


"""
a = 5

What is a ?
-> a is a variable which is holding value

def a():
    print("Hello")

-> a is a variable which is holding multiple/Single statement and the variable which holds
    statements inside it is known as Function.
    
    Ex :- a is holding print("Hello")
        Whenever we write a() then, print( "Hello" ) will be executed and output will be Hello
        So, print("Hello") is a statement. Thus, we can say that a is a function.
"""

"""
Function

i) Function defintion/Creation

Def :- It is a variable which has capability to hold multiple
       Statements .

In Java, we declare function like this,

string f_name()
{
    System.out.print("Hello")
    System.out.print("Hi")
}
#In Python, we declare function like this,
def function_name():
    print( "Hello" )
    print('Hi')

ii) Function calling

#Java,
function_name()

#Python,
function_name()


#we can do the same work with the help of loop but,
#if we have satements to be categorized then, we use functions
"""

'''
d1 = 0
d2 = 0

for i in range( 1, 3 ):
    a1 = 1
    a2 = 5
    print( f"d1 = {d1}" )
    print(f"d2 = {d2}")
    d1 = int(input("Enter d1 value = "))
    d2 = int(input("Enter d2 value = "))

    print(f"a1->{a1} + a2->{a2} = { a1 + a2 }")
    print(f"d1->{d1} + d2->{d2} = { d1 + d2 }")
    print(f"d1->{d1} * d2->{d2} = { d1 * d2 }")
    print(f"d1->{d1} / d2->{d2} = { d1 / d2 }")

'''

'''
def initialize():
    a1 = 1
    a2 = 5
    d1 = int(input("Enter d1 value = "))
    d2 = int(input("Enter d2 value = "))

    print(f"a1->{a1} + a2->{a2} = {a1 + a2}")
    print(f"d1->{d1} + d2->{d2} = {d1 + d2}")
    print(f"d1->{d1} * d2->{d2} = {d1 * d2}")
    print(f"d1->{d1} / d2->{d2} = {d1 / d2}")

initialize()
'''

"""
Type of Functions,

1) #No Agurement/Parameter and no return,

Gautam called Prashant at his place.
Gautam didn't tell anything to prashant.
Prashant came and Made the bottle and he took the bottle with him.

Here, Gautam is not giving any Information/Data/Argument to Prashant(Function).
Our Function i.e., Prashant is doing some task.
#and then, Prashant is not giving bottle to Gautam. It means, Prsahant( our Function )
is not returning any thing.
"""

"""
#No Agurement/Parameter and no return,

def func():

    a1 = int( input("Enter 1st number = ") )
    a2 = int(input("Enter 2nd number = "))

    print(f"{a1} + {a2} = {a1+a2}")

func()
"""

#Dis Advantage :- We can't Give our Values. Inside Function only we
#will have consider some values and then, perform any task.


"""
#2) Agurement/Parameter and no return,

Gautam called Prashant at his place.
Gautam told some work( To make Chair ) to prashant.
Prashant came and Made the chair and he took the chair with him.

Here, Gautam is giving Information/Data/Argument to Prashant(Function).
Our Function i.e., Prashant is doing some task.
#and then, Prashant is not giving chair to Gautam. It means, Prsahant( our Function )
is not returning any thing.

#Agurement/Parameter and no return,
#Function
def func( x, y ): #Formal Parameter/Argument., x = 7, y = 10
    
    print(f"{x} + {y} = { x+y }")

#Main
print("Hello")
a1 = int( input("Enter 1st number = ") )            #let assume, a1 = 7
a2 = int(input("Enter 2nd number = "))            #let assume, a2 = 10

a1 = ( (a1+2) * 5 ) / 7
a2 = ( (a2+2) * 5 ) / 7

print( f"a1 before function calling = { a1 }" )
print( f"a2 before function calling = { a2 }" )

func( a1, a2 )   #Actual Parameter/ A   rguement  #func( 7, 10 )

#func( ?1 , ?2 )   #?1 -> a1, a1 -> new a1, ?2 -> a2, a2 -> new a2




#Note :- Number of argument at sending side should be equals to Number of argument at receiving side

#Here at Actual Parameter, we have used a1 and a2 and at Formal Parameter
#We are using x and y. Here, Actual and Formal Parameter's Variable is
#Diffrent but still our Function will run. Because, At both Actual and
#Formal side our variable are holding the value and we are passing value
#not variables.


def abcd( x, y ):
    print( f"Inside Function, x = { x } and y = { y }" )

    x = x + 10
    y = y + 10

    print(f"Inside Function, x = {x} and y = {y}")

    x = x*8
    y = y*4

    print(f"Inside Function, x = {x} and y = {y}")


a = 7
b = 10

print( f"Outside Function, a = { a } and b = { b }" )

abcd( a, b )    #x, y -> ?, x,y = p, q ; Allot x value into p and y value into q
"""

"""
#3) #No Agurement/Parameter and return,

# Gautam called Prashant at his place.
# Gautam didn't tell anything to prashant.
# Prashant came and Made the Fan and he gave the Fan to Gautam.
#
# Here, We are not giving any Information/Data/Argument to Prashant(Function).
# Our Function i.e., Prashant is doing some task.
# and then, Prashant is giving Fan to Gautam. It means, Prsahant( our Function )
# is returning any thing.
#
# No Agurement/Parameter and return,
# We are returning only one value/Variable following,

def func():
    print( "Inside Function" )
    a1 = int( input("Enter 1st number = ") )
    a2 = int(input("Enter 2nd number = "))

    x = a1+a2
    print( f"Inside Function, x = { x }" )

    return x            #We are returning sum.( Only 1 value/var.)

print("Hi")
#add = ?, ? -> func()

add = func()        #This func() will return integer i.e, sum
print( f"func() = {  add  }" )
print("hello")

"""

"""
#We are returning only multiple value/Variable following,

def func():
    print( "Inside function" )
    a1 = int( input("Enter 1st number = ") )
    a2 = int(input("Enter 2nd number = "))

    l = []
    l.append(a1)
    l.append( a2 )
    print( f"l inside function = {l}" )

    return l            #We are returning the list l.

print("Hi")
p = func()        #This func() will return the list.
print()
print( f"OutSide Function, p = { p } and type(p) = { type(p) }" )
print()
print( f"p[0] = { p[0] } and p[1] = { p[1] }" )
print()
print( f"func() = {  p[0] + p[1] }" )   #9 +
print("hello")
"""


                        #or
"""
#we can return multiple values/variables from a function in following way
#also,

#Function
def func():
    print( "Inside Function" )
    a1 = int( input("Enter 1st number = ") )
    a2 = int(input("Enter 2nd number = "))

    return a1, a2            #We are returning sum.( Only 1 value/var.)

#Main
print("Before calling Function")

x, y = func()        #This func() will return integer i.e, sum   x = 2, y  =5

print(f"x = {x}")
print(f"y = {y}")
print( f"func() = { x+y }" )
print("hello")

#print(f"{a1} + {y} = {a1+y}")
"""

"""
# 4) #Agurement/Parameter and return,
#
# Gautam called Prashant at his place.
# Gautam told some work( To make T.V. ) to prashant.
# Prashant came and Made the T.V. and he returned the T.V. to Gautam.
#
# Here, Gautam is giving Information/Data/Argument to Prashant(Function).
# Our Function i.e., Prashant is doing some task.
# #and then, Prashant is giving TV. to Gautam. It means, Prsahant( our Function )
# is returning any thing.

#Agurement/Parameter and return,

def func( x, y ):   #x = a1 value, x = 6 and y = a2 value, y = 2
    print("Inside Function")
    print( f"Old x = { x }" )
    print( f"Old y = { y }" )
    x = x + 10
    y = y + 10
    print()
    print(f"New x = {x}")
    print(f"New y = {y}")

    return x, y

#Main
print( "Outside Function" )
a1 = int( input("Enter 1st number = ") )            #8
a2 = int(input("Enter 2nd number = "))              #3

print(f"a1 before function = {a1}")
print(f"a2 before function = {a2}")
print()
a1, y = func( a1, a2 )   #a1, y = ?, ? = func( a1, a2 ), a1 = ? = 8, a2 = ? = 3.
                         #a1, y = ?, ? = func( 8, 3 )
                         #a1, y = x, y, x = 18, y = 13
                         #a1 = 18, y = 13

print(f"a1 after function = {a1}")
print(f"a2 after function = {a2}")
print(f"y = {y}")
print()
# Internally, Value are getting allot in this way -> x, a2 = x, y
print(f"a1 = {a1} + a2 = {a2} = { a1 + a2 }")
print(f"a1 = {a1} + y = {y} = { a1 + y }")
"""
