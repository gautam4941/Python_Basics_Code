'''
l1 = [6, 2, 8, 1, 0]
l2 = [4, 6, 9, 11, 13]

print(f"l1 = {l1}")
print(f"l2 = {l2}")

temp = []
for i in range( len(l1) ):
    temp.append( l1[i] )

for i in range( len(l2) ):
    l1.append( l2[i] )
    print(f"l1 = {l1}")

print()
print(f"temp = {temp}")
print(f"l1 = {l1}")
print(f"l2 = {l2}")

l3 = l1
print(f"l3 = {l3}")

l1 = temp
print(f"l1 = {l1}" )
print()
print()
print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(f"l3 = {l3}")
print()

l3 = []
l3.append( l1 )
l3.append( l2 )
print(l3)

'''

'''
l1 = [6, 2, 8, 1, 0]
l2 = [4, 6, 9, 11, 13]

print(f"l1 = {l1}")
l3 = l1.extend( l2 )

print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(f"l3 = {l3}")
'''

l1 = [6, 2, 8, 1, 0]
l2 = [4, 6, 9, 11, 13]

l1 = l1+l2
print(f"l1 = {l1}")