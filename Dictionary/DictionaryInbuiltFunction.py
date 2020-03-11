"""
human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

print( human_details )
print()

print( f"human_details[ 'Empid' ] = { human_details[ 'Empid' ] }\n" )
print( f"type( human_details[ 'Empid' ] ) -> type( { human_details[ 'Empid' ] } ) = { type( human_details[ 'Empid' ] ) }\n" )


print( f"human_details[ 'Empid' ][3] = { human_details[ 'Empid' ][3] }\n" )
print()
print( human_details['Empid'] )

print( f"Type casting into list = { list( human_details['Empid'] ) }")

print( human_details['Empid'] )

human_details['Empid'] = list( human_details['Empid'] )
print()
print( human_details['Empid'] )
print()
print( type( human_details[ 'Empid' ] ) )
print()
print( human_details )
"""

"""
#keys()
human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

print( f'''human_details.keys() = { human_details.keys() }\n
and type( human_details.keys() ) = { type( human_details.keys() ) }''' )

print()
print()
keys = list( human_details.keys() )

print( f"keys = { keys } and type( keys ) = { type(keys) } and len( keys ) = { len( keys ) }" )
print()
"""

"""
human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

for i in human_details :   #0, 1, 2
    print( f"i = { i } and human_details[ i ] = { human_details[ i ] }")
"""

"""
#values()
human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ['AB+', 'AB-', 'B+', '0+', '0+'],
                 'msg' : {'Hello'} }

print( f"human_details.keys() = { human_details.keys() }" )
print( f"type( human_details.keys() ) = { type( human_details.keys() ) }" )
print( f"human_details.values() = { human_details.values() }" )
print( f"type( human_details.values() ) = { type( human_details.values() ) }" )
print()

print( f"list( human_details.keys() ) = { list( human_details.keys() ) }" )
print( f"list( human_details.values() ) = { list( human_details.values() ) }" )
print()
for i in human_details.values():
    print( f"i = { i } and type( i ) = { type(i) }" )
"""

"""
#item()
#Syntax :- dict_name.item()

human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

print( human_details )
print()
print( human_details.items() )
print()


for i, j in human_details.items():
    print( f"i = { i } and type(i) = { type(i) }" )
"""


"""
a, b = 2, 3
a -> 2
b -> 3

a = 2, 3

print( a )
 a -> (2, 3)
 
a, b = (2, 3 )
a -> 2
b -> 3

for i, j in human_details.items():
    print(i, end = ' -> ')
    print(j)
"""

"""
Show How to add a new data( Key and Value ) int the dictionary.
"""

"""
#copy()
#Syntax :- var = dict.copy()

human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

temp1 = human_details
temp2 = human_details.copy()

print( f"temp1 = { temp1 }" )
print()
print( f"temp2 = { temp2 }" )

temp1['Empid'] = 1
temp2['Empid'] = 3
print()
print( f"human_details = { human_details }" )
print()
print( f"temp1 = { temp1 }" )
print()
print( f"temp2 = { temp2 }" )
print()
print( f"id( human_details ) = { id( human_details ) }" )
print( f"id( temp1 ) = { id( temp1 ) }" )
print( f"id( temp2 ) = { id( temp2 ) }" )
"""

"""
#fromkeys()
#Rules for fromkeys() : Left side element must be a dataset( Which follows indexing )   -> This will become Key
#                        Right Side element can be anything -> This will become value
a = [4, 2, 8]
b = 'hello'
c = 10

print( f"dict.fromkeys( a, b ) = { dict.fromkeys( a, b ) }" )
print( f"dict.fromkeys( b, a ) = { dict.fromkeys( b, a ) }" )
print( f"dict.fromkeys( a, c ) = { dict.fromkeys( a, c ) }" )
print( f"dict.fromkeys( b, c ) = { dict.fromkeys( b, c ) }" )
print( f"dict.fromkeys( c, a ) = { dict.fromkeys( c, a ) }" )    #dict.fromkeys( 10, [4, 2, 8] ) -> { 10 : [4, 2, 8] }
"""

"""
#set_default()

human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ) }

print( human_details )
print()

#human_details.setdefault( 'msg', 'hi' )        #Adding Data into dictionary as key doesn't exist
#human_details[ 'msg' ] = 'hi'                  #Adding Data into dictionary as key doesn't exist
#human_details[ 'Blood_group' ] = 5             #Updating Data from dictionary as key already exist

print( human_details )
"""

"""
#update()

human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

print( human_details )
print()
#human_details.update( {'Empid' : 1} )           #update or insert

human_details[ 'Empid' ] = 1                          #Updating Data from dictionary as key already exist
human_details[ 'salary' ] = 12000, 5000, 8000, 16000  #Adding Data into dictionary as key doesn't exist

print( human_details )
print()
"""

"""
#pop() and popitem()

human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

print( human_details )
print()
human_details[ 'roll'] =  12

print( human_details )
print()
human_details.pop( 'Blood_group' )

print( human_details )
print()
human_details.popitem()

print( human_details )

del human_details['Empid']

print( human_details )
"""

"""
#get()
human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

print( f"human_details = { human_details }" )

print( f"human_details.get( 'Empid' ) = { human_details.get( 'Empid' ) }" )
print( f"human_details['a'] = { human_details['a'] }" )
"""