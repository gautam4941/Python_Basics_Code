import re

mystr='send an email 6789 from this@gmail.com to test@user.com 34 times'

#Selecting one character

#Syntax :-   re.sub( 'old_sub_str', 'new_sub_str', main_str  )
#            re.sub( 'what to replace', 'new string', from_where_tro_replace )

print( re.sub('a', '&', mystr) )

print( re.sub('\d', '*', mystr) )# finds the positions of all available digits in string

print( re.sub('\d+', '*', mystr) )# finds the positions of all available digits in string

print( re.sub('\W', '*', mystr) )