import re

mystr='send an Email 6789 from HELLO this@gmail.com To test@user.com 34 times !879'

#Selecting one character

#syntax  :-  re.findall( 'what_to_find', 'Where_to_find')

print( f"mystr = { mystr }" )

print( f"re.findall('a', mystr) = { re.findall('a', mystr) }", end = ', ' )#Find all by 'a'
print( f"len( re.findall('a', mystr) ) = { len( re.findall('a', mystr) ) }" )

print()
print("\d = ",end='')
print( re.findall('\d',mystr) )# finds the positions of all available digits in string

print()
print("\D = ",end='')
print( re.findall('\D',mystr) )# finds the positions of all available non - digits in string

# '^' Sign
print()
print("^\d = ",end='')
print( re.findall('^\d',mystr) )# finds the positions of all available digits in strings

# '$' Sign
print()
print("\d$ = ",end='')
print( re.findall('\d$',mystr) )# finds the positions of all available digits in string

print()
print("^\d$ = ",end='')
print( re.findall('^\d$',mystr) )# finds the positions of all available digits in string

# '+' Sign
print()
print("\d+ = ",end='')
print( re.findall('\d+',mystr) )# finds the positions of all available digits in string

print()
print("\D+ = ",end='')
print( re.findall('\D+',mystr) )# finds the positions of all available non - digits in string

print()
print("\s = ",end='')
print( re.findall('\s', mystr) )#Doesn't finds the positions but shows all available spaces in string

print()
print("\S = ",end='')
print( re.findall('\S', mystr) )#Doesn't finds the positions but shows all available non - space in string

print()
print("\W = ",end='')
print( re.findall('\W',mystr) )#Doesn't finds the positions but shows all available characters in string

print()
print("\w = ",end='')
print( re.findall('\w', mystr) )#Doesn't finds the positions but shows all available non - characters in string

#Selecting Range of Charaters

print()
print( f"[a-z] = {re.findall('[a-z]', mystr) }" )   #find all elements between a-z

print()
print(f"[A-Z] = {re.findall('[A-Z]', mystr) }" )      #find all elements between A-Z

print()
print(f"[0-9] = {re.findall('[0-9]', mystr) }" )      #find all elements by 0-9

print()
print(f"[0-9]+ = {re.findall('[0-9]+', mystr) }" )      #find all elements by 0-9

#Selecting Non - Range of Charaters

print()
print(f"^[a-z] = {re.findall('^[a-z]', mystr) }" )      #find all elements by non a-z range

print()
print(f"^[a-z]+ = {re.findall('^[a-z]+', mystr) }" )      #find all elements by non a-z range

print()
print(f"[^a-z] = {re.findall('[^a-z]', mystr) }" )      #find all elements by non a-z range

print()
print(f"[^A-Z]+ = {re.findall('[^A-Z]+', mystr) }" )      #find all elements by non A-Z range

print()
print(f"^[^a-z] = {re.findall('^[^a-z]', mystr) }" )      #find all elements by non a-z range

print()
print(f"^[^A-Z] = {re.findall('^[^A-Z]', mystr) }" )      #find all elements by non A-Z range

print()
print(f"^[^a-z]+ = {re.findall('^[^a-z]+', mystr) }" )      #find all elements by non a-z range

print()
print(f"^[^A-Z]+ = {re.findall('^[^A-Z]+', mystr) }" )      #find all elements by non A-Z range