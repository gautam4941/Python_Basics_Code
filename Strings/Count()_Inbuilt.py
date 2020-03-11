word = "Hesllo, How areHes you ?"
substr = "Hes"

i = 0
count = 0

while( i < len( word ) ):
    j = 0
    k = 0
    flag = False

    while( j < len(substr) ):
        if( substr[j] == word[i+k] ):
            flag = True
        else:
            flag = False
            break

        j = j + 1
        k = k + 1

    if( flag == True ):
        count = count + 1
        i = i + len( substr )

    else:
        i = i + 1

print( f"Count = { count }" )