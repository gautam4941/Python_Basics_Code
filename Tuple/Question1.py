#Question :- t = (5, 2, 9, 0)

#output :- t =( 5, 2, 9, 0, 15, 20 )

#Method 1 :-
'''
t1 = (5, 2, 9, 0)

t2 = (5, 2, 9, 0, 15, 20)

print( f"t1 = {t1}" )
print(f"t2 = {t2}")
print()
t1 = t2
print( f"t1 = {t1}" )
print(f"t2 = {t2}")
'''
'''
#Method 2 :- Using Type Casting.

t1 = (5, 2, 9, 0)

list1 = list( t1 )

print(f"t1 = {t1}")
print(f"list1 = {list1}")

list1.append(15)
list1.append(20)

print(f"list1 = {list1}")

t2 = tuple( list1 )

print(f"t2 = {t2}")


t = (5, 2, 9, 0)

t = list(t)
t.append(15)
t.append(20)
t = tuple(t)

print(t)
'''