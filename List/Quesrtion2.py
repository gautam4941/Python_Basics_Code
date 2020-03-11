list1 = []
list2 = []

for i in range(1, 6):

    index = int( input("Enter the index = ") )
    data = input( "Enter the data = " )

    list1.insert( index, data )

    list2.append( data )

print(f"List 1 = {list1}")
print(f"List 2 = {list2}")

list1.pop()
print(f"list1 = {list1}")
list1.pop()
print(f"list1 = {list1}")

list2.pop(3)
print(f"list2 = {list2}")
list2.pop(2)
print(f"list2 = {list2}")