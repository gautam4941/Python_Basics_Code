import re

phn = "432-555-1221 434-555-1221 are my codes to access"

print( re.findall("\d",phn) )

print( re.findall("\d+",phn) )

print( re.findall("\d+-\d+-\d+",phn) )