'''
1
2
3
4
5

Let's Assume , above 1 to 5 printing is w1.

we have to run w1 5 times. w2 = w1 * 5

So, w1 is one loop. Then, w1 is another loop
'''

j = 1

while( j <= 5 ):
    i = 1
    a = 1

    while( i <= 5):
        print( a, end = ', ' )

        a = a + 1
        i = i + 1

    print()

    j = j + 1
