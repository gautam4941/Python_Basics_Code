'''
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).
'''

count = 0

i = 1500
while( i <= 2700 ):

    if ((i % 5 == 0) and (i % 7 == 0)):
        print(f"{i} is divisible by 5 and 7")
        count = count + 1

    i = i + 1

print( f"{ count } numbers are divible by 5 and 7" )