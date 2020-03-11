msg = "Hello how are you ?"

#a-z = 97 - 122
#A-Z = 65 - 90
print( f"msg = { msg } " )
print()

flag = True

for i in range( len( msg ) ):

    temp = ord( msg[i] )

    print( f"msg[i] = { msg[i] }, temp = { temp }", end = ' ' )
    print( f"temp >= 97 and temp <= 122  = { temp >= 97 and temp <= 122  }", end = ' ' )
    print( f"temp >= 65 and temp <= 90 = { temp >= 65 and temp <= 90 }" )

    if( temp >= 97 and temp <= 122 ):
        pass
    elif( temp >= 65 and temp <= 90 ):
        flag = False
        break

if( flag == False ):
    print( "Not only lower" )
else:
    print( "only Lower" )
