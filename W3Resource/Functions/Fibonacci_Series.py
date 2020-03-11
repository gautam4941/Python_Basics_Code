
def fibo( num1, num2, limit ):

    i = 1
    num3 = 0
    while( True ):
        if( i == 1 ):
            print( num1, end=', ' )
        elif( i == 2 ):
            print( num2, end=', ' )
        else:
            num3 = num1 + num2
            if( num3 > limit ):
                break

            print( num3, end=', ' )
            num1 = num2
            num2 = num3

        i = i + 1

    return num3

print( f"num3 = { fibo( 21, 34, 2000 ) }")