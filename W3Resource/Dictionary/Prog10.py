d = {}

for i in range( 1, 6 ):
    d[i] = i+10

print( d )

#l = []
sum = 0
for i, j in d.items():
    #l.append( i + j )
    print( f"i = { i } and j = { j } and i + j = { i + j }" )
    sum = sum + i + j

print()
#print( f"l = { l }" )
print( f"Total Sum = { sum }" )

"""
new_d = {}

count = 0
for i in l:
    new_d[ i ] = count
    count = count + 1
    print( new_d )
"""