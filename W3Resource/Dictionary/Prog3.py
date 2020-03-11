"""
Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

"""
dic1 = { 1:10, 2:20 }
dic2 = { 3:30, 4:40 }
dic3 = { 5:50, 6:60 }

print( f"dic1 = { dic1 }" )
print( f"dic2 = { dic2 }" )
print( f"dic3 = { dic3 }" )

new_d = {}

print( f"new_d = { new_d }" )

for i, j in dic1.items():
    new_d[i] = j

print( f"new_d = { new_d }" )

for i, j in dic2.items():
    new_d[i] = j

print( f"new_d = { new_d }" )

for i, j in dic3.items():
    new_d[i] = j

print( f"new_d = { new_d }" )
"""

"""
dic1 = { 1:10, 2:20 }
dic2 = { 3:30, 4:40 }
dic3 = { 5:50, 6:60 }

l = [ dic1, dic2, dic3 ]
print( f"l = { l }" )

new_d = {}

for i in l:
    for j, k in i.items():
        new_d[j] = k
        print( f"new_d = { new_d }" )


    print()
"""


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, '1' : 0}

key = 'a'
print( f"key = { key }" )

flag = True

for i in d:
    if( isinstance( i, str ) ):
        if( str( key ) == i ):
            print( f"Key is available in the dictionary and type(i) = { type(i) } " )
            flag = False
            break

    else:
        if( key == i ):
            print(f"Key is available in the dictionary and type(i) = { type(i) }")
            flag = False
            break

print() 
if( flag == True ):
    print(f"Key is not available in the dictionary")
else:
    print(f"Key is available in the dictionary")