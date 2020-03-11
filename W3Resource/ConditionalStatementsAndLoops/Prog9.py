"""
Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""

num1 = 0
num2 = 1

pos = 100
count = 2
num3 = 0

print( num1, end=', ' )
print( num2, end=', '  )

for i in range( 1, pos ):   #no_of_iteration = End - Start = (51+9) - 51 = 60-51 = 9
    num3 = num1 + num2

    if( num3 < 100 ):
        print(num3, end=', ')

        count = count + 1

    num1 = num2
    num2 = num3

print()
print( f"Count = { count}" )