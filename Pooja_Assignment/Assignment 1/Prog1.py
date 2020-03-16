ap_seq = input().split( ', ' )
key = int( input() )

for i in range( len( ap_seq ) ):
    ap_seq[i] = int( ap_seq[i] )

a = ap_seq[0]
d = ap_seq[1] - ap_seq[0]

if( d < 0 ):
    d = -d

indicator = False

if( key < a ):
    while( a>=key ):
        if( a == key):
            indicator = True

        a = a - d
else:
    while( a <= key ):
        if (a == key):
            indicator = True

        a = a + d

if( indicator == True ):
    print( "Yes" )

else:
    print( "No" )
