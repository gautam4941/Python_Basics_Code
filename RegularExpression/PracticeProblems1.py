import re

dict1={}

NameAge ='Ram is 22, and Rohit is 33, Dinesh is 45 and Shwetha is 23'

ages = re.findall('[0-9]+',NameAge)

names = re.findall('[A-Z][a-z]+',NameAge)

print(f"ages = { ages }")
print( f"names =  {names} " )

for i in range( len( names ) ):
    dict1[ names[i] ] = ages[i]

print( dict1 )