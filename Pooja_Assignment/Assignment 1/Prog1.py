ap_seq = input().split( ', ' )
key = int( input() )

for i in range( len( ap_seq ) ):
    ap_seq[i] = int( ap_seq[i] )

a = ap_seq[0]
d = ap_seq[1] - ap_seq[0]

sum = a
indicator = 0

if( d >0 ):
    while( sum <= key ):

        if( sum == key ):
            indicator = 1
            break

        sum = sum + d
else:
    while (sum >= key):

        if (sum == key):
            indicator = 1
            break

        sum = sum + d

if( indicator == 0 ):
    print(False)
else:
    print( True )