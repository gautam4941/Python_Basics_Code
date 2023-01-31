############# Conditional Statements #####################

# If condition
# Syntax :-

# Syntax :- if( True/ False ):
                # Statement 1
                # Statement 2
                # .
                # .
                # Statement n


# If-else Statement . else = otherwise

# Syntax :- if( True/ False ):
                # Statement 1
                # Statement 2
                # .
                # .
                # Statement n
#           else:
                # Statement 1
                # Statement 2
                # .
                # .
                # Statement n



#### Elif Ladder ####
# Syntax :- if( True/ False ):
                # Statement 1
                # Statement 2
                # .
                # .
                # Statement n
#           elif( True/ False ):
                # Statement 1
                # Statement 2
                # .
                # .
                # Statement n
#           else:
                # Statement 1
                # Statement 2
                # .
                # .
                # Statement n

#### Nested Condition ####
# Conditional Block -> If , if-else, elif ladder
    
# Syntax :- Conditional Block:
#                 Conditional Block:
#                   Conditional Block:


#### Multiple Conditional Statements ####
# Conditional Block -> If , if-else, elif ladder, nested structure
    
# Syntax :- Conditional Block 1:
#           Conditional Block 2:
#           .:
#           .:
#           Conditional Block n:


"""
# maths = float( input( "Enter Maths marks = " ) )
# phy = float( input( "Enter Physics marks = " ) )
# chem = float( input( "Enter Chem marks = " ) )

maths = 65
phy = 55
chem = 50
total = maths+phy+chem
maths_phy = maths+phy

print( f"maths = { maths }" )
print( f"phy   = { phy   }" )
print( f"chem  = { chem  }" )
print( f"Total = { total }" )
print( f"maths_phy = { maths_phy }" )

if( maths >= 65
    and phy >= 55
    and chem >= 50
    and ( ( total >= 190 ) or ( maths_phy >= 140 ) )
    ):
    print( f"Eligible" )
else:
    print( f"Not Eligible" )

"""


################### Loops #################

# Components of Loops
# Start Point
# Ending Point
# Incr/ Decr
# Incr by/ Decr by
# Work
# Loop VariableFor

# 1) While Loops,
# Syntax :-
# loop_variable = start
# while( Condition ): # Condition start <= end
#
#   work
#   loop_var = loop_var incr(+) incr_by


"""
print( "Start" )

i = 1
while( i <= 10 ):

    print( 1 )
    i = i + 1

print( "End" )
"""

# *********
#  *******
#   *****
#    ***
#     *

"""
a = -1
b = 8
n = 5

i = 1
while( i<= n ):

    j = 1
    while( j <= i+a ):
        print( f" ", end= '' )
        j = j + 1

    j = 1
    while( j <= i+b ):
        print( f"*", end='' )
        j = j + 1
        
    i = i + 1

    print()

    b = b - 3

# i     n(Symbol)     i+a = n(symbol)   a
# 1     9             1+? = 9           8
# 2     7             2+? = 7           5

# i     n(Symbol)     i+a = n(symbol)   a
# 1     0             1+-1 = 0          -1
# 2     1             2+? = 1           -1
"""

# template
"""
a_initial Value =
b_initial Value =

i = 1
while( i <= no_of_lines ):

    j = 1
    while( j <= i + a ):
        print( "Symbol1", end = '' )
        j = j + 1

    j = 1
    while( j <= i + a ):
        print( "Symbol2", end = '' )
        j = j + 1

    print()
    i = i + 1

    adjust a value
    adjust b value


i     n(Symbol)     i+a = n(symbol)     a
"""

"""
n = 5
i = 1
while( i <= n ):

    j = 1
    while( j <= i):
        print( "*", end = '' )
        j = j + 1

    print()
    i = i + 1

a = 3
n = 4
i = 1
while( i <= n ):

    j = 1
    while( j <= i+a):
        print( "*", end = '' )
        j = j + 1

    print()

    a = a - 2
    i = i + 1

# i     n(Symbol)     i+a = n(symbol)     a
# 1      1            1+0  = 1            0
"""


"""
print( "*" )
n = 3
i = 1
while( i <= n ):

    print( "*", end ='')
    j = 1
    while( j <= i - 1 ):
        print( " ", end = '' )
        j = j + 1
    
    print( "*", end ='')
    
    print()

    i = i + 1

print( "*"*(n+2) )

# i     n(Symbol)     i+a = n(symbol)     a
# 1     0
"""


"""
Input upto the table number starting from 1 : 8
Expected Output :
Multiplication table from 1 to 8
1x1 = 1, 2x1 = 2, 3x1 = 3, 4x1 = 4, 5x1 = 5, 6x1 = 6, 7x1 = 7, 8x1 = 8
...
1x10 = 10, 2x10 = 20, 3x10 = 30, 4x10 = 40, 5x10 = 50, 6x10 = 60, 7x10 = 70, 8x10 = 80
"""

"""
start = 1
end = 8

# 1x1 = 1, 2x1 = 2, 3x1 = 3, 4x1 = 4, 5x1 = 5, 6x1 = 6, 7x1 = 7, 8x1 = 8
# 1x1 = 1, 2x1 = 2, 3x1 = 3, 4x1 = 4, 5x1 = 5, 6x1 = 6, 7x1 = 7, 8x1 = 8,

i = 1
while( i<= 10 ):
    # Work
    j = 1
    while( j <= end ):
        print( f"{j}x{i} = {j*i}", end = ', ' )
        j = j + 1

    print()
    i = i + 1
"""


"""
X^0/0! - X^2/2! + X^4/4! - .........]

Test Data :
Input the Value of x :2
Input the number of terms : 5

Expected Output :
the sum = -0.415873
Number of terms = 5
value of x = 2.000000
"""

"""
# n = 5 , pattern = 8 , end_point = 2*n-2
# n = 6 , pattern = 10 , end_point = 2*n-2
total = 0
x = 2
n_term = 5

j = 0
while( j <= ((2*n_term)-2) ):
    # counter = counter + 1

    # Fact Code Start
    fact = 1
    n = j
    i = 1
    while( i <= n ):
        fact = fact * i
        i = i + 1
    # Fact Code End
    
    ans = (x**j)/ fact

    if( j%4 != 0 ):
        ans = ans * -1
        
    total = total + ans
    print( f"Numerator = { x**j }, Deno = { fact }, ans = { ans }, total = { total }" )
    
    # print( ans )
    j = j + 2

print( f"\n\nTotal = { total }" )
"""    

"""
n_term = 100000

j = 2
while( j <= n_term ):

    n = j
    end = int( n**0.5 )
    # print( 1, end = ', ')
    total = 1

    i = 2
    while( i <= end ):
        if( n%i == 0 ):
            # print( f"{i}, {n//i}", end = ', ' )
            if( i == (n//i) ):
                total = total + i
            else:
                total = total + i + (n//i)
            
        i = i + 1

    if( n == total ):
        print( f"{n} is a perfect number" )

    j = j + 1
"""

"""
n_term = 1000

j = 1
while( j <= n_term ):
    n = j
    temp = n

    power = len( str( n ) )
    total = 0

    while( n > 0 ):
        rem = n%10
        n = n//10

        total = total + (rem**power)

    # print( f"total = { total }" )
    if( temp == total ):
        print( f"{temp} is an Armstrong number" )

    j = j + 1
"""


