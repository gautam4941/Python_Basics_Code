l1 = [1, 2, 3, 5, 9]
l2 = [3, 6, 9, 12]
l3 = []

for i in range(len(l1)):

    if (l1[i] in l2):
        if ((l2.count(l1[i])) == (l1.count(l1[i]))):
            l3.append(l1[i])

        elif( l1[i] not in l3 ):
            l3.append(l1[i])

print(l3)
