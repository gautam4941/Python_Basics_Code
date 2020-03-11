#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

#Ex :- Write a Python program that accepts an integer (5) and computes the value of 5+55+555

a = input("Enter a number = ")

a_1 = int(a)
a_2 = int( a*2 )
a_3 = int( a*3 )

print( f"Value of a = { a_1 } and { a_1 } + { a_2 } + { a_3 } = { a_1 + a_2 + a_3 }" )