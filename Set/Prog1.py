"""
s1 = {10, 1, 9, 5, 1, 9, 4, 1}
s2 = { 7, 2, 3, 2, 6, 7 }

print(f"s1 = {s1}")
print(f"s2 = {s2}")

print()
s3 = {'AB1C', 'CDE', 'ABC', 'AB1C', 'CDE', 'EFG', 'HIJ', 'Buiscuit', "Gautam", "Sanket"}
s4 = {'AB1C', 5, 7, 'CDE', 1, 'ABC', 'AB1C', 1, 'CDE', 'EFG', 9, 'HIJ', 'Buiscuit', "Gautam", "Sanket"}

print(f"s3 = {s3}")
print()
print( f"s4 = { s4 }" )
print()
print(f"s3 = {s3}")

l =  list(s4)
print( f"Before Sort, l = { l }" )
l.sort()
print( f"After Sort, l = { l }" )
"""

"""
s = {''}
print( f"Before removal of '' type( s ) = { type( s ) } and s = { s }" )
s.remove( '' )
print( f"After removal of '' type( s ) = { type( s ) } and s = { s }" )

s.add(2)
print( f"s = { s }" )
s.add(3)
print( f"s = { s }" )
s.add(2)
print( f"s = { s }" )
"""


"""
s3 = {''}  #This is set.
s4 = {}   #but, this is dictionary because, it is empty.

print( f"type(s3) = { type(s3) }" )
print( f"type( s4 ) = { type( s4 ) }" )

print(f"s3 = { s3 }")

print(f"s4 = { s4 }")


s3.add(3)
print( f"s3 = { s3 }" )
s3.remove( '' )
print( f"s3 = { s3 }" )
s3.add(2)
s3.add(3)
"""

#______________________Set Inbuilt Functions ________________________
"""
#1) add()

#syntax :- set_name.add( value/variable )

s1 = { '' }
print(f"s1 = {s1}")
s1.remove( '' )
print(f"s1 = {s1}")
s1.add('ABC')
print(f"s1 = {s1}")

s1.add('BCD')
print(f"s1 = {s1}")

s1.add('ABC')
print(f"s1 = {s1}")
"""

"""
#2) pop()
#Syntax :- Set_name.pop()

s1 = {10, 1, 9, 5, 1, 9, 4, 1}
s2 = {'ABC', 'CDE', 'ABC', 'ABC', 'CDE', 'EFG', 'HIJ'}

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print()
#how pop works if elements are number
print( f" s1 before pop = {s1} " )

del_element = s1.pop()
print( f"Deleted Element = {del_element}" )
print( f" s1 after pop = {s1} " )  #It will pop element from starting not ending.

del_element = s1.pop()
print( f"Deleted Element = {del_element}" )
print( f" s1 after pop = {s1} " )  #It will pop element from starting not ending.

print()
#how pop works if elements are string.
print( f" s2 before pop = {s2} " )

del_element = s2.pop()

print( f"Deleted Element = {del_element}" )
print( f" s2 after pop = {s2} " )  #It will pop element from starting not ending.

del_element = s2.pop()
print( f"Deleted Element = {del_element}" )
print( f" s2 after pop = {s2} " )  #It will pop element from starting not ending.
"""

"""
#3) remove()

s1 = {10, 1, 9, 5, 1, 9, 4, 1}
s2 = {'ABC', 'CDE', 'ABC', 'ABC', 'CDE', 'EFG', 'HIJ'}

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print()
#how remove works if elements are number
print( f" s1 before remove = {s1} " )

del_element = s1.remove(1)   #it will not return anything. So, it is None

print( f"Deleted Element = {del_element}" )
print( f" s1 after remove = {s1} " )
print()
#how remove works if elements are string.
print( f" s2 before remove = {s2} " )

del_element = s2.remove( 'ABC' )   #it will not return anything. So, it is None

print( f"Deleted Element = {del_element}" ) #None
print( f" s2 after remove = {s2} " )
"""

"""
#4) update()
#Syntax :- set1.update( set2 )

s1 = {10, 1, 'ABC', 9, 5, 1, 9, 4, 1, 'HIJ'}
s2 = {'ABC', 'CDE', 'ABC', 'ABC', 'CDE', 'EFG', 'HIJ'}

print(f"s1 before update = {s1}")
print(f"s2 before update = {s2}")

#s1.update(s2)
s2.update(s1)
print()
print(f"s1 after update = {s1}")
print(f"s2 after update = {s2}")
"""

"""
#diffrence()
#Syntax :- set1.diffrence( set2 )

s1 = {10, 1, 'ABC', 9, 5, 1, 9, 4, 1, 'HIJ'}   
s2 = {'ABC', 'CDE', 'ABC', 'ABC', 'CDE', 'EFG', 'HIJ'}

print(f"s1 before diffrence = {s1}")
print(f"s2 before diffrence = {s2}")
print()
print( f"s1.difference(s2) = {s1.difference(s2)}" )
print()
print(f"s1 after diffrence = {s1}")
print(f"s2 after diffrence = {s2}")
s1 = s1.difference(s2)   #Doing update manually.
print()
print( f"s1 = { s1 }" )
print( f"s2 = { s2 }" )
#It will do the action but doesn't update the s1.
#To update s1, we will have to do it manually.
"""




l = [5, 6, 5, 1, 0, 2, 1, 9, True, False, 'hi', True, 'abc', 'cde', 'abc' ]

print( l )
print( set(l) )