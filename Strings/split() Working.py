msg = "Hello how are you ?"

# o/p :- ['Hello', 'how', 'are', 'you', '?']

temp = ''
l = []
for i in range( len( msg ) ): #0           , 1              , 2
    if( ( msg[i] != ' ' ) and ( i != len( msg ) - 1 ) ):      #'H'e        , 'e'            , 'l' non -space and non - last
        temp = temp + msg[i]  #''+'H' = 'H', 'H' + 'e' = 'He', 'He' + 'l' = 'Hel'

    else:               #space is there
        if( i == len(msg) - 1 ):     #last element
            if( msg[i] != ' ' ):        #non - space, if space then, don't do anything
                l.append( msg[i] )
        else:                           #non last index and non - space
            l.append( temp )
            temp = ''

    print( f"i = { i } and temp = { temp } and l = { l }" )

print( f"Final l = { l }" )