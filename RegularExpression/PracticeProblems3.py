import re

'''

Extract the number from each of the lines using a regular expression and the findall()
method. Compute the average of the numbers and print out the average.

Input,
i) 38444.0323119
ii) 39756.9259259
'''

def findavg( number ):
    number = str( number )

    digits = re.findall("\d", number)
    print(f"digits = { digits }")

    add = 0
    for i in digits:
        add = add + int( i )

    print( f"Inside findavg, digits = { digits }" )
    print(f"Add = {add}, len(digit) = { len(digits) }, Average = {add/len(digits)}")
    print()

findavg( 38444.0323119 )
findavg( 39756.9259259 )