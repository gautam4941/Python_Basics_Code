'''
#Bakery 1
if( Tea ):
    if( sweet buiscuit ):
        pass
    else:
        salty buiscuit
        if( choclate ):
            take choclate

elif( Coffee ):
    if( Lays ):
        pass

elif( Milk ):
    if( Kurkure ):
        pass

elif( Water ):
    pass

else:
    go

#Bakery 2
if( Veg Puff ):
    if( Coffee ):
        pass
    else:
        Tea

#Bakery 2
if( Tea ):
    if( sweet buiscuit ):
        pass
    else:
        salty buiscuit
        if( choclate ):
            take choclate

elif( Egg Puff ):
    if( Lays ):
        pass
'''

"""
#If Statement

#Syntax :-
#Condition == True, Condition == False( It will not go inside/ not do the work )
#if( Condition ):   
#    WORK

a = int( input("Enter a number = ") )   #6 -> input() -> '6' -> int() -> 6

print( f"a = { a } and a>0 = { a>0 }" )

if( a>0 ):
    print(f"{a} is greater than 0")

print("Hello")
print(2+3)
"""

"""
#If - else Statement
a = int( input("Enter a number = ") )       6 -> input() -> '6' -> int() -> 6 -> a

print( f"a = { a } and a>0 = { a>0 }" )

if(a>0):
    print(f"{a} is greater than 0")

else:
    print(f"{a} is smaller than 0")

print("Hello")
"""


# #elif Ladder/Series Statement
#
# if( Tea == available):
#     print( "Drink Coffee at Bakery")
#
# elif( coffee == available):
#     print( "Drink Coffee at Bakery")
#
# elif( Water == available):
#     print( "Drink water at Bakery")
#
# elif( buiscuit == available):
#     print( "Eat buiscuit at Bakery")
# else:
#     print("Go Home")

"""
a = 35

print("Hello, Start of elif Block")

if( a<0 ):
    print(f"{a} is less than 0")

elif( a == 0 ):
    print(f"{a} is equals to 0")

elif( a>0 and a<=10 ):
    print(f"{a} is from 1 to 10")

elif( a>10 and a<=20 ):
    print(f"{a} is from 11 to 20")

elif( a>20 and a<=30 ):
    print(f"{a} is from 21 to 30")

else:
    print(f"{a} is more than 30")

print( "After If Else" )

"""

"""
a = 65
#if, check 65 is divisible by 3
#or check 65 is divisible by 5
#or check 65 is divisible by 7
#check 65 is divisible by 8

a = 6

if( a%3 == 0 ):
    print( f"{a} is divisible by 3" )

elif( a%5 == 0 ):
    print( f"{a} is divisible by 5" )

if( a%7 == 0 ):
    print( f"{a} is divisible by 7" )

elif( a%8 == 0 ):
    print( f"{a} is divisible by 8" )
"""

"""
a = 10

if( a>=0 and a<=20 ):
    print(f"Your Grade is A and marks is {a}")

elif( a>20 and a<=40 ):
    print(f"Your Grade is B and marks is {a}")

elif( a>40 and a<=60 ):
    print(f"Your Grade is C and marks is {a}")

elif( a>60 and a<=80 ):
    print(f"Your Grade is D and marks is {a}")

elif( a>80 and a<=100 ):
    print(f"Your Grade is E and marks is {a}")

else:
    print("Incorrect Marks")
"""

"""
#Multiple if - else block
a = 7
b = -5


if( a > 0 ):
    print(f"{a} is more than 0")

print("End of 1st if statement")
print()

if( a == 5 ):
    print("a is equal to 5")
else:
    print("a is not equal to 5")

if( b == -5 ):
    print("b is equals to -5")
else:
    print("b is not equals to -5")

if( a>0 ):
    print("a is greater than 0")
else:
    print("a is not greater than 0")

if( b>0 ):
    print("b is greater than 0")
else:
    print("b is not greater than 0")
"""


#Nested if else

#Condition 1 : Number should be greater than 0.

#If condition1 is True, Then, if number is divisible by 2 then, print Even
#                            otherwise, print ODD

#if Condition1 Fails then, print condition one is failing.

"""
if( coffee == available ):
    print( "Order Coffe" )
    if( buiscuit == available ):
            if( sweet_buiscuit == available ):
                print( "Order sweet_buiscuit" )
            else:
                print("Order salt buiscuit")

elif( lays == available ):
    print( "Order Lays" )
    if( kurkure == availble ):
        print( "Order Kurkure" )
"""

"""
num = -6

if( num >= 0 ):
    print(f"{num} is Greater than or equals to 0", end=' -> ')

    if( num%2 == 0 ):
        print("Even")

    else:
        print("Odd")

else:
    print(f"{num} is Smaller than 0", end=' -> ')

    if (num % 2 == 0):
        num = num * 2

    else:
        num = num * 3

    print( f"Num = { num }" )
"""

"""
a = 15
b = 20
c = 20

if( a>=b and a>=c):
    print(f"a is greater than {b} and {c}")

elif( b>=a and b>=c ):
    print(f"{b} is greater than {a} and {c}")

else:
    print(f"c is greater than {a} and {c}")
"""

"""
a = 125
b = 30
c = 232

if( a>b ):
    print("IF ", end = '-> ')
    if( a>c ):
        print("IF ")
        print(f"{a} is greater than {b} and {c}")

    else:
        print("Else ")
        print(f"{c} is  greater than {a} and {b}")

else:
    print("Else -> ", end = '')
    if (b > c):
        print("IF -> ")
        print(f"{b} is greater than {a} and {c}")

    else:
        print("Else -> ")
        print(f"{c} is greater than {a} and {b}")
"""


"""
#Multiple If-Else Blocks

#Bakery1
if( coffee = available ):
    print( "Drink Coffe" )

elif( milk == available ):
    print("Drink Milk")

#Bakery 2
if( coffee = available ):
    print( "Drink Coffe" )

elif( Water == available ):
    print("Drink water")

else:
    print("Go")

#bakery 3
if( Tea = available ):
    print( "Drink Tea" )
"""

"""
a = 12

if( a>0 ):
    print(f"{a} si greater than 0")
else:
    print( f"{a} is smaller than 0" )

if( a%2 == 0 ):
    print( f"{a} is Even" )
else:
    print("Odd")

if( a%13 == 0):
    print(f"{a} is divisible by 3")

elif( a%4 == 0):
    print(f"{a} is divisible by 4")

elif( a%3 == 0):
    print(f"{a} is divisible by 5")

else:
    print( f"{a} is not divisble by 3, 4 and 5" )
"""