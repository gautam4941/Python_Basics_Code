"""
#Introduction to Strings,
msg = "Hello, Ram"

print( f"msg = { msg }" )
print( f"msg[2] = { msg[2] }" )
print( f"msg[0] = { msg[0] }" )
print( f"msg[5] = { msg[5] }" )
print( f"msg[9] = { msg[9] }" )
#print( f"msg[10] = { msg[10] }" )

print( f"len(msg) = { len(msg) }" )              #To Find the Length of any dataset, use :- len( dataset_name )
print( f"Last index : len(msg) - 1 = { len(msg) - 1 }" )
print( f"msg[ len(msg) - 1 ] = {msg[ len(msg) - 1 ]}" )     #msg[ index ]
#print( f"msg[ len(msg) ] = { msg[ len(msg) ] }" )
"""

"""
msg = "Hello, Ram"
#index 0123456789
#len             ->10
                                           #Work Variable
for i in range( 0, len( msg ) ):    #0,1, 2, .., 9          #i is loop variable
    print( i, msg[i])

print()
print()

for i in range( len( msg )-1 , -1, -1 ):
    #print( f"i = { i } and msg[ i ] = { msg[ i ] }" )
    print(i, msg[i] )
"""

"""
#Capitalize()
#Syntax :- String_name.capitalize()

word = "hello, How are you. Hello ?"
substr = "Hello"

print( word.capitalize() )
print( substr.capitalize() )
"""

"""
#center()

word = "Hello"


#O/p :-        Hello

# print( word.center( 8 ) )

for i in range(1, 9):
    print(" ", end = '' )

print( word, end = '' )

for i in range(1, 9):
    print(" ", end = '' )
"""

"""
#Count()
#print( word.count( substr ) )

#Syntax :- dataset_variable/Dataset.count( character/String )
word = "Hello, How are you. Hello ?"


print( f"word.count( 'H' ) = { word.count( 'H' ) }" )
print( f"word.count( 'He' ) = { word.count( 'He' ) }" )
print( f"word.count( 'll' ) = { word.count( 'll' ) }" )
print( f"word.count( 'o' ) = { word.count( 'o' ) }" )
print( f"word.count( ' ' ) = { word.count( ' ' ) }" )
print( f"word.count( 'are' ) = { word.count( 'are' ) }" )
print( f"word.count( 'z' ) = { word.count( 'z' ) }" )
"""

"""
#encode()
#Syntax :- dataset.encode( encoding = "ascii", errors = error_name )

print( f"word = { 'Ståle' }" )
print( f"Ståle.encode() = { 'Ståle'.encode() } and å = { 'å'.encode() }" )
print( "Hello".encode(encoding="ascii",errors="backslashreplace") )
print( "Ståle".encode(encoding="ascii",errors="backslashreplace") )
print("Ståle".encode(encoding="ascii",errors="ignore"))
print("Ståle".encode(encoding="ascii",errors="namereplace"))
print("Ståle".encode(encoding="ascii",errors="replace"))
print("Ståle".encode(encoding="ascii",errors="xmlcharrefreplace"))
#print("Ståle".encode(encoding="ascii",errors="strict"))
"""

"""
#EndsWith()

word = "Hello, How are you. Hello ?"
substr1 = "Hello"
substr2 = "Hello ?"
substr3 = "lo ?"

print( f"word = { word }" )
print( f"substr1 = { substr1 }" )
print( f"substr2 = { substr2 }" )
print( f"substr3 = { substr3 }" )
print( f"{ word }.endswith({ substr1 }) = { word.endswith(substr1) }" )
print( f"word.endswith(substr2) = { word.endswith(substr2) }" )
print( f"word.endswith(substr3) = { word.endswith(substr3) }" )

#Startwith()
print( f"word.startswith(substr1) = { word.startswith(substr1) }" )
print( f"word.startswith(substr2) = { word.startswith(substr2) }" )
print( f"word.startswith(substr3) = { word.startswith(substr3) }" )
"""

"""
#find()
#Syntax :- Main_String.find(substr, start_location)
#If location not given, then by default location will be 0.

word = "Hello, How are you He?"
substr = "He"

firstind = word.find(substr)

print(f"First Index of { substr } = { firstind }")

firstind = word.find(substr, 0)

print(f"First Index of { substr } = { firstind }")

secondind = word.find(substr, firstind + 1)

print( f"Second Index of { substr } = { secondind}" )

thirdind = word.find(substr, secondind + 1)

print( f"Third Indes of { substr } = { thirdind }" )

fourthind = word.find(substr, thirdind + 1)

print( f"Fourth Indes of { substr } = { fourthind }" )

fifthind = word.find(substr, fourthind + 1)

print( f"Fifth Indes of { substr } = { fifthind }" )
"""

"""
word = "Hello,How aRe you ?"

print( f"Title of { word } = { word.title() }" )

print(f"Length of { word } = { len( word ) }")

print( f"Upper of { word } = { word.upper() }"  )

print(f"Lower of { word } = { word.lower() }"  )
"""

"""
#Rule for title() -> First letter of each word must be in Upper case and in the middle no upper should be there
#  in a string.
word1 = "This Is Vss Institute"
word2 = "ThisIsVssinsTItu123te"
substr1 = 'Thisisvssinstitute123'
substr2 = 'is Vss'

print(f"istitle of { word1 } = { word1.istitle() }" )
print(f"istitle of { word2 } = { word2.istitle() }" )
print(f"istitle of { substr1 } = { substr1.istitle() }" )
print(f"istitle of { substr2 } = { substr2.istitle() }" )
"""

"""
#replace()
#Syntax :- Main_string.replace( old_sub_str, new_sub_str )

message = "Hello, My name is Shirak and i never bring pen"

print( f"message = { message }" )

print( f"message.replace( 'Shirak', 'lakshita' ) = { message.replace( 'Shirak', 'lakshita' ) }" )

print( f"message = { message }" )

message = message.replace( 'Shirak', 'lakshita' )

print( f"message = { message }" )
"""

"""
message = "Hello, How are you ?"

print( f"message.isalpha() = { message.isalpha() }" )
print( f"message.isdigit() = { message.isdigit() }" )
print( f" '67.8'.isdigit() = { '67.8'.isdigit() }" )
print( f" '678'.isdigit() = { '678'.isdigit() } " )
print( f"message.istitle() = { message.istitle() }" )
print( f"message.isspace() = { message.isspace() }" )
print( f"message.isalnum() = { message.isalnum() }" )
print( f" '678'.isalnum() = { '678'.isalnum() } " )
print( f"'678dasdad'.isalnum() = { '678dasdad'.isalnum() }" )
print( f"'678dasd ad'.isalnum() = { '678dasd ad'.isalnum() }" )
print( f"message.isdecimal() = { message.isdecimal() }" )
print( f" '67.8'.isdecimal() = { '67.8'.isdecimal() }" )
print( f" '678'.isdecimal()  = { '678'.isdecimal()  } " )
print( f" '678'.islower() = { '678'.islower() } " )
print( f" '67.8'.islower() = { '67.8'.islower() } " )
print( f" message.islower() = { message.islower() } " )
print( f" '678'.isupper() = { '678'.isupper() } " )
print( f" message.isupper() = { message.isupper() } " )
print( f" message.upper().isupper() = { message.upper().isupper() } " )
"""


#Split() and join()
#Syntax :- String_var.split( substring ) -> It return, the value into list.

message = "Hello, My name is Anu and I am studying python in VSS with Sumant and Anand (VSS)"

l = message.split('')

print( f"message = { message }" )
print( f"l = { l }" )
print( f"len(l) = { len(l) }" )
print( f"len(l) - 1 = { len(l) - 1 }" )
print( f"l[ len(l) - 1 ] = l[ { len(l) - 1 } ] = { l[ len(l) - 1 ] }" )

joinlist = '*'.join( l )

print( f"'*'.join( l ) = { joinlist }" )


"""
#Slicing
#Syntax :- data_set[ start_index : end_index : incr/dec  ]

msg = "Hello, How are you ?"

print( f"msg = { msg }" )
print( f"len( msg ) = { len( msg ) }" )
print()
print( f"msg[ 0 : len(msg) : 1 ] = { msg[ 0 : len(msg) : 1 ] }" )
print( f"msg[ 0 : len(msg) :  ] = { msg[ 0 : len(msg) :  ] }" )
print( f"msg[ : len(msg) :  ] = { msg[ : len(msg) :  ] }" )
print( f"msg[ : :  ] = { msg[ :  :  ] }" )
print( f"msg[ : : 1 ] = { msg[ :  : 1 ] }" )
print( f"msg[ : : -1 ] = { msg[ :  : -1 ] }" )

l = [ 6, 7, 8, 9 ]
print( f"Reverse of list = l[  :  : -1 ] = { l[  :  : -1 ] }" )
"""