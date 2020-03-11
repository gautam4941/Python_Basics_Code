word = "hello, How ARE yOU. Hello ?"

new_msg = ''

for i in range( len( word ) ):
    ascii_val = ord( word[i] )

    if( i == 0 ):
        if (ascii_val >= 97 and ascii_val <= 122):
            ascii_val = ascii_val - 32

    else:
        if (ascii_val >= 65 and ascii_val <= 90):
            ascii_val = ascii_val + 32

    new_msg = new_msg + chr( ascii_val )

print( "Word = ",word )
print( "New_Message = ",new_msg )