"""
n = input( "Enter the Binary Value = " )
n = n[ ::-1 ]
n_len = len(n)
total = 0

i = 0
while( i < n_len ):
    total = total + ( int(n[i]) * (2**i) )
    
    i = i + 1
    

print( f"Binary = {n} and Number = { total }" )
"""

########## for Loop #########

# for Loop -> with range and without range

# Components of Loops
# Start Point
# Ending Point
# Incr/ Decr
# Incr by/ Decr by
# Work
# Loop Variable

#Syntax :-
# for loop_var in range( start, end, incr/decr by ):
    # Work

# i = 1
# while( i <= 10 ):
#     print( i )
#     
#     i = i + 1

# for i in range( 1, 11, 1 ):
#     print( i )

# range( start = 0, end, step = 1 )    
# range( start = 0, end)    

# for i in range( 1, 11, 1 ):
#     print( i )



# DIfference between For and While Loop
# 1) Incr By decimal/ multiple increment : While Loop
# 2) Infinite Loop : While Loop
# 3) Conditional Based Incr/ Decr : WHile Loop


"""
i = 1
while( i < 15 ):
    print( f"Before, i = {i}", end = ' , ' )

    if( i%3 == 0 ):
        i = i + 1

    i = i + 1
    print( f"After, i = {i}\n" )
"""

"""
for i in range(1, 16):
    print( f"Before, i = {i}", end = ' , ' )

    if( i%3 == 0 ):
        i = i + 2

    print( f"After, i = {i}\n" )
"""

####### String ######

"""
word = "Hello"
#len =  12345
#+ve in=01234
#-ve in=   -1
       =  -2
       = -3
       =-4
       -5
"""

# last_index = len() - 1

word = "Hello"

# for i in range( 5 ):
#     print(i, word[i] )

# for i in range( -1, -6, -1 ):
#     print( i, word[i] )

# for i in range( len(word) ):
#     print( i , word[i] )

# for i in range( -1, -len(word)-1 ,-1 ):
#     print( i , word[i] )


# '5' -> int('5') -> 5

# character -> ascii value
# chr() -> ord()

# for i in range( 1, 1000 ):
#     print( i, chr(i) )

# Digits -> 48 to 57
# Upper Case -> 65 to 90
# Lower Case -> 97 to 122

"""
word = "Hello, How are 4354365 you ?"

upper_count = 0
lower_copunt = 0
number_count = 0

for i in range( len( word ) ):
    ord_val = ord( word[i] )

    if( ord_val >= 48 and ord_val <= 57 ):
        number_count += 1

    elif( ord_val >= 65 and ord_val <= 90 ):
        upper_count += 1

    elif( ord_val >= 97 and ord_val <= 122 ):
        lower_copunt += 1

print( f"upper_count  = { upper_count  }" )
print( f"lower_copunt = { lower_copunt }" )
print( f"number_count = { number_count }" )
"""

"""
65 A
66 B
67 C
68 D
69 E
.
.
85 U
86 V
87 W
88 X
89 Y
90 Z

97 a
98 b
99 c
100 d
101 e
.
.
117 u
118 v
119 w
120 x
121 y
122 z
"""

# Digits -> 48 to 57
# Upper Case -> 65 to 90
# Lower Case -> 97 to 122

"""
word = "Hello, How are 4354365 you ?"
new_word = ""

for i in range( len( word ) ):
    ord_val = ord( word[i] )

    # if( ord_val >= 97 and ord_val <= 122 ):
    #     ord_val = ord_val - 32

    if( ord_val >= 65 and ord_val <= 90 ):
        ord_val = ord_val + 32

    new_word = new_word + chr( ord_val )

print( f"word = {word}" )
print( f"new_word = {new_word}" )
"""

######## String ######
"""
L = [ 11, 12, 13 ]

print( "Before", L )
L[0] = 100
print( "After", L )


word = "Hello"
print( "Before", word )
word[0] = 'Z'
print( "After", word )
"""

########## String Inbuilt Functions ######

"""
# Input
word = 'hello, How are you 123 hey hi'
substr = 'h'

# Output
# Index 1 : 4
# Index 2 : 8
# Index 3 : 16

find_val = -1
counter = 0
while( True ):
    find_val = word.find( substr, find_val+1 )

    if( find_val == -1 ):
        break

    counter = counter + 1
    print( f"Index {counter} = { find_val }" )
"""

# Slicing
# str_data[ start = 0 : end = last_index : step = 1 ]

"""
swapcase()
replace()
ljust()
rjust()
strip()
rstrip()
lstrip()


isalnum()
isalpha()
isdecimal()
isdigit()
islower()
isspace()
istitle()
isupper()

split()
join()
"""

"""
3. Write a Python program to get a string made of the first 2 and last 2 characters
of a given string.
If the string length is less than 2, return the empty string instead.

Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""

"""
word = "w"

if( len(word) < 2 ):
    print( "" )
else:
    print( word[ : 2] + word[ -2 : ] )
"""

"""
word = "restart"

print( word[0] + word[1:].replace( word[0], '$' ) )
"""

'''
word = """Hello
We are in Python
Training Session"""

word = word.replace( '\n', '' )

print( word )
'''

"""
word = 'thequickbrownfoxjumpsoverthelazydog'

output = ""
for i in range( len( word ) ):
    if( word[i] not in output ):
        count_char = word.count( word[i] )

        if( count_char > 1 ):
            output = output + f"{word[i]} { count_char }" '\n'

print( output )
"""

"""
word = "32.054,23"

print( f"1. word = { word }" )

word = word.replace( '.', '$' )
print( f"2. word = { word }" )

word = word.replace( ',', '.' )
print( f"3. word = { word }" )

word = word.replace( '$', ',' )
print( f"4. word = { word }" )
"""

"""
word = "32.054,23"
print( f"1. word = { word }" )

word_list = word.split( '.' )
print( f"2. word_list = { word_list }" )

for i in range( len( word_list ) ):
    word_list[i] = word_list[i].replace( ',', '.' )

print( f"3. word_list = { word_list }" )

word_list = ','.join( word_list )
print( f"4. word_list = { word_list }" )
"""

"""
word = "ab ca bc ab"

