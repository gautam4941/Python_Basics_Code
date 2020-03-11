word = input("Enter any String = ")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range( 0, len(numbers) ):
    numbers[i] = str(numbers[i] )

flag = True

for i in word:
    if( i in numbers ):
        flag = False
        break

if( flag == True ):
    print(f"{word} contains only alphabet")

else:
    print(f"{word} doesn't contains only alphabet")