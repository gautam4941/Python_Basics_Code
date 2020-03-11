"""
a = 8
b = 2.2
c = True
d = 'Hello'

print(a)
print(b)
print()
print(c)
print( d )
"""

"""
#print() is printing the value and then, changing the line.

a = 8
b = 0.2
c = False
d = 'Hello'

#Method 1  - Printing Multiple Variables/Values .
print(a, b, c, d)
print()
print( 8, 0.2, False, 'Hello' )
print()
print(8, b, c, 'Hello')
"""


#Syntax : print( data, end = String )
a = 2
b = 0.2
c = False
d = 'Hello'

#Method 2
"""
#Syntax :  print( value, end = '' )

print('This is my data', end = '')
print(a , b, end = ' * ' )
print(c )
print(d )
print("Hello", end = ' && ' )
print(b )
print("Hello")
"""

"""
#This is my data -> 2 0.2**False#Hello(d)
#Hello@0.2
#Hello


#Method 3

#typeCasting -> int( value/variable ), str(), float(), bool()
#Type -> type( value/variable )

#O/p :- Santosh 5Rakesh True *7.8

a = 5
b = 'Santosh'
c = "Rakesh"
d = True
e = 7.8

print( b, a, c, d, '*', e )            #Method 1
print()
print(b, end = ' ')         #Method 2
print(a, end = '')
print( c, end = ' ' )
print(d, end = ' *')
print( e, end = '' )
print()

print( b + ' ' + str(a) + c + ' ' + str(d) + ' *' +str(e) )        #Method 3 ( String Concatination )
"""


"""
a = 5
b = 4.5
c = True
d = 'Shiv'
e = 0.234234

#O/p :- Shiv*0.234234 True#4.5 5

print( 'shiv'+'*'+str( 0.234234 )+' '+str( True )+'#'+str( 4.5 )+' '+str( 5 ) )

print( d+'*'+str(e)+" "+str(c)+'#'+str(b)+' '+str(a) )
"""

#Method 4 - f method

#O/p :- This id my data 8+2.2*True#Hello

a = 8
b = 2.2
c = True
d = 'Hello'

print( "This id my data a+b*c#d" )
print( f"This id my data a+b*c#d" )
print( f"This id my data {a}+b*c#d" )
print( f"This id my data {a+2}+{b}*c#d" )
print( f'This id my data {a}+{b}*{c}#{d}' ) #Method 4
print( f"This id my data {a}+{b}*{c}#{d}" ) #Method 4
print( 'This id my data {a}+{b}*{c}#{d}' ) #Method 4


#Hello, We are True ITRAIN@%)) 500.67 90

#print( str + str( non_str ) + str + str( non_str ) )

#str_area+ non _str_area +


#All types of Printing Together.

a = 8
b = 2.2
c = True
d = 'Hello'

#O/p :- This id my data 8+2.2+True+Hello

print("Method 1")
print( "This is my data", a, '+', b, '+', c, '+', d )   #Method 1
print()
print("Method 2")
print( "This is my data", end = ' ' )
print(a, end = '+')
print(b, end = '+')
print(c, end = '+')
print(d)
print()
print("Method 3")
print( "This is my data "+str(a) + '+' + str(b) + '+' + str(c) + '+' + d )
print()
print("Method 4")
print( f"This is my data+{a}+{b}+{c}+{d}" )