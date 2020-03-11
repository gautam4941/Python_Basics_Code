#Filling Data into Dictionary from List
d = {}
l = ['one', 1, 'two', 2, 'three', 3, 'four', 4]

for i in range( 0, len(l) , 2):

    d[ l[i] ] = l[i+1]

print(d)