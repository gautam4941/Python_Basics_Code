import re

msg = '...hello,,how aRe yoU ?'

msg = msg.lower()

print( f"Souce msg = { msg }" )

l = re.findall( '[a-z]+', msg )

temp = []

for i in l:
    temp.append( list(i) )

for i in temp:
    i[0] = i[0].upper()

for i in range( len( temp ) ):
    temp[i] = ''.join( temp[i] )

print( f"Lastest Temp = { temp }" )
print()

for i in temp:
    print( i.lower(), msg.index( i.lower() ) )

print( len(msg) )