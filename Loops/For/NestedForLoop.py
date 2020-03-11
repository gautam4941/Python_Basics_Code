for k in range( 1, 3 ):
    print( f"k = { k }" )
    for j in range(1, 5):  # i = 1

        print(f"j = {j}")
        for i in range(1, 6):  # i = 1 -> W1, i = 2 -> W1, .., i = 5 -> W2, i = 6
            print(f"W1 : i = {1}", end=' ')

        print()

        for i in range(1, 6):  # i = 1 -> W2, i = 2 -> W2s, .., i = 5 -> W2, i = 6
            print(f"W2 : i = {2}", end=' ')

        print()