"""
# 0 to 9 -> 48 to 57
# A to Z -> 65 to 90
# a to z -> 97 to 122


for i in range( 256 ):
    print( f"i = { i } and chr(i) = { chr( i ) }" )

#character -> ascii_value -> character
#a -> ord(a) -> chr( a )
#str -> int -> str
"""

"""
msg = "He.llo"
new_msg = ""

#O/P :- hE.LLO

for i in range( len(msg) ):
    ascii_val = ord( msg[i] )

    print( "Before new_msg = ", new_msg, " msg[i] = ", msg[i], "and ascii_val = ", ascii_val)

    if( ascii_val >= 65 and ascii_val <= 90 ):
        ascii_val = ascii_val + 32

    elif( ascii_val >= 97 and ascii_val <= 122 ):
        ascii_val = ascii_val - 32

    new_msg = new_msg + chr( ascii_val )

    print( "After new_msg = ", new_msg, "and New ascii_val = ", ascii_val )
    print()
"""