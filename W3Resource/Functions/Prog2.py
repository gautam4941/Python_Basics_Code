def sumoflist( x, y ):     #x = [6, 123, 453, 2, 8]
    sum = 0

    for i in x:
        sum = sum + i           #sum = ?, ? = 0 + 6 = 6 -> sum.   sum = ?, ? = 6 + 123 = 129 -> sum

    sum = sum + y

    return sum

l = []
l.append(6)
l.append( 123 )
l.append( 453 )
l.append( 2 )
l.append( 8 )

print( f"Outside l = { l }" )

print("Calling Function sumoflist for 1st time ")
a = sumoflist( l, 5 )    #a = ?, ? = sumoflist( ? ), ? = [6, 123, 453, 2, 8]
                    #a = ?, ? = sumoflist( [6, 123, 453, 2, 8] )
                    #a = sumoflist( [6, 123, 453, 2, 8] )

print( f"Outside a = { a }" )