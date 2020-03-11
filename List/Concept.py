"""
a = [ 23, 6.7, True, 'Hello', 'Hi', 8, 9, 0 ]
#index: 0, 1, 2, 3, 4, 5, 6, 7, ..., n

print( f"a = { a } and type( a ) = { type( a ) }" )
print()
print( f"a[0] = { a[0] }, type( { a[0] } ) = { type( a[0] ) }" )
print( f"a[1] = {a[1]}" )
print( f"a[2] = {a[2]}, type( { a[2] } ) = { type( a[2] ) }" )
print( f"a[3] = {a[3]}" )
print( f"a[4] = {a[4]}" )
print( f"a[5] = {a[5]}" )
print( f"a[6] = {a[6]}, type( { a[6] } ) = { type( a[6] ) }" )
print( f"a[7] = {a[7]}" )


b = a[0] + 5    #23+5 = 28
print()
print(f"b = {b}")
print()
print( f"a = { a }" )
print()
a[0] = a[0] + 3
print()
print(f"a = {a}")    #\n = print()
print("Hello")
"""

"""
a = [ 23, 6.7, True, 'Hello', 'Hi', 8, 9, 0 ]

print( f"a = { a }" )

for i in range( len( a ) ):
    print( a[i], type( a[i] ) )
"""

#index :- 0 to ....

#[] -> List
#() -> tuple
#{} -> Set, Dictionary


###################Data Insertion #######################

"""
#########Manual/ Static way of data insertion#########
l = [True, 6.7, 'Hi', 6, 8, 4, 9, 1]

print(f"l = {l}")
print( f"type(l) = {type(l)}" )
print()
"""

"""
#Following is dynamic way of feeding the values inside list#####

#append() - It will always feed the data at the last index
#syntax :- list_name.append( data/value )

# l = []
# l = [2]
# l = [2, 3]
# l = [2, 3, 4]

abc = []

print(f"1st abc = {abc}")
abc.append( 9 )
print(f"2nd abc = {abc}")

abc.append(8.6)
print(f"3rd abc = {abc}")

abc.append(False)
print(f"4th abc = {abc}")

abc.append('Hello')
print(f"5th abc = {abc}")

abc.append(10)
print(f"6th abc = {abc}")

abc.append('Class Over')
print(f"7th abc = {abc}")

abc.append('Prashant is eating')
print(f"8th abc = {abc}")
"""

"""
#list_name.append()

#append() using loop

#1, 8.6, False, Hello, 10, 'Class Over'


abc = []

n = int( input("Enter the no. of element required in list = ") ) #7 -> '7' -> int() -> 7 -> n


print(f"abc = {abc}")

for i in range( n ):    #5. i = 0, 1, 2, 3, 4, 5, 6
    abc.append( input("Enter a data = ") )   #abc.append( ? ), ? -> input() -> 2, abcd.append( 2 )
    print( f"abc = { abc }" )

print()
print(f"Final Print of abc = {abc}")
"""

"""
abc = []

while( True ):
    op = int( input("1. Append, 2. Exit, 3.Print = ") )

    if( op == 1 ):
        abc.append( input("Enter a value = ") )

    elif( op == 2 ):
        break

    elif( op == 3 ):
        print( abc )

    else:
        print("Incorrect Option")

print( f"Final Print of abc = { abc }" )
"""

"""
#insert() - It will feed the data at the specific index( Start or middle or last, index)
#insert() using loop
#Syntax :- list_name.insert( index, data )

abc = []

print( f"abc = { abc }" )

abc.insert( 0, 7 )
print( f"abc = { abc }" )
abc.insert(99, 13)   #if index is out of range, data will sotre at last index
print( f"abc = { abc }" )
abc.insert(-56, 10)   #if index is negative, data will sotre at 0 index
print( f"abc = { abc }" )
abc.insert( 0, 2 )   #if index is in range, data will sotre at specific index
print( f"abc = { abc }" )
abc.insert( -1, True )
print( f"abc = { abc }" )
"""