i = 0
while( i<len( word) ):
    temp = ""

    while( True ):
        if( 
        print( i, word[i] )

    i = i + 1


"ab bc ab ca" , temp = "ca ", considered_str = "ab, ca,", max_count = 2, selected_str = temp
"""


############ List ##########

"""
L1 = []
print( f"L1 = { L1 } and type( L1 ) = { type( L1 ) }" )

L1.append( 5 )
print( f"L1 = { L1 }" )

L1.append( 5.2 )
print( f"L1 = { L1 }" )

L1.append( True )
print( f"L1 = { L1 }" )

L1.append( False )
print( f"L1 = { L1 }" )

L1.append( "Hello" )
print( f"L1 = { L1 }" )

L1.append( [11, 12, 13] )
print( f"L1 = { L1 }" )
"""

"""
L1 = []
print( f"L1 = { L1 } and type( L1 ) = { type( L1 ) }" )

L1.insert( 0, 'zero' )
print( f"L1 = { L1 }" )

L1.insert( 100, 'one' )
print( f"L1 = { L1 } and L1[1] = { L1[1] }" )

L1.insert( -100, 'two' )
print( f"L1 = { L1 }" )

L1.insert( 3, 'Three' )
print( f"L1 = { L1 }" )

L1.insert( 1, 'Four' )
print( f"L1 = { L1 }" )

L1.insert( -200, 'Five' )
print( f"L1 = { L1 }" )
"""

"""
L1 = [ 11, 13, 11, 15, 15, 19, 20 ]
print( f"L1 = { L1 }\n\n" )

L1_len = len( L1 )
i = 0
while( i < L1_len ):
    curr_ele = L1[i]
    ele_count = L1.count( curr_ele )
    print( f"i = {i}, curr_ele = { curr_ele } and ele_count = { ele_count }" )
    
    if( ele_count > 1 ):

        j = 0
        while( j<ele_count-1 ):
            print( f"\tBefore: j = {j}, curr_ele = { curr_ele }, L1 = {L1}" )
            L1.remove( curr_ele )
            j = j + 1

            print( f"\tAfter: j = {j}, curr_ele = { curr_ele }, L1 = {L1}\n" )
            
            L1_len = L1_len - 1

        print()
            
    i = i + 1
    
print( f"L1 = { L1 }" )
"""

"""
L1 = ['abc', 'xyz', 'aba', '1221', 13, 19, 20]
count = 0

for i in range( len( L1 ) ):
    if( isinstance( L1[i], str ) ):
        if( (len( L1[i] ) > 1) and ( L1[i][0] == L1[i][-1] ) ):
            print( L1[i] )
            count += 1

print( count )
"""

"""
L = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

count_zero = L.count(0)

for i in range( count_zero ):
    L.remove(0)

L.extend( [0] * count_zero )

print( L )
"""

"""
L = [ 2, 2, 2, 2, 3, 4, 5, 5, 4, 4, 4 ]

# Step 1 : [ 2, 2, 2, 3, 4, 5, 4, 4 ]
# Step 2 : [ 2, 2, 3, 4, 5, 4 ]
# Step 3 : [ 2, 3, 4, 5, 4 ]
# Step 4 : [ 2, 3, 4, 5, 4 ]

len_L = len(L)

i = 0
while( i < len_L ):
    print( f"Before: i = {i}, L[i] = {L[i]}, L = {L}, len_L = { len_L }" )

    if( i == len_L-1 ):
        break
    
    if( L[i] == L[i+1] ):
        L.pop( i )
        i = i - 1
        len_L -= 1

    print( f"After : i = {i}, L[i] = {L[i]}, L = {L}, len_L = { len_L }\n" )
    i = i + 1

print( f"Final : L = {L}" )
"""

"""
while( True ):
    start_len_L = len(L)

    i = 0
    while( i < start_len_L ):
        
         i = i + 1
"""


"""
Leet Code :-

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
"""

######## Set ############
"""
s = { 14, 11, 13, 12, "Hello", "ABC", "XYZ", "EFP" }

print( f"1. s = { s }" )
print( f"2. s = { s }" )
print( f"3. s = { s }" )
print( f"4. s = { s }" )
"""


# s = set()

"""
s.add(2)
print( f"1. s = { s }" )
s.add( 1 )
print( f"2. s = { s }" )
s.add( True )
print( f"3. s = { s }" )
s.add( 1.5 )
print( f"4. s = { s }" )
s.add( "Hello" )
print( f"5. s = { s }" )
"""

"""
s = {1, 2, 'Hello', 1.5}
print( f"1. s = { s } and id(s) = { id(s) }" )
s.clear()
# s = set()
print( f"2. s = { s } and id(s) = { id(s) }" )
"""

"""
s = {1, 2, 'Hello', 1.5}
print( f"1. s = { s } and id(s) = { id(s) }" )
s2 = s.copy()
s3 = s
# s = set()
print( f"2. s = { s } and id(s) = { id(s) }" )
"""

"""
s1 = {1, 2, 'Hello', 1.5, 6}
s2 = {11, 12, 'Hello', 1.5}

print( f"1. s1 = { s1 }" )
print( f"1. s2 = { s2 }\n" )

# print( f"s1.difference( s2 ) = { s1.difference( s2 ) }\n" )
# print( f"s1.difference_update( s2 ) = { s1.difference_update( s2 ) }\n" )

# print( f"s1.intersection( s2 ) = { s1.intersection( s2 ) }\n" )
# print( f"s1.intersection_update( s2 ) = { s1.intersection_update( s2 ) }\n" )

# print( f"s1.discard( 1 ) = { s1.discard( 1 ) }" )
# print( f"s1.remove( 1 ) = { s1.remove( 1 ) }" )

# s1.pop()
# print( f"s1.isdisjoint( s2 ) = { s1.isdisjoint( s2 ) }\n" )
# print( f"s1.issubset( s2 ) = { s1.issubset( s2 ) }\n" )
# print( f"s1.issuperset( s2 ) = { s1.issuperset( s2 ) }\n" )

# print( f"s1.union( s2 ) = { s1.union( s2 ) }\n" )
# print( f"s1.intersection( s2 ) = { s1.intersection( s2 ) }\n" )
# print( f"s1.symmetric_difference( s2 ) = { s1.symmetric_difference( s2 ) }\n" )

# print( f"s1.union( s2 ).difference( s1.intersection( s2 ) ) :- \n{ s1.union( s2 ).difference( s1.intersection( s2 ) ) }\n" )

# s1.symmetric_difference_update(s2 )
s1.update( s2 )

# print( f"s1.discard( 100 ) = { s1.discard( 100 ) }" )
# print( f"s1.remove( 100 ) = { s1.remove( 100 ) }" )
print( f"2. s1 = { s1 }" )
print( f"2. s2 = { s2 }" )
"""

"""
L1 = [ [1, 2, 3], True,  [11, 12, 13], [ 14 , False] ]
L2 = [ [11, 12, 3], True,  [21, 22, 13], [ 24 , False] ]

# a) common and it's product
# b) not common and it's product 
# c) Union  and it's product 
# d) Difference without using difference().

s1 = set()
s2 = set()

for i in L1:
    if( isinstance( i, list ) ):
        for j in i:
            s1.add( j )
    else:
        s1.add( i )

for i in L2:
    if( isinstance( i, list ) ):
        for j in i:
            s2.add( j )
    else:
        s2.add( i )

print( f"s1 = {s1}" )
print( f"s2 = {s2}" )

s1_new = set()
for i in s1:
    if( i not in s2 ):
        s1_new.add( i )

s2_new = set()
for i in s2:
    if( i not in s1 ):
        s2_new.add( i )

print( f"s1_new = {s1_new}" )
print( f"s2_new = {s2_new}" )

s_final = s1_new.union( s2_new )
print( f"s_final = { s_final }" )
"""


########## Dictionary ##########


# Bonus = ( 12000, 35000 )
# Salary = ( 20000, 40000 )

# Bonus_and_Salary = [ 12000, 20000, 40000, 35000 ]


# Dictionary = It's key-value pair datatype

"""
d = { key1 : value1
      , key1 : value1
      .
      .
      , keyn : valuen}
"""

# d = {}
d = dict()

# Add or Update value of any key in the dictionary.
# d[key] = value
"""
d[ 1 ] = "Hello"
print( f"1. d = { d }" )

d[ 2 ] = True
print( f"2. d = { d }" )

d[ 1 ] = "Bye"
print( f"3. d = { d }" )
"""

"""
d = {11: 'Bye', 12: True}
# d.setdefault( 3, "Three" )

print( f"1. d = { d }" )

# print( f"d.pop( 1 ) = { d.pop( 1 ) }" )
# print( f"d.popitem() = { d.popitem() }" )

# print( d[100] )
# print( d.get(100) )

# print( f"d.keys() = { d.keys() } and type( d.keys() ) = { type( d.keys() ) }" )
# print( f"d.values() = { d.values() } and type( d.values() ) = { type( d.values() ) }\n" )
print( f"d.items() = { d.items() } and type( d.items() ) = { type( d.items() ) }\n" )

for i, j in d.items(): # i, j in (11, 'Bye')
    print( f"For : i = {i}" )
    print( f"For : j = {j}\n" )
    
print( f"\n2. d = { d }" )    
"""

"""
d = {1: 'One', 6: 'Six', 2: 'Two'}
print( f"1. d = {d}" )

# print( f"dict.fromkeys( ['One', 'two', 'three'], 0 ) = { dict.fromkeys( ['One', 'two', 'three'], 0 ) }" )

d.update( {11: True, 12 : False} )


print( f"2. d = {d}" )

"""

"""
1) Counting the frequencies in a list using dictionary in Python
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
                  4, 4, 4, 2, 2, 2, 2]
