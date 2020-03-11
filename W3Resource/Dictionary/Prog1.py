#1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = { 'a' : 1, 'b' : 5, 'c' : 2, 'd' : 0 }

key_list = []
value_list = []

for i, j in d.items():
    key_list.append( i )
    value_list.append( j )

#print( f"key_list = { key_list }" )
#print( f"value_list = { value_list }" )

value_list.sort()
#print()
print( f"key_list = { key_list }" )
print( f"value_list = { value_list }" )

new_d = {}

for i in value_list:
    print( f"i = { i }", end = ' -> ' )
    for j, k in d.items():
        print( f"\n       j = {j} and k = { k } and i == k = { i == k }", end = ' ' )
        if( i == k ):
            new_d[j] = k
            print( f"new_d = { new_d }" )

print( new_d )