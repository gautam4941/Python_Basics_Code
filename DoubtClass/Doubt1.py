l = [78, 3, 5, 12, 90]


print( f"Maximum = {max(l)}" )
print( f"Minimum = { min(l)}" )
print( f"Sum = { sum(l)}" )
print()
l.sort()

print( f"Minimum = {l[0]}" )

print( f"Maximum = {l[ len(l) - 1 ]}" )

sum = 0

for i in range(0, len(l) ):
    sum = sum + l[i]

print(f"Sum = {sum}" )
print(f"Average = {sum//len(l)}" )