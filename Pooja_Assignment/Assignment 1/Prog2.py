l = input()
l = l[ 1 : len( l ) -1 ].split( ',' )

print( l )

for i in range( len(l) ):
    l[i] = int( l[i] )

print( l )