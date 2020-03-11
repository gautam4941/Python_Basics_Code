#With Range()

#For loop Structure to make the block

"""
i = 1
while( i <= 10 ):
    print( i, end = ', ' )
    i = i + 4
"""

#Syntax :
"""
for loop_var in range( start, end, incr/decr ):
    work
 
"""



for i in range(1, 11, 1):           #11-0 = 11
    print(i, end=' ')

print()
print(f"i = {i}")

"""
for i in range( 11, 0, -1 ):
    print(i, end= ', ')

print()
print(f"i = {i}")
"""

# print( range(1, 11, 1) )  #print( ? ), ? -> range( 1, 11, 1 ) ->  range( 1, 11 )
# print( range(0, 11, 1) )  #print( ? ), ? -> range( 1, 11, 1 ) ->  range( 1, 11 )
#
# print()
# print( list( range(1, 10) ) )   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print()


'''
for i in list( range(1, 10, 1) ) :
    print(i, end = ', ')
print()
for i in [ [ [1, 2, 3, 4, 5, 6, 7, 8, 9] ] ]:
    print(i, end = '# ')
print()
for i in [8, 6, 9, 5]:
    print(i, end='* ')

print()
print( f"i  = { i }" )
'''