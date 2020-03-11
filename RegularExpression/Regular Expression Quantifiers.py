"""
+, ?, *, { m }, { m, n }
"""

import re

mystr='send an Email 6789 from HELLO this@gmail.com To test@user.com 34 times !879'

print( re.findall( "[a-z]", mystr ) )
print()
print( re.findall( "[a-z]?", mystr ) )
print()
print( re.search( "[a-z]?", mystr ) )
print()
print( re.search( "Email", mystr, re.M|re.I ) == True)
print()
print( re.M, re.I, re.A, re.S, re.T, re.U, re.X )
print( re.match( "Email", mystr, re.M|re.I ) == True)
print()