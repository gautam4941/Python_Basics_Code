count_i = 0
count_j = 0
count_k = 0

k = 1
while( k <= 4 ):
    j = 1
    while (j <= 3):
        i = 1
        while (i <= 5):
            print(i)
            i = i + 1
            count_i = count_i + 1

        j = j + 1
        count_j = count_j + 1

    print()
    count_k = count_k + 1

    k = k + 1

print( f"count_i = { count_i }" )
print( f"count_j = { count_j }" )
print( f"count_k = { count_k }" )