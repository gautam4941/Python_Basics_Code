print("While : Print '1' 10 times : w1, and This w1 * 10 times : w2, w2 * 5 Times : 3, W3*3 times = w4 ")

k = 1                                                                 #W4
while( k <= 3 ):

    j = 1                                               # W3
    while (j <= 5):                                     # W3

        i = 1                                   # W2    # W3
        while (i <= 10):                        # W2    # W3

            print(1, end=', ')          # W1    # W2    # W3

            i = i + 1                           # W2    # W3

        print()                                         # W3

        j = j + 1                                       # W3

    print()

    k = k+1                                                           #w4


"""
print("While : 10x5x3 Times Ended")
    
print()

print("For : Print '1' 10 times and This 10 times is 5 Times")

for k in range(1, 4):
    
    for j in range(1, 6):
        
        for i in range( 1, 11 ):
            print(1, end = ', ')

        print()
    print("10x5 Times Ended")
    
print("For : 10x5x3 Times Ended")
"""

'''
a = 1

while( a <= 4 ):
    k = 1

    while (k <= 3):
        i = 1

        while (i <= 5):
            print(1, end=', ')
            i = i + 1
        print()

        k = k + 1

    print()

    a = a + 1
'''