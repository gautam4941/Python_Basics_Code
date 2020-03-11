str1 = "abc"

str2 = "123"

str3 = "1abcd2"

#0-9 -> 48 - 57

flag = True

for i in range( 0, len( str3 ) ):  #0, 1, 2, 3, 4, 5  -> 0, 1
    print( f"i = { i } and str3[ {i} ] = { str3[i] }", end=' -> ' ) #str3[0], str3[1]
    print( ord( str3[i] ) )

    if( ( ord( str3[i] ) >= 48 ) and ( ord( str3[i] ) <= 57 ) ):  #True, False
        print( f"str3[i] = { str3[i] } and OK" )

    else:
        flag = False                    #flag = False
        break

if( flag == True ):
    print("String contains only Digit")
else:
    print("String doesn't contains only Digit")

print("hello")