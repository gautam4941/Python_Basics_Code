data = input("Enter a data = ")    #Hello -> 0lleH

rev_data = data[ : : -1 ]

if( data == rev_data ):
    print( "Palindrome" )

else:
    print("Not a Palindrome")