Output : 1 : 5
         2 : 4
         3 : 3
         4 : 3
         5 : 2
Explanation : Here 1 occurs 5 times, 2 
              occurs 4 times and so on...

2) Python counter and dictionary intersection example (Make a string using deletion and rearrangement)
Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible

Input : s1 = Hello
      : s2 = dnaKfhelddf
Output : Not Possible

Input : s1 = GeeksforGeeks
      : s2 = rteksfoGrdsskGeggehes
Output : Possible

3) Find Out all years, data with pattern [A-Z][a-z][a-z][a-z]... 
"""

"""
data = "Geeks for Geeks and Geeks for Geeks is great Website"
new_data = ""

for i in data.split( ' ' ):
    if( i not in new_data ):
        new_data = new_data + i + ' '

new_data.strip()
print( new_data )
"""

"""
data = "paradox"
n = 3

n = n - 1
upper_list = [ 'A'
, 'B'
, 'C'
, 'D'
, 'E'
, 'F'
, 'G'
, 'H'
, 'I'
, 'J'
, 'K'
, 'L'
, 'M'
, 'N'
, 'O'
, 'P'
, 'Q'
, 'R'
, 'S'
, 'T'
, 'U'
, 'V'
, 'W'
, 'X'
, 'Y'
, 'Z' ]
lower_list = [ 'a'
, 'b'
, 'c'
, 'd'
, 'e'
, 'f'
, 'g'
, 'h'
, 'i'
, 'j'
, 'k'
, 'l'
, 'm'
, 'n'
, 'o'
, 'p'
, 'q'
, 'r'
, 's'
, 't'
, 'u'
, 'v'
, 'w'
, 'x'
, 'y'
, 'z' ]

new_data = data[ : n ]
for i in range(n, len(data ) ):
    if( data[i].islower() ):
        new_data = new_data + lower_list[ -lower_list.index( data[i] ) -1 ]
        
    elif( data[i].isupper() ):
        new_data = new_data + upper_list[ -upper_list.index( data[i] ) -1 ]

print( f"Data = { data }" )
print( f"New data = { new_data }" )
"""

data = '''Tendulkar took up cricket at the age of eleven, made his Test match debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years. In 2002, halfway through his career, Wisden ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards.[9] Later in his career, Tendulkar was part of the Indian team that won the 2011 Cricket World Cup, his first win in six World Cup appearances for India.[10] He had previously been named "Player of the Tournament" at the 2003 edition of the tournament.
Tendulkar received the Arjuna Award in 1994 for his outstanding sporting achievements, the Khel Ratna Award, India's highest sporting honour, in 1997, and the Padma Shri and Padma Vibhushan awards in 1999 and 2008, respectively, two of India's highest civilian awards.[11][12] A few hours after the end of his last match in November 2013, the Prime Minister's Office announced the decision to award him the Bharat Ratna, India's highest civilian award.[13][14] As of 2021, he is the youngest recipient to date and was the first sportsperson to receive the award.[15][16] In 2012, Tendulkar was nominated to the Rajya Sabha, the upper house of the Parliament of India.[17]'''

"""
upper_ind = False
lower_ind = False
temp = ""

for i in data:
    if( (upper_ind == False) and (lower_ind == False) and i.isupper() ):
        upper_ind = True
        temp = i

    elif( (upper_ind == True) and (lower_ind == False) and i.islower() ):
        lower_ind = True
        temp = temp + i

    elif( (upper_ind == True) and (lower_ind == True) and i.islower() ):
        temp = temp + i

    elif( (upper_ind == True) and (lower_ind == True) and ( i.islower() == False ) ):
        print( temp, end = ', ' )
        upper_ind = False
        lower_ind = False
        temp = ""
"""

"""
upper_ind = False
lower_ind = False
temp = ""

for i in data:
    if( (lower_ind == False) and (upper_ind == False) and and i.islower() ):
        lower_ind = True
        temp = i

    elif( (lower_ind == True) and (upper_ind == False) and i.isupper() ):
        upper_ind = True
        temp = temp + i

    elif( (lower_ind == True) and (upper_ind == True) and i.isupper() ):
        temp = temp + i

    elif( (upper_ind == True) and (lower_ind == True) and ( i.isupper() == False ) ):
        print( temp, end = ', ' )
        lower_ind = False
        upper_ind = False
        temp = ""
"""


######## File Handling ######

# file_path = r"C:\Users\gauta\PycharmProjects\MachineLearning\ML Projects\4_Thyroid Test\hypothyroid.csv"
# output_folder_path = r"C:\Users\gauta\Desktop\New folder"

"""
f = open( file_path, "r" )
data = f.read()
f.close()

# print( data )
# print( type( data ) )

data = data.split( '\n' )
data.pop()

data = data[ : : -1 ] # To write the data in water image manner

print( f"len( data ) = { len( data ) } and type( data ) = { type( data ) }" )

no_of_files = 4
rows_in_each_file = len(data)//no_of_files
extra_rows_check = len(data)%no_of_files
start = 0
txt_output_file_path = output_folder_path + '\\' + f"File_in_txt.txt"
txt_f = open( txt_output_file_path, "w" )

i = 1
while( i < no_of_files + 1 ):
      csv_output_file_path = output_folder_path + '\\' + f"File_{i}.csv"
      # txt_output_file_path = output_folder_path + '\\' + f"File_{i}.txt" # To write multiple txt files

      csv_f = open( csv_output_file_path, "w" )
      # txt_f = open( txt_output_file_path, "w" )     # To write multiple txt files
      
      # print( data[ start : start + rows_in_each_file  ] )      
      # print()

      for j in data[ start : start + rows_in_each_file  ]:
            csv_f.write( j + "\n" )
            txt_f.write( j + "\n" )         # Normal data write
            # txt_f.write( j[::-1] + "\n" ) # Mirror Image data write

      start = start + rows_in_each_file

      csv_f.close()
      # txt_f.close()     # To write multiple txt files

      i = i + 1

