l = []

for i in range( 1, 11 ):
    a = input("Enter a number = ")

    if( a.isdigit() ):
        if( isinstance( int( a ), int ) ):
            a = int(a)
            l.append(a)

    print(f"l = { l }")
