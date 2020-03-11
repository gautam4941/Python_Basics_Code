import re

#Convert the Given Message into lowerCase using Regular Expression

message = '''
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS ) WITH LMTPA;
SAT, JAN
YOU CAN
'''

uppercaseletters = re.findall('[A-Z]+', message)

characterscount = re.findall('\W+', message)

index = 1
newmessage = ''

print( f"uppercaseletters = { uppercaseletters }" )
print( f"characterscount = { characterscount }" )
print()

for i in uppercaseletters:
    newmessage = newmessage + i.lower() + characterscount[index]
    index = index + 1

print(f"New Message = \n{newmessage}")