txt_f.close()     # To write Single txt files

# Code to Check extra lines Start
if( extra_rows_check > 0 ):
      csv_output_file_path = output_folder_path + '\\' + f"File_{i-1}.csv"

      # # To write in last file in case of multiple txt files
      # txt_output_file_path = output_folder_path + '\\' + f"File_{i-1}.txt"

      # To write in txt file in case of Single txt files
      txt_output_file_path = output_folder_path + '\\' + f"File_in_txt.txt"

      csv_f = open( csv_output_file_path, "a" )
      txt_f = open( txt_output_file_path, "a" )
      
      # print( data[ start : ] )
      
      for j in data[ start : ]:
            csv_f.write( j + "\n" )
            # txt_f.write( j + "\n" )
            txt_f.write( j[::-1] + "\n" )

      csv_f.close()
      txt_f.close()
# Code to Check extra lines End

"""

########## Json File Handling ############
# file_path = r"C:\Users\gauta\PycharmProjects\Python_Concept_Gautam\Json\DUMMY_JSON_DATA.json"

"""
import json

f = open( file_path, "r" )
# data = f.read()
data = json.load(f)

f.close()

# print( data )
# print( type(data) )

for i in data.values():
      # print( i )

      if( "TV" in i['hobbies'] ):
            print( i["Name"] )
            i['hobbies'].append( "Music" )

      print( i )

"""
# f = open( r"C:\Users\gauta\Desktop\New folder\Output_Json_Data.json", "w" )
"""
json.dump(data, f, indent = 4 )
# f.write( str( data ) )
f.close()
"""


########## Functions ##################

# Function = Function is variable which holds statements and arguments

"""
a = 2
print(a)  # 2

a = 3
print(a)  # 3

def f():
      print( "Hello" )
      a = 2
      print(a )
      print( a + 4 )


f()
print()
print()

def f():
      print( "New Specification " )


f()
"""

"""
def f(a):
      
      print( f"Before, f(), a = {a}" )
      a = a * 5
      print( f"After, f(), a = {a}" )

      # return "Hello", 10, 45, a
      return a

op = f(2) # "Hello", 10, 45
# op, op1, op2 = f(2) # "Hello", 10, 45

print( f"op = {op} and type( op ) = { type( op ) }" )
"""

"""
def add( num1, num2 ):
      print( f"add() : num1 = { num1 } and num2 = {num2}" )

      return num1+num2

def add( num1, num2, num3 ):
      print( f"add() : num1 = { num1 } and num2 = {num2} and num3 = { num3 }" )

      return num1+num2+num3

add( 2, 5, 6 )

add(2, 5 )
"""

"""
def add( *nums ): # nums = ()
      print( f"nums = {nums} and type( nums ) = { type( nums ) }" )
      total = 0

      for i in nums:
            total = total + i

      return total

op = add(2, 3, 6)
print( f"op = {op} and type( op ) = { type( op ) }" )
"""


############ Types of Arguments ################

# 1) Requirement Argument
"""
def f1(a, b):
      print( f"f1() : a = {a} and b = {b}" )

f1(2, 3, 45)
"""

# 2) Default Argument
"""
def f1(a, b = 0): # a, b = 2, 3
      print( f"f1() : a = {a} and b = {b}" )

f1(2, 3, 4)
"""

"""
def add( num1, num2, num3 = 0 ):
      print( f"add() : num1 = { num1 } and num2 = {num2} and num3 = { num3 }" )

      return num1+num2+num3

op = add( 2, 5, 3)
print( f"op = {op} and type( op ) = { type( op ) }" )
"""

# 3) Positional Arguments
"""
def add( num1, num2, num3 = 0 ):
      print( f"add(), Before : num1 = { num1 } and num2 = {num2} and num3 = { num3 }" )
      # O/p :- add(), Before : num1 = 2 and num2 = 5 and num3 = 3

      num1 = num1 * 2
      num2 = num2 * 3
      num3 = num3 * 4

      print( f"add(), After : num1 = { num1 } and num2 = {num2} and num3 = { num3 }" )
      # O/p :- add(), After : num1 = 4 and num2 = 15 and num3 = 12

      return num1+num2+num3

# op = add( 2, 5, 3) # O/p :- op = 31 and type( op ) = <class 'int'>

# op = add( 5, 2, 3)
op = add( num2 = 5, num1 = 2, num3 = 3)
print( f"op = {op} and type( op ) = { type( op ) }" )
"""


# 4)  Variable Length Arguments
# Args -> arguments -> *
# Kwargs = Kw-args = keyword argument
"""
def add( a, b, c = 0, *nums ): # nums = ()
      print( f"a = {a}, b = {b} and c = {c}" )
      print( f"nums = {nums} and type( nums ) = { type( nums ) }\n" )
      total = a+b+c

      for i in nums:
            total = total + i

      return total

# op = add(2, 3)
# op = add(2, 3, 5)
op = add(2, 3, 5, 6, 9, 10, 22)
print( f"op = {op} and type( op ) = { type( op ) }" )
"""

"""
def add( a, b, c = 0, *nums, **d_nums ): # nums = ()
      print( f"a = {a}, b = {b} and c = {c}" )
      print( f"nums = {nums} and type( nums ) = { type( nums ) }\n" )
      print( f"d_nums = {d_nums} and type( d_nums ) = { type( d_nums ) }\n" )
      total = a+b+c

      for i in nums:
            total = total + i

      for i in d_nums.values():
            total = total + i

      return total

# op = add(2, 3)
# op = add(2, 3, 5)
# op = add(2, 3, 5, 6, 9, 10)
op = add(2, 3, 5, 6, 9, e = 10, f = 22)
print( f"op = {op} and type( op ) = { type( op ) }" )
"""

"""
def pascal( n=0 ):
      currList = []
      
      if( n == 0 ):
            return "Not Possible as n = 0"
      
      elif( n == 1 ):
            currList = [1]

      else:
            currList = pascal(n-1) # currList = [1]
            
            prevList = currList.copy() # prevList = []
            
            currList = [1]          # currList = [1]

            for i in range( len(prevList) - 1 ):
                  currList.append( prevList[i] + prevList[i+1] )

            currList.append( 1 )

      print( currList )

      return currList

pascal( 4 )
"""

"""
[ 2, 2, 2, 2, 2, 6, 9, 6, 10, 10, 2, 2, 4, 7 ]
[ 2, 2, 2, 6, 9, 6, 10, 2, 4 ]
[ 2, 2, 6, 9, 6, 10, 2, 4 ]
[ 2, 6, 9, 6, 10, 2, 4 ]
"""

"""
# I/p :- abc
# O/p :- abc, acb, bac, bca, cab, cba

data = [ 2, 2, 2, 2, 2, 6, 9, 6, 10, 10, 2, 2, 4, 7 ]

