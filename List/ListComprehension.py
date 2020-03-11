#List and Tuple Comprehension

#List Comprehension

l = [1, 2, 3, 4, 5, 6]

#for i in range( len(l) ):             #parent
#    print(f"i = { i } and l[{ i }] = { l[i] }" )            #child

#[ child parent ], Note :- No colon
#[ print(f"i = { i } and l[{ i }] = { l[i] }" ) for i in range( len(l) ) ]

#for i in range(0, len(l)):
#    print( l[i] )


#[ print( l[i] ) for i in range(0, len(l)) ]

#for i in range(1, 3):           #parent1 -> Grand Father
#    for j in range(1, 6):       #parent2 -> Father
#        print(j, end=', ')      #child -> child

#    print()

#[ [ print(j, end=', ') for j in range(1, 6) ] for i in range(1, 3) ]

"""
#Key Notes:
1) put '[' and ']' outside of "every" child-parent combination
2) [ child parent ]
3) No colon for the parent part
#Tuple Comprehension
"""

t = (100, 200, 300, 400, 500, 600)

#for i in range( len(t) ):
#    print( f"i = { i } and t[{i}] = { t[i] }" )

[ print( f"i = { i } and t[{i}] = { t[i] }" ) for i in range( len(t) ) ]
