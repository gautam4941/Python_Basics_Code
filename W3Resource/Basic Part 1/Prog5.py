"""
 Write a Python program which accepts the user's first and last name
  and print them in reverse order with a space between them.
"""

f_name = input("First Name = ")
l_name = input("Last Name = ")

print( l_name, f_name )  #Method 1
print()
print( l_name, end=' ')  #Method 2
print( f_name )
print()
print( l_name + " "+f_name )        #Method 3
print()
print( f"{ l_name } { f_name }" )