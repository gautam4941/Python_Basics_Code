l = [ 1, 2, 3, 3, 3, 9, 9, 9, 9, 6, 6, 13, 13, 13, 13, 13, 5, 5, 7 ]

new_l = []

i = 0
while( i < len(l) ):
    if( l[i] == l[i+1] ):
        new_l.append( l[i] )
        i = i + 2

    else:
        new_l.append( l[i] )
        i = i + 1

    print(i, l[i], new_l)