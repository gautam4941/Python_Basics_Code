word = "Hello, How are you. Hello ?"
substr1 = "Hello"

flag = True

for i in range( len( substr1 ) ):
    if( word[i] != substr1[i] ):
        flag = False
        break

if( flag == True ):
    print( "Startswith = True" )
else:
    print( "Startswith = False" )