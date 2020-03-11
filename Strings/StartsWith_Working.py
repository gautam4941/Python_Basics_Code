str1 = "Hello, How are you ?"

str2 = "Hi"

str3 = "Hellos"

if( len( str1 ) >= len( str3 ) ):
    temp = str1[ 0 : len( str3 ) ]
    print( f"temp = { temp }" )

    if( temp == str3 ):
        print( True )
    else:
        print( False )

else:
    print( f"{ str1 } is not starting with { str3 }" )