"""
for i in range( 1, 256):
    print( f"i = { i } and chr( {i} ) = { chr( i ) }" )
"""

msg = 'HH`ello, How Are You ?'
new_msg = ''

print( f"Before Action, msg = { msg }" )

for i in range( 0, len( msg ) ) :

    # A-Z = ( 65 - 90 )
    # 0-9 - ( 48 - 57 )
    # a-z = ( 97 - 122 )

    ascci_val = ord( msg[i] )

    if( ascci_val >= 65 and ascci_val <= 90 ):
        new_msg = new_msg + chr( ascci_val + 32 )

    elif( ascci_val >= 97 and ascci_val <= 122 ):
        new_msg = new_msg + chr( ascci_val - 32 )

    else:
        new_msg = new_msg + msg[i]

print()
print( f"After Action, msg = { msg }" )
print( f"After Action, new_msg = { new_msg }" )