"""
a = {'SNO' : [1, 2 ] ,
'Name' : ['Gautam', 'Anil' ] ,
'Salary' : [ 25000, 28000] ,
'Bonus' : [17000, 22000] }

print( a )
print()
print( f"a['Name'] = { a['Name'] } and type( a['Name'] ) = { type( a['Name'] ) }" )

print( a['Name'][0] )
"""

"""
human_details = {'name' : ['Gautam', 'buke', 'vibha', 'mrityunjoy', 'prasanth'],
                'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ) }

print( human_details )
print()
print( human_details[ 'name' ] )

human_details['name'].append( True )
print()
print( human_details )
"""

"""
x = { 'a' : 'b',
 'c' : ['d', 1, 2],
  'e' : { 8, 9, 0 },
  'f' : ( 10, 11, 12 ),
  'g' : { 'h' : [1, 2, 3],
          'i' : 'Hello'}    ,
  'j' : 13 }

print( f"x = { x } and type( x ) = { type( x ) }" )
print( f"x['a'] = { x['a'] } and type( x['a'] ) = { type( x['a'] ) }" )
print( f"x['c'] = { x['c'] } and type( x['c'] ) = { type( x['c'] ) }" )
print( f"x['e'] = { x['e'] } and type( x['e'] ) = { type( x['e'] ) }" )
print( f"x['f'] = { x['f'] } and type( x['f'] ) = { type( x['f'] ) }" )
print( f"x['g'] = { x['g'] } and type( x['g'] ) = { type( x['g'] ) }" )
print( x['g']['i'] )
print( f"x['j'] = { x['j'] } and type( x['j'] ) = { type( x['j'] ) }" )
"""

x = [1
    , 2
    , 3
    , { 'a' : 1, 'b' : [ 'Hi', 2, { 'c' : False, 'd' : 10, 'e' : ( 11 ) } ] }
    , 6
    , 7
    , [ True, 9, 8 ]
     ]

#write python program to reach to following data,

print( x[3]['b'][2]['d'] )    #10
print( x[3]['b'][0]  ) #'Hi'
print( x[6][2] )   #8
print( x[3]['b'][2]['c'] )  #False
print( x[3]['b'][2]['e'] )  #11
