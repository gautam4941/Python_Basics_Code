l1 = [2, 3, 4, 5, 6, 7]
l2 = ['Ram', 'Shyam', 'Mohan', 'Ritu','ABC']
l3 = ['1BM14CS049', '1BM14CS050', '1BM14CS051', '1BM14CS052']

min_l = []

if( ( len( l1 ) <= len( l2 ) ) and ( ( len( l1 ) <= len( l3 ) ) ) ):
    min_l = l1.copy()

elif( ( len( l2 ) <= len( l1 ) ) and ( ( len( l2 ) <= len( l3 ) ) ) ):
    min_l = l2.copy()

else:
    min_l = l3.copy()

zip_l = []

for i in range( len( min_l ) ):
    zip_l.append( ( l1[i], l2[i], l3[i] ) )

print( zip_l )