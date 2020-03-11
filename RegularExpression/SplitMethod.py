import re

mystr='786send an Email 6789 from this@gmail.com To test@user.com 34 times !879'

#Selecting one character

print( re.split('a', mystr) )#Find all by 'a'

#\d = ['send an email ', '', '', '', ' from this@gmail.com to test@user.com ', '', ' times']
print("\d = ",end='')
print( re.split('\d',mystr) )# finds the positions of all available digits in string

print("\D = ",end='')               #/D or [ ^0-9 ]
print( re.split('\D',mystr) )# finds the positions of all available non - digits in string

print("\s = ",end='')
print( re.split('\s', mystr) )#Doesn't finds the positions but shows all available spaces in string

print("\S = ",end='')
print( re.split('\S', mystr) )#Doesn't finds the positions but shows all available non - space in string

print("\W = ",end='')
print( re.split('\W', mystr) )#Doesn't finds the positions but shows all available characters in string

print("\w = ",end='')
print( re.split('\w', mystr) )#Doesn't finds the positions but shows all available non - characters in string

#Selecting Range of Charaters

print( f"[0-9][0-9][a-z] = {re.split('[0-9][0-9][a-z]', mystr) }" )   #find all elements by a-z

print(f"[A-Z] = {re.split('[A-Z]', mystr) }" )      #find all elements by A-Z

print(f"[0-9] = {re.split('[0-9]', mystr) }" )      #find all elements by 0-9

#Selecting Non - Range of Charaters

print(f"[^a-z] = {re.split('[^a-z]', mystr) }" )      #find all elements by non a-z range

print(f"[^A-Z] = {re.split('[^A-Z]', mystr) }" )       #find all elements by non A-Z range