"""
abc = []

limit = int( input("Enter the Limit = ") )

print(f"abc = {abc}")

for i in range(1, limit+1):
    data = input("Enter the data = ")
    index = int( input( "Enter the index value = " ) )

    abc.insert(index, data)

    print( f"abc = { abc }" )
"""

"""
abc = []

while( True ):
    op = int( input("1. Insert, 2. Exit, 3. Display = ") )

    if( op == 1 ):
        val = input("Enter a value = ")
        index = int( input("Enter the position ( 0 t0 n.. ) = ") )
        abc.insert( index, val )

    elif( op == 2 ):
        break

    elif( op == 3 ):
        print( f"abcd = { abc }" )

    else:
        print("Incorrect Option")

print( f"Final abc = { abc }" )
"""

###############Data Deletion ###############
"""
#del - delete

abc = [2, 50, 3, 'True']

print( f"Before Deletion, abc = { abc }" )

print( f"Before Deletion, abc[2] = {abc[2]}" )

del abc[2]              #=> [2, 50, 'True']

print( f"After Deletion, abc = {abc}" )
print( f"After Deletion, abc[2] = {abc[2]}" )

del abc

print(f"abc = { abc }")
"""

"""
#pop()
#Syntax :- listname.pop()

abc = [2, 50, 3, 'True', 9, 'Hello', True, 23.34]
print(f"Before pop, abc = { abc }")

#action, update, return value
temp = abc.pop()  #pop() - Will remove the data from last index

print( f"temp = {temp}" )
print()
print(f"After abc = {abc}\n")

print( f"Deleted Item = { abc.pop( 5 ) }" )

print( f"abc = { abc }" )

print( f"Deleted Item = { abc.pop( -5 ) }" )

print( f"abc = { abc }" )
"""

"""
#If index inside pop is out of the existing range then, it will show error.

abc = [2, 50, 3, 'True', 9, 'Hello', True, 23.34]

print(f"abc = {abc}")

for i in range( 0, len( abc ) ):   #0, 1, 2, 3, 4, 5, 6, 7
    index = int( input("Enter the index value to be deleted = ") ) # ex :- 5 -> input() -> '5' -> int() -> 5 -> index
    indicator = 0

    if( index >= 0 ):
        if( index < len( abc ) ):
            indicator = 1
    else:
        if( index >= -len( abc ) ):
            indicator = 1

    if( indicator == 1 ):
        print( f"index = { index } and -len( abc ) = { -len( abc ) } and index <= -len( abc ) = { index <= -len( abc ) }" )
        print(f"Deleted Item = {abc.pop(index)}")  # abc.pop( 5 )

        print(f"abc{i + 1} = {abc}")
    else:
        print( "Index Out of Range" )
"""

'''
#len() -> len() is used to find the length of any dataset.
#Syntax :- len( dataset )

abc = [2, 50, 3, 'True']
#ind -> 0,  1, 2,  3
#count. 1,  2, 3,  4
#Extra :- Finding the len of list and accessing the last index

print( f"len( {abc} ) = {len( abc )}" )
print( f"Last Index :- len( abc ) - 1 =  len({ abc }) - 1 = {len( abc ) - 1}" )
print( f"Last Index Value :- abc[ len( abc ) - 1 ] = {abc[ len( abc ) - 1] }" )
'''

"""
############remove() ###############

#syntax :- list_name.remove( data/value )
#remove() will delete the data

abc = [2, 'True', True, 50, 3, 3, 'True', True]

print(f"abc = {abc}")
abc.remove( True )
print(f" abc = {abc}")

abc.remove( True )
print(f" abc = {abc}")

abc.remove( 'True' )
print(f" abc = {abc}")

abc.remove( 10 )
print(f" abc = {abc}")

print("Hello")
"""

"""
#count() - To count the number of elements inside list,
#Syntax :- list_name.count( value/variable )

l1 = [3, 10, 5, 6, 6, 8, 8, 8, 9, 10, 11, 6, 9, 8, 13]

print( f"l1 = { l1 }" )

print( f"l1.count( 10 ) = { l1.count( 10 ) }" )
print( f"l1.count( 9 ) = { l1.count( 9 ) }" )
print( f"l1.count( 8 ) = { l1.count( 8 ) }" )
print( f"l1.count( 13 ) = { l1.count( 13 ) }" )
print( f"l1.count( 7 ) = { l1.count( 7 ) }" )
"""

"""
l1 = [3, 10, 5, 6, 6, 8, 8, 8, 9, 10, 11, 6, 9, 8, 13]

find_data = int( input("Enter the data to be found = ") )

print( f"len( l1 ) = { len( l1 ) }" )

count_data = 0

for i in range( len( l1 ) ):
   if( find_data == l1[ i ] ):
       count_data = count_data + 1

print( f"Count_data = { count_data }" )

print( f"l1.count( { find_data } ) = { l1.count( find_data) }" )
"""

"""
#Count() + remove()

l = ['Mango', 'Apple', 'Mango', 2, True, 'Mango', 'Banana']

#Aim :- To remove all the Mango from the above list.

#Without Using Loop.
print( f"l = { l }" )

l.remove('Mango')
print( f"l = { l }" )

l.remove('Mango')
print( f"l = { l }" )

l.remove('Mango')
print(f"l = {l}")
"""

"""
#or
#With Using Loop,

l = ['Mango', 'Apple', 'Mango', 2, True, 'Mango', 'Banana', 'Mango']

count_mango = l.count('Mango')   # 4 -> count_mango

print(f"count_mango = { count_mango }")
print(f"l = {l}\n")

for i in range( 1, count_mango + 1 ):  # 0 .. 4-1 -> 0 .. 3 -> 0, 1, 2
    l.remove( 'Mango' )
    print(f"when i = { i }, l = {l}")

print( f"Final l = { l }" )
"""

"""
#extend() - To merge the 2 list into one,
#Syntax :- list1.extends( list2 )

l1 = [6, 2, 8, 1, 0]
l2 = [4, 6, 9, 11, 13]

print(f"l1 = {l1}")
print(f"l2 = {l2}\n")

l3 = l1.extend( l2 )                #l1 = l1+l2
l4 = l1+l2

print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(f"l3 = {l3}")
print(f"l4 = {l4}")
"""

"""
#Following is the alternative option of extends,

l1 = [6, 2, 8, 1, 0]
l2 = [4, 6, 9, 11, 13]

l1 = l1+l2
print(f"l1 = {l1}")
print( f"l2 = { l2 }" )
"""

"""
#index()
#Data + Start_range( Optional ) + End_range/Stop_range( Optional )
#list_name.index( data, start_range, End_range )
#Start_range and End_range are optional for finding index but, data is neccesary.

l1 = [3, 9, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]

print(f"l1 = {l1}")

index1 = l1.index( 9 )
print(f"First Time, index1 = {index1}")

index1 = l1.index(9, 0 )
print(f"Second Time, index1 = {index1}")

index1 = l1.index(9, 0, len(l1) )
print(f"Third Time, index1 = {index1}")

index2 = l1.index( 9, index1 + 1 )
print( f"Fourth Time, index2 = {index2}" )

index3 = l1.index( 9, index2 + 1 )
print( f"Fifth Time, index3 = {index3}" )

index4 = l1.index(9, index3+1)
print( f"Sixth Time, index 4 = {index4}" )
"""

#Note :- If your data is not in the range from start to End then, index() gives error.

"""
l1 = [3, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]

data = int( input("Enter the number to be searched = ") ) #5 -> input() -> '5' -> int() -> 5 -> data

# index1 = l1.index( data,     -1 + 1 )
# index2 = l1.index( data, index1 + 1 )
# index3 = l1.index( data, index2 + 1 )

count_data = l1.count( data )
print(f"count_data = { count_data }")
pos = []

ind = -1
for i in range( 1, count_data+1 ):   #iteration_count = count_data +1 - 1 = count_data( 4 )
    ind = l1.index( data, ind + 1 )
    print( ind, end=', ' )
    pos.append( ind )

print()
print( f"pos =  { pos }" )
"""

"""
#Sorting the list in acending and decending order
#Syntax :- list_name.sort() or list_name.sort( reverse = True )
#or list_name.sort( reverse = False )

l1 = [3, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]

print(f"l1 before sort = { l1 }")
print( l1.sort( ) )                 #action, update, return
print(f"l1 after sort = { l1 }\n")

l1 = [3, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]

print(f"l1 before sort, reverse = Fasle -> { l1 }")
l1.sort( reverse = False )
print(f"l1 after sort, reverse = Fasle -> { l1 }\n")

l1 = [3, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]

print(f"l1 before sort, reverse = True -> { l1 }")
l1.sort( reverse = True )
print(f"l1 after sort, reverse = True -> { l1 }\n" )
"""


#Explain this topic after slicing
#l1 = [3, 10, 5, 6, 7, 8, 8, 9, 10, 11, 6, 9, 13, 10]

#print( f"l1[ : : -1] = { l1[ : : -1] }")

"""
#SLICING()
# Syntax :- l1[ start : End : incr/decr ]


l1 = [3, 10, 5, 6, 7, 8, 8, 9, 10, 11, 6, 9, 13, 10]

print( f"l1[ 2 : 6 : 1 ] = {l1[ 2 : 6 : 1 ]}\n")

print( f"l1[ : 6 : 1 ] = {l1[ : 6 : 1 ]}")

print( f"l1[ 2 : : 1 ] = {l1[ 2 : : 1 ]}")

print( f"l1[ : : 1 ] = {l1[ : : 1 ]}")    #print( l1 )

print( f"l1[ : : 2 ] = {l1[ : : 2 ]}")

print( f"l1[ 2 : 10 : 2 ] = {l1[ 2 : 10 : 2 ]}")

print( f"l1[ 5 : 2 : -1 ] = {l1[ 5 : 2 : -1 ]}")

print( f"l1[ 5 : -1 : -1 ] = {l1[ 5 : -1 : -1 ]}")

print( l1[ -1 : -len(l1)-1 : -1 ] )

a = l1[ : : -1 ]
print( f"a = { a } and type(a) = { type(a) }" )

print( f"a[ 8: :  ] = { a[ 8: :  ] }" )
print( f"l1[ : : -1 ][ 8: :  ] = { l1[ : : -1 ][ 8: :  ] }" )
"""

"""
0, 1, 2, .. n
1, 2, .. n+1

-1, -2, ..., -n, -n-1
len() -> n+1
"""

"""
#It will reverse the order of list
#Syntax :- list_name.reverse()

l1 = [3, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]

print( f"Before reverse = { l1 }" )
l1.reverse()
print( f"After reverse = { l1 }" )
print()

l1 = [3, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]
print( f"l1 = { l1 }" )
print( f"l1[ : : -1] = { l1[ : : -1] }" )
print()
print( f"l1 = { l1 }" )
"""

"""
#copy()
l1 = [3, 10, 5, 6, 6, 8, 8, 9, 10, 11, 6, 9, 13, 10]

l2 = l1.copy()
l3 = l1

print( f"l1 = {l1}\n" )
print( f"l2 = {l2}\n" )
print( f"l3 = {l3}\n" )

l1[1] = 15

l4 = l3.copy()

print("After Change\n")
print( f"l1 = {l1}\n" )
print( f"l2 = {l2}\n" )
print( f"l3 = {l3}\n" )
print( f"l4 = {l4}\n" )

print( f"id(l1) = { id(l1) }" )
print( f"id(l2) = { id(l2) }" )
print( f"id(l3) = { id(l3) }" )
print( f"id(l3) = { id(l4) }" )
"""