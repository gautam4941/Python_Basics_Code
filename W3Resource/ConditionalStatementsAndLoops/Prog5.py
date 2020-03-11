#Write a Python program that accepts a word/number from the user and reverse it.

#We are going with numbers, go for words after studying String concept.

num = int( input("Enter  a number = ") )

print(num)

new_num = 0

while( num > 0 ):
    new_num = new_num* 10 + num%10
    num = num/10

print(f"New_Num = { new_num }")
print( f"Old Num = { num }" )