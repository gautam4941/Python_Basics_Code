msg = "Hello, How are you ?"

print( f"msg = { msg }" )

print( msg[7] , end = '' )
print( msg[8] , end = '' )
print( msg[9] , end = '' )
print( msg[10] , end = '' )
print( msg[11] , end = '' )
print( msg[12] , end = '' )
print( msg[13] )

print( f"msg[ 7 : 14 : 1 ] = { msg[ 7 : 14 : 1 ] }" )
print( f"msg[ 7 : 14 ] = { msg[ 7 : 14 ] }" )
print( f"msg[ : 14 ] = { msg[ : 14 ] }" )
print( f"msg[ 7 :  ] = { msg[ 7 : ] }" )
print( f"len( msg ) = { len( msg ) }" )
print( f"msg[ 7 : len( msg ) ] = { msg[ 7 : len( msg ) ] }" )
print( f"msg[ : : 1 ] = { msg[ : : 1 ] }" )
print( f"msg[ : : 2 ] = { msg[ : : 2 ] }" )
print( f"msg[ : : 3 ] = { msg[ : : 3 ] }" )
print( f"msg[ : :  ] = { msg[ : :  ] }" )
print( f"msg[ : : 1 ] = { msg[ : : 1 ] }" )
print( f"msg[ : : -1 ] = { msg[ : : -1 ] }" )