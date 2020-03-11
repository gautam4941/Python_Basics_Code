''''''
"""
Mutable -> Any DataSet( Any Datatype which follows indexing ) which allows to change itself using indexing
            is known as Mutable DataSet/Data type and the process of changing is known as mutability.
            
    Ex :- a = [ 23, 6.7, True, 'Hello', 'Hi' ]
          a = [11, 12, 13, 14]   #This is not mutability practice. We are changing the whole list. we are not using
                                index here
          print( a[2] ) # 13
          a[2] = 0                      #Mutability( Process of changing value using index )
          print( a ) -> [11, 12, 0, 14]
          
          Thus, a is the list and it is supporting mutability. So, a is a mutable datatype.

ImMutable -> Any DataSet which doesn't allow to change itself using
            indexing, is known as Immutable DataSet/Data type.
            
        ex:- msg = "abcd"
             print( msg ) -> 'abcd'
             print( a[2] ) -> 'c'
             a[2] = 'g' -> Error( Immutability )
        
        Thus, msg is string and it is not supporting mutability. So, string is a immutable datatype.
"""

#ImMutable DataSet/Datatype

msg = "Hello"

print(f"msg = {msg}")
print(f"msg[0] = { msg[0] }")
print(f"msg[1] = { msg[1] }")
print(f"msg[2] = { msg[2] }")
print(f"msg[3] = { msg[3] }")
print(f"msg[4] = { msg[4] }")

#msg[0] = "i"  #H -> i  ,  This will not work as String is ImMutable
                        # DataType

#Mutable DataSet/DataType

a = [ 23, 6.7, True, 'Hello', 'Hi' ]
#index: 0, 1, 2, 3, 4

print( f"a[0] = {a[0]}" )
print( f"a[1] = {a[1]}" )
print( f"a[2] = {a[2]}" )
print( f"a[3] = {a[3]}" )
print( f"a[4] = {a[4]}" )

print( f"a = {a}" )
a[0] = 3
print(f"a = {a}")