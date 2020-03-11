'''
#Give me all prime number from 1 to 23.

2 -> Check Prime
3 -> Check Prime
4 -> Check Prime
.
.
.
23 -> Check Prime

23 -> 1, 2, 3, .., 22   #Cheking the prime number
'''

'''
#Checking one number as prime or not
for i in range( 2, 23+1 ):

    num = int( input() )
    flag = True
    a = 2

    for j in range( 2, num ):
        if( num%a == 0 ):
            flag = False
            break

        else:
            a = a + 1
            continue

    if( flag == True ):
        print("Prime No.")

    else:
        print( "Non - Prime Numer" )
'''

num = int(input())  # 9
prime = []

for i in range(2, num + 1):  # 2, 3, 4, 5..,9
    flag = False

    for j in range(2, i):  # (2,1), ( 2, 2 )

        if (i % j == 0):
            flag = True
            break

    if (flag == False):
        prime.append(i)

a = 0
for i in range( 0, len( prime ) ):
    print( prime[a] , end=" ")
    a = a + 1