def removePairs( data ):
      print( data )

      temp = []
      i = 0
      while( i < len( data ) ):
            
            if( (i < len(data)-1) and  (data[i] == data[i+1]) ):
                  i = i + 1

            temp.append( data[i] )

            i = i + 1

      if( temp == data ):
            return 

      data = temp.copy()

      removePairs( data )
      
removePairs( data )
"""

"""
# 'b' -> ['b']
# 'c' -> ['c']

# 'bc' -> [ 'b' * ['c'], 'c' * ['b'] ]

# 'abc' -> [ 'a' * 'bc', 'b' * 'ca' , 'c' * 'ab' ]

def possibilities( chars, op = [] ):
      if( len( chars ) == 1 ):
            return chars
      else:            
            i = 0
            while( i < len( chars ) ):
                  currChar = chars[i]

                  nextIterChar = chars[ : i ] + chars[i+1:]
                  print( f"currChar = {currChar} and nextIterChar = {nextIterChar}" )

                  output = possibilities( nextIterChar )
                  print( f"output = {output}" )
                  
                  for j in output:
                        op.append( currChar + j )

                  op.append( currChar + output[0] )
                  
                  i = i + 1

data = "abc"
data = list( data )

outcome = []
possibilities( data, outcome )
print( outcome )
"""

"""
def checkPalindrome(s):
    return s == s[::-1]

def getPalindromePartitions(s,i):
    if i>=len(s):
        return [""]
    partitions=[]
    j=i
    while(j<len(s)):
        t=s[i:j+1]
        print( f"i = {i}, j = {j}, j+1 = {j+1}, s = {s} and t = {t}" )
        
        if checkPalindrome(t):
            
            newPartitions = getPalindromePartitions(s, j+1)

            print( f"\tnewPartitions = { newPartitions }" )
            
            for p in newPartitions:
                k=[t]
                k.extend(p)
                partitions.append(k)
                print( f"\t\t t = {t} , k = {k}" )

            print( f"partition = {partitions}\n" )
                
        j+=1
    return partitions

s="nitin"
l=getPalindromePartitions(s,0)
print(l)
"""

# 1) stringifyNumbers,
"""
I/P    :- {'num': 1, 'test': [], 'data': {'val': 4, 'Info': {'isRight': True, 'random': 66}}}

O/P :- {'num': '1', 'test': [], 'data': {'val': '4', 'Info': {'isRight': True, 'random': '66'}}}


def stringifyNumbers(obj):
      for i, j in obj.items():
            print( f"i = {i} and j = {j}" )
            
            if( isinstance( j, int) or isinstance( j, float) ):
                  obj[i] = str( j )
            elif( isinstance( j, dict) ):
                  obj[i] = stringifyNumbers( j )

      return obj

obj = {
    "num" : 1,
    "test" : [],
    "data" : {
        "val" : 4,
        "Info" : {
            "isRight" : True,
            "random" : 66
        }
    }
}

print( obj )
print()
print()
print( stringifyNumbers( obj ) )
"""

# 2) nestedEvenSum
"""
I/P :- {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

O/P :- 10


def nestedEvenSum(obj, sum=0):

  if( isinstance( obj, dict ) == False ):
    return 0

  for i, j in obj.items():

    if( isinstance( j, int) or isinstance( j, float) ):
      if( j%2 == 0 ):
        sum = sum + j

    elif( isinstance( j, dict) ):
      sum = nestedEvenSum( j, sum )

  return sum

obj = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 12}, "ee": 'car'}
}
op = nestedEvenSum( obj )
print( f"op = { op }" )
"""

# 3) Flatten the list data,

"""
I/P :- [1, 2, 3, [4, 5], [6] ]
O/p :- [1, 2, 3, 4, 5, 6]


def flatten(arr):
    if( isinstance( arr, list ) == False ):
        return arr

    temp = []

    for i in arr:
        if( isinstance( i, list ) ):
            temp.extend( flatten( i ) )
        else:
            temp.append( i )

    return temp

print( flatten( [1, 2, 3, [4, 5] ] ) )
"""

"""
name = [ 'A', 'B', 'C' ]
age = [ 25, 20, 30 ]
roll = [ 3, 5, 2 ]

name, age, roll

student 1 : name = "A", age = 25, roll = 3
student 2 : name = "B", age = 20, roll = 5
student 3 : name = "C", age = 30, roll = 2
"""


# Filter stundetns whose age is more than 20. A and C
# Syntax : class <class_name>:
"""     
            Statement1
            Statement2
            .
            .
            Statementn
"""     
"""
class Abc:
      x = 1
      y = 2

      def arithmetic(self, x, y): # obj_name = obj, x = , y =
            print( f"arithmetic() : id(self) = { id( self ) }" )
            print( f"arithmetic() : x = {x}, y = {y}, self.x = { self.x } and self.y = { self.y }" )
            print( f"arithmetic() : Sum = { x+y+self.x+self.y }" )

            
            

# Syntax of creating objects : variable/ Obj_name = class_name()

ob1 = Abc()
ob2 = Abc()

print( f"Outside : id(Abc) = { id(Abc) }" )
print( f"Outside : id(ob1) = { id(ob1) }" )
print( f"Outside : id(ob2) = { id(ob2) }\n" )

ob1.x = 10
ob1.arithmetic(2, 5) # or A.arithmetic(ob1, 2, 5)
"""

"""
class Student:
      a = 1

s1 = Student()
s2 = Student()

print( f"Before, dir(s1 ) :- \n{ dir(s1 ) }\n\n" )

# Add data in a Object_name.variable = value
s1.b = 2          

print( f"After, dir(s1 ) :- \n{ dir(s1 ) }" )
"""

"""
class Student:

      def takeInput( self, name, age, roll ): # s1, 'A', 20, 12
            print( f"takeInput() : id(self) = { id(self) }" )
            self.name = name        # s1.name = 'A'
            self.age = age         # s1.age = 20
            self.roll = age        # s1.roll = 12

      def display(self):
            print( f"display() : id(self) = { id(self) }" )
            print( f"Name = {self.name}" )
            print( f"Age = {self.age}" )
            print( f"Roll = {self.roll}\n" )

s1 = Student()
s2 = Student()

print( f"Outside : id(Student) = { id(Student) }" )
print( f"Outside : id(s1) = { id(s1) }" )
print( f"Outside : id(s2) = { id(s2) }\n" )

# s1.takeInput( 'A', 20, 12 )
s1.display()
"""

# Constructor : Constructor is also a normal function . The only extra feture is it will be
#                 called automatically when any object is created.

"""
class Student:

      def __init__( self, name, age, roll ): # s1, 'A', 20, 12
            print( f"__init__() : Constructor : id(self) = { id(self) }\n" )
            self.name = name        # s1.name = 'A'
            self.age = age         # s1.age = 20
            self.roll = age        # s1.roll = 12

      def display(self):
            print( f"display() : id(self) = { id(self) }" )
            print( f"Name = {self.name}" )
            print( f"Age = {self.age}" )
            print( f"Roll = {self.roll}\n" )

      def __del__( self ):
            print( f"__del__() : Destructor : id(self) = { id(self) }\n" )
            # self.display() # s1.display()

s1 = Student( 'A', 20, 12 )
s2 = Student( 'B', 30, 42 )

print( f"Outside : id(Student) = { id(Student) }" )
print( f"Outside : id(s1) = { id(s1) }" )
print( f"Outside : id(s2) = { id(s2) }\n" )

# s1.takeInput( 'A', 20, 12 )
s1.display()
s2.display()
"""

'''
class Student:
      
      def __init__(self, student_id, name, age, gender):
            self.id = student_id
            self.name = name
            self.age = age
            self.gender = gender

            print( f"User has been created with id : {student_id}" )

      def display(self):
            print( f"ID : {self.id}, Name = {self.name}, Age = {self.age}, Gender = {self.gender}" )

      def __del__(self):
            print( "Destructor Called " )

menu = """Student Details : 1. Create, 2. Delete, 3. Print All, 4. Print Specific
            , 5. Find Duplicates, 6. Delete Duplicates, 7. Deleted Records, 8. Exit = """

student_id = 0
student_active_dict = {}
student_disable_dict = {}

while( True ):
      op = input( menu )
      print()

      if( op == '1' ):
            name = input("Enter Student Name = ")
            age = input("Enter Student Age = ")
            if( age.isdigit() ):
                  age = int( age )
            
                  gender = input("Enter Student Gender, M : Male and F: Female = ").upper()
                  if( gender in ('M', 'F') ):
                        obj = Student( student_id, name, age, gender )
                        student_active_dict[ student_id ] = obj
                        
                        student_id = student_id + 1
                        unique_dict = {}
                        
                  else:
                        print( "Please Enter only M or F for gender option" )
            else:
                  print( "Student Details Can't be added because age is not an Integer" )

      elif( op == '2' ):
            curr_id = input( "Enter Student - Id that has to be Deleted = " )
            if( curr_id.isdigit() ):
                  curr_id = int( curr_id )
                  
                  if( curr_id in student_active_dict ):
                        student_disable_dict[curr_id] = student_active_dict.pop( curr_id )
                        print( f"Stundent - ID : {curr_id} has been deleted" )
                        unique_dict = {}
                  else:
                        print( f"Enter correct Stundent - ID" )
                        
            else:
                  print( "Please Enter only Digits as ID" )

      elif( op == '3' ):
            count = 0
            for i in student_active_dict.values():
                  i.display()
                  count = count + 1

            print( f"Total Records = { count }" )

      elif( op == '4' ):
            curr_id = input( "Enter Student - Id that has to be Printed = " )
            if( curr_id.isdigit() ):
                  curr_id = int( curr_id )
                  
                  if( curr_id in student_active_dict ):
                        student_active_dict[curr_id].display()
                  else:
                        print( f"Enter correct Stundent - ID" )
                        
            else:
                  print( "Please Enter only Digits as ID" )

      elif( op == '5' ):
            unique_dict = {}

            for i in student_active_dict.values():
                  if( (i.name, i.age, i.gender) not in unique_dict ):
                        unique_dict[ (i.name, i.age, i.gender) ] = [i.id]
                  else:
                        unique_dict[ (i.name, i.age, i.gender) ].append( i.id )

            isDuplicate = False
            for details, student_id_list in unique_dict.items():
                  if( len( student_id_list ) > 1 ):
                        isDuplicate = True
                        print( f"Name : { details[0] }, Age : { details[1] }, Gender : { details[2] }, id : {student_id_list}, count = { len( student_id_list ) }" )

            if( not isDuplicate ):
                  print( "No Duplicate Data Found" )

      elif( op == '6' ):
            if( len( unique_dict ) == 0 ):
                  print( "No Duplicate Data Found" )
            else:
                  for details, student_id_list in unique_dict.items():
                        print( f"OP : 6 : details = { details }" )
                        
                        if( len( student_id_list ) > 1 ):

                              for curr_id in student_id_list[1:]:
                                    student_disable_dict[curr_id] = student_active_dict.pop( curr_id )
                                    print( f"Duplicate Data : Stundent - ID : {curr_id} has been deleted" )

                  unique_dict = {}
            
      elif( op == '7' ):
            count = 0
            for i in student_disable_dict.values():
                  i.display()
                  count = count + 1

            print( f"Total Records = { count }" )
            
      elif( op == '8' ):
            break
      else:
            print( "Please Choose Correct Option from : 1 to 8 Only" )

      print()
'''

'''
# Decorator 
def add_one(func):
      print( f"add_one : func = { func }\n" )
      
      def wrapper(x):
            print("In add_one wrapper, before calling func")
            result = func(x) + 1
            print( f"In add_one wrapper, after calling func, result = {result}\n", )
            
            return result

      return wrapper

def add_two(func):
      print( f"add_two : func = { func }\n" )
      
      def wrapper(x):
            print("In add_two wrapper, before calling func")
            result = func(x) + 2
            print( f"In add_two wrapper, after calling func, result = {result}\n", )
            
            return result

      return wrapper

def add_three(func):
      print( f"add_three : func = { func }\n" )
      
      def wrapper(x):
            print("In add_three wrapper, before calling func")
            result = func(x) + 3
            print( f"In add_three wrapper, after calling func, result = {result}\n", )
            
            return result

      return wrapper

@add_one
@add_two
@add_three
def add(x):
    return x

print( f"Outside : add = { add }\n" )
print( add(0) )
'''

"""
class A:
      def add( self, num1, num2 ):
            print( f"A : add() : id(self) = {id(self)}" )
            return num1 + num2
      
class B(A):
      def add_A( self, num1, num2 ):
            print( f"Before, B : add_A : id(self) = {id(self)}" )
            op = super().add( num1, num2 ) # super() = A
            print( f"After, B : add_A : op = { op }\n" )
      
      def add( self, num1, num2, num3 ):
            print( f"B : add() : 3 args : id(self) = {id(self)}" )
            return num1 + num2 + num2
      
oba = A()
obb = B()

print( f"id(oba) = { id(oba) }" )
print( f"id(obb) = { id(obb) }\n" )

op = oba.add( 2, 5)
print( f"op = {op}\n" )

op = obb.add( 2, 5, 7 )
print( f"op = {op}\n" )


op = obb.add_A( 2, 5 )
print( f"op = {op}\n" )
"""

"""
# Inheritance Syntax :-
# class A:
      func 1
      func 2
      .
      .

# class B( class_name1 ):
      func 1
      func 2
      .
      .
"""

"""
class A:
      def add( self, num1, num2 ):
            print( f"A : add() : id(self) = {id(self)}" )
            print( f"A : add() : Total = { num1 + num2 }\n" )

class B:
      def add( self, num1, num2 ):
            print( f"B : add() : id(self) = {id(self)}" )
            print( f"B : add() : Total = { num1 + num2 }\n" )
            
      def sub( self, num1, num2 ):
            print( f"B : sub() : id(self) = {id(self)}" )
            print( f"B : sub() : Total = { num1 - num2 }\n" )

class C(A, B):
      def add_A( self, num1, num2 ):
            print( f"C : add_A() : id(self) = {id(self)}" )
            super().add( num1, num2 )
            
      def mult( self, num1, num2 ):
            print( f"C : mult() : id(self) = {id(self)}" )
            print( f"C : mult() : Total = { num1 * num2 }\n" )



oba = A()
obb = B()
obc = C()

obc.add(2, 3)
obc.add_A(2, 3)
"""

# Types of Inheritance

# Simple  :  A -> B
# Multiple : A, B, C -> D
# Hierarchical : A -> B, C, D
# Multi-Level : A -> B -> C
# Hybrid/ Diamond : A -> B, C -> D

# Abstract Class and Polymerphism

"""
from abc import ABC, abstractmethod

class Arithmetic(ABC):
# class Arithmetic():

      @abstractmethod
      def add( self ):
            pass
      
      @abstractmethod
      def sub( self ):
            pass

      @abstractmethod
      def mult( self ):
            pass

      @abstractmethod
      def div( self ):
            pass

class Twodigit( Arithmetic ):
      def add( self, num1, num2 ):
            print( f"Twodigit : add() : Total = { num1 + num2 }" )
            
      def sub( self, num1, num2 ):
            print( f"Twodigit : sub() : Total = { num1 - num2 }" )

      def mult( self, num1, num2 ):
            print( f"Twodigit : mult() : Total = { num1 * num2 }" )

      def div( self, num1, num2 ):
            print( f"Twodigit : div() : Total = { num1 / num2 }" )

class Threedigit( Arithmetic ):
      def add( self, num1, num2, num3 ):
            print( f"Threedigit : add() : Total = { num1 + num2 + num3 }" )

      def sub( self, num1, num2, num3 ):
            print( f"Threedigit : sub() : Total = { num1 - num2 - num3 }" )

      def mult( self, num1, num2, num3 ):
            print( f"Threedigit : mult() : Total = { num1 * num2 }" )

      def div( self, num1, num2, num3 ):
            print( f"Threedigit : div() : Total = { num1 / num2 }" )

# oba = Arithmetic()
obtwo = Twodigit()

# obtwo.add( 2, 5 )
"""

"""
# Table : Student
# Col : student_id, name, age

class Student:
      name = "A"
      __age = 21

      def get_age( self, name ):
            # print( f"name = { name }" )
            
            print( f"self.name = { self.name }" )
            print( f"self.__age = { self.__age }\n" )

      def set_age( self, newAge ):
            self.__age = newAge
      

s1 = Student()

s1.get_age( "Hello" )
s1.set_age( 5 )
s1.get_age("Hi")
"""

"""
class A:

      x = 1
      y = 2

      def f1(self, val):
            print( f"f1() : id(self) = { id(self) }" )
            print( f"Before, self.x = { self.x }" )
            self.x = val
            print( f"After, self.x = { self.x }\n" )

      @classmethod
      def f2( self, val ):
            print( f"f2() : id(self) = { id(self) }" )
            print( f"Before, self.x = { self.x }" )
            self.x = val
            print( f"After, self.x = { self.x }\n" )

      @staticmethod
      def f3( self ):
            print( f"f3() : self = { self }\n" )
            print( f"f3() : id(self) = { id(self) }\n" )

ob1 = A()
ob2 = A()

print( f"Outside : id(A) = { id(A) }" )
print( f"Outside : id(ob1) = { id(ob1) }" )
print( f"Outside : id(ob2) = { id(ob2) }\n" )

print( f"1. A.x = { A.x }, ob1.x = { ob1.x } and ob2.x = { ob2.x }" )
print( f"1. A.y = { A.y }, ob1.y = { ob1.y } and ob2.y = { ob2.y }\n" )

ob1.f1( 10 )

print( f"2. A.x = { A.x }, ob1.x = { ob1.x } and ob2.x = { ob2.x }" )
print( f"2. A.y = { A.y }, ob1.y = { ob1.y } and ob2.y = { ob2.y }\n" )

ob1.f2( 100 )

print( f"3. A.x = { A.x }, ob1.x = { ob1.x } and ob2.x = { ob2.x }" )
print( f"3. A.y = { A.y }, ob1.y = { ob1.y } and ob2.y = { ob2.y }\n" )

ob1.f3(5)
"""

"""
# Magic Functions/ Dender methods -> __functions_name__

class A:
      x = 1
      y = 2

      def __init__(self):
            print( f"A Const." )

      def __add__(self, num):
            print( f"A __add__, self = {self} and num = {num}\n" )
            # return 1+num

      def __sub__(self, num):
            print( f"A __sub__, self = {self} and num = {num}\n" )
            # return 1+num

      # def __str__(self):
      #       # print( f"A __str__\n" )
      #       print( f"x = { self.x } and y = { self.y }" )
      #       return ""

      def __gt__( self, num ):
            print( f"A : __gt__ self = { self } and num = { num }" )

      

ob1 = A()

# ob1 + 5
# ob1 - 5

print( f"OP = { ob1 }" )
# ob1.__str__()

ob1 > 5
"""


####### Exception/ Error Handling #########

# Component of Exception Handling
# 1) try
# 2) except
# 3) else
# 4) finally
# 5) raise
# 6) assert

"""
L = [ 1, 2, 10, 8, 0, 3 ]

for i in L:
      try:
            print(  "Try : ", i, 1/i )
      except:
            print( f"Except : Error Occured when i = {i}" )
      else:
            print( f"Else : i = {i}" )

      finally:
            print( f"Finally : i = {i} Processed" )

      print()
"""

"""
# Data base Connection using Python

try:
      # Writing and running a query1 using Python -> Proper
      # Writing and running a query2 using Python -> Throws Error
except:
      # If anything goes wrong
      # rollback()
else:
      # commit()
finally:
      close connection
"""

"""
try:
      # print(1/0)        # ZeroDivisionError: division by zero
      L = []
      # print( L[0] )       # IndexError: list index out of range
      # print(a)            # NameError: name 'a' is not defined

      # d = {}
      # print( d[1] )

      f = open( r"C:\ABCD" )
except ZeroDivisionError as e:
      print( f"ZeroDivisionError : Error Occured = {e}" )

except IndexError as e:
      print( f"IndexError : Error Occured = {e}" )

except NameError as e:
      print( f"NameError : Error Occured = {e}" )

except Exception as e:
      print( f"Error Occured = {e}" )
"""

"""
try:
      L = [ 10, 4, -4, 5 ]

      for i in L:
            '''
            if( i < 0 ):
                  raise Exception( f"Throwing Error because i = {i} is -ve" )
            else:
                  print( i )
            '''
            assert i >= 0, f"Throwing Error because i = {i} is -ve"

            print( i )
            
except Exception as e:
      print( f"Error Occured = {e}" )
"""

######### Modules ###########

"""
class sc:
      pass

sc = A()

def add( num1, num2):
      print( f"Sigmoid Coding : add() : Total = { num1 + num2 }" )
      return num1+num2

sc = 1

print( f"Sigmoid : __name__ = { __name__ }" )

if( __name__ == '__main__' ):
      add(2, 5 )
"""

"""
########### Test.py ###########
import sys

print( type( sys ) )
# print( sys.path )
sys.path.append( 'C:\\Users\\gauta\\Desktop' )

import Sigmoid_Coding as sc

class sc:
      pass

sc.add(12, 15 )
print( f"sc.sc = { sc.sc }" )

print( f"Test : __name__ = { __name__ }" )
"""

################ Regular Expression ############### 

