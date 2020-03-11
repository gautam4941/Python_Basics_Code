for i in range( 4 ):
    print(i, end=', ')

print()
print( range( 4 ) )                 # ( [ { 0, 1, 2, 3 } ] )
print( range( 1, 4 ) )              #1, 2, 3
print( range( 1, 4, 2 ) )           #1, 3
print()
print( list( range(4) ) )
print( list( range(1, 4) ) )
print( list( range(1, 4, 2) ) )
print()
print( tuple( range(4) ) )
print( tuple( range(1, 4) ) )
print( tuple( range(1, 4, 2) ) )
print()
print( set( range(4) ) )
print( set( range(1, 4) ) )
print( set( range(1, 4, 2) ) )
print()

print("Loop using List")

for i in range(0, 4 ):
    print(i)

for i in [ 0, 1, 2, 3 ]:
    print(i, end=', ')
print()
print("Loop using Tuple")
for i in (0, 1, 2, 3):
    print(i, end=', ')
print()
print("Loop using Set")
for i in { 0, 1, 2, 3 }:
    print(i, end=', ')
print()

print( "Using Random number in the list, " )
for i in [ 7, 0, 9, 1, 4, 6 ]:
    print( i, end=', ' )
print()


"""

human_details = {'Empid' : (550891, 0, 1, 11563797, 552866) ,
                'Blood_group' : ('AB+', 'AB-', 'B+', '0+', '0+' ),
                 'msg' : 'Hello'}

for i in human_details.keys():
    print( human_details[i], end=', ' )
"""

# Conclusion :- Go for for loop in range, if you want a continious series.
# if you want to run the loop in the data set you can go for with range for loop and
# without range for loop
#
# If you are going for with range then, make you range( start, end, incr/decr ) such
# that, if make a continue series which is same as indexing of the dataset.
#
# You can use without range for loop only inside a dataset. You can use it to create any
# continuous sequence.
#
# Above statements are for Understanding but ultimately the whole for loop is working a
# dataset only.
