l = [1, 3, 5, 6, 10]
key = int( input() )

indicator = True

for i in range( len(l) ):
    for j in range( len(l) ):
        if( i != j ):
            if( ( l[i] - l[j] ) == key ):
                indicator = False
                break

    if( indicator == False ):
        break

if( indicator == False ):
    print( "YES" )
else:
    print( "NO" )