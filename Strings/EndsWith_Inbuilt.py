word = "Hello, How are you. Hello ?"
substr1 = "Hello"
substr2 = "Hello ?"
substr3 = "lo ?"


print( f"len(word) = { len(word) }" )
print( f"len( substr2 ) = { len( substr2 ) }" )
print( f"len(word) - len( substr2 ) = { len(word) - len( substr2 ) }" )

print( f"word[ len(word) - len( substr2 ) ] = { word[ len(word) - len( substr2 ) ] }"  )
print()
indicator = 1

k = 0
for i in range( 20, len( word ) ):
    if( word[i] != substr2[k]  ):
        indicator = 10
        break

    k = k + 1

if( indicator == 1 ):
    print( "Endswith = True" )
else:
    print( "Endswith = True" )