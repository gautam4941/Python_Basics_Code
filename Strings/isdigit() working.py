"""
48 0
49 1
50 2
51 3
52 4
53 5
54 6
55 7
56 8
57 9
"""
msg = input("Enter a string = ")

flag = True

for i in range( len( msg ) ):
    current_str = msg[i]
    if( ord( current_str ) >= 48 and ord( current_str ) <= 57 ):
        pass
    else:
        flag = False
        break

if( flag == True ):
    print( f"{msg} contains only Digits" )

else:
    print( f"{msg} doesn't contains only digits" )