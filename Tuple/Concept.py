"""
List -> []
tuple - ()

Common,
Both can hold multiple data of hybrid datatype
Both Supports Indexing
we can print both

inbuilt Support,
1) del tuple -> Support  and del list -> Support
2) index()
3) Slicing
4) count()

Diffrence,
1) Tuple is Immutable whereas list is mutable
2) We can't add/remove data into tuple once it is fixed where we can add/remove in list
3) We can't update item using index( immutablility ) in tuple but we can do it in list.

inbuilt not Supporting,
del list[index] -> Support but del tuple[index] -> Error
pop(), sort(), copy(), reverse(), remove(), append(), insert(), extend() -> Support in list not in tuple

Why Tuple ?
We use tuple for the security purpose.
"""

#CREATE
"""
t = (8, 7, 9, 1)

print(f"t = {t}")

t.append( 1 )   #We Can't add or delete any element inside list.

                #Size of tuple will be fixed once it gets created.

print( f"t = {t}" )
"""

"""
#Update

t = (8, 7, 9, 1)

print(f"t = {t}")

#t[ 2 ] = 5          #We can't Update the data inside the tuple. Whereas,
                    #We can update the whole tuple.

t = ( 10, 19, 2 )

print(f"t = {t}")
"""

"""
#Delete

t = (8, 7, 9, 1)

print(f"t = {t}")

#del t[2]  #We can't delete the element of tuple by indexing. WHereas, we
          #can delete the whole tuple.

del t
print("SuccessFully Deleted")
print( t )
"""

'''
#Retrieve

t = (8, 7, 9, 1)

print(f"t = {t}")
print(f"t[0] = {t[0]}")
print(f"t[1] = {t[1]}")
print(f"t[2] = {t[2]}")
print(f"t[3] = {t[3]}")
'''

"""
#tupel's Inbuilt Functions,

#Count() and Index()

t = (8, 7, 9, 1, 9, 10, 1, 1, 8, 2, 9, 9, 1)

print(f"t = { t }")
data = int( input("Enter the data = ") )

count_data = t.count( data )

print(f"Count Data = { count_data }")

start_index = -1

for i in range( 0, count_data ):

    current_index = t.index( data, start_index+1 )

    print(f"Current Index = { current_index }")

    start_index = current_index
"""