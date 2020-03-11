"""
human_details = {'name' : ['Gautam', 'buke', 'vibha', 'mrityunjoy', 'prasanth'],
                'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ) }

print(f"human_details = {human_details}")
print()
print( f"type( human_details ) = { type( human_details ) }" )
print()
print( f"human_details['name'] = {human_details['name']}" )
print()
print( f"human_details['Empid'] = {human_details['Empid']}" )
print()
print(f"human_details['Blood_group'] = {human_details['Blood_group']}")
"""

"""
d = { 'Name' : ['Ram', 'mohan', 'Shyam', {'Number': [1, 2, 4,9] } ],
      'Age' : 20, 'PassFail' : True }

print( f"Main Dictionary = {d}" )
print()
print( f"d['Name'] = { d['Name'] }" )      #List
print()
d['Name'].append(True)

print(f"d = {d} and type( d ) = { type( d ) }" )
print()
print( f"d['Name'] = { d['Name'] } and type( d['Name'] ) = { type( d['Name'] ) }" )
print()
print( f"d['Name'][3] = { d['Name'][3] } and type( d['Name'][3] ) = { type( d['Name'][3] ) }" )   #Nested Dictionary
print()
print( f"d['Name'][3]['Number'] =  { d['Name'][3]['Number'] } and type( d['Name'][3]['Number'] ) = { type( d['Name'][3]['Number'] ) }" )  #Nested - nested - List
print()
d['Name'][3]['Number'].append(0)

print(d)
"""