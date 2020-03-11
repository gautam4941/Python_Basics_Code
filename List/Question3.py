#Identify the Duplicate value from list l1.

'''
l1 = [3, 10, 5, 6, 6, 8, 8 , 9, 10, 11, 9, 13]

l2 = []

print( f"len(l1) = {len(l1)}" )

for i in range( len(l1) ):  # <len( l1 )  -> <10

    for j in range( i+1, len( l1 ) ):

        if( l1[i] == l1[j] ):

            l2.append( l1[i] )

print(f"l2 = {l2}")

print(f"l1 = {l1}")
'''
#Solvig Same above question using count()

l1 = [3, 10, 5, 6, 6, 8, 8 , 9, 10, 11, 6, 9, 13, 6]
l2 = []
dupl = []

for i in range( len(l1) ):

    dup = l1.count( l1[i] )
    dupl.append( dup )

    if( dup > 1 and dup not in l2):
        l2.append( dup )

print(f"l1 = {l1}")
print()
print(f"dupl = {dupl}")
print()
print(f"l2 = {l2}")