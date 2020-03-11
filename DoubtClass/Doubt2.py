'''
d = {}
#Method 1 for filling data in dictionary
for i in range(1, 5):
    key = input("Enter the Key = ")
    value = int(input("Enter the Value = "))

    d[key] = value
'''
'''
#Method 2 for filling data in dictionary
key = []
value = []

for i in range(1, 5):
    key.append(input("Enter the key = ") )
    value.append( int( input("Enter the value = ") ) )

print(f"Key = {key}")
print(f"Value = {value}")

for i in range( len( key ) ):
    d[ key[i] ] = value[i]

print(d)
'''