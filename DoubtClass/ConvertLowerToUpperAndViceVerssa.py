#A-Z = 65 - 90
#a - z = 97 - 122

msg = input("Enter a String = ")

msg1 = ""

last_index = len( msg ) - 1

i = 0
while( i<=last_index ):

    current_letter = msg[i]

    if(  ord( current_letter ) >= 65 and ord( current_letter ) <= 90 ):
        msg1 = msg1 + chr( ord(current_letter) + 32 )

    elif(  ord( current_letter ) >= 97 and ord( current_letter ) <= 122 ):
        msg1 = msg1 + chr( ord(current_letter) - 32 )

    else:
        msg1 = msg1 + current_letter

    i += 1

print(f"msg = { msg } and Msg1 = { msg1 }")