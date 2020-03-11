message = "Hello, My name is Anu and I am studying python in VSS with Sumant and Anand ( VSS )"

#Count Total number of words

wordlist = message.split(' ')
print( wordlist )
print( f"Total number of words in Message = {len(wordlist ) - 2}" )

#Count total number of VSS, Anand, Anu & Sumant in message.

print( f"Total number of Vss in Message = {message.count('VSS')}" )       #or wordlist.count('VSS')
print( f"Total number of Anand in Message = {message.count('Anand') }" )       #or wordlist.count('Anand')
print( f"Total number of Anu in Message = {message.count('Anu') }" )       #or wordlist.count('Anu')
print( f"Total number of Sumant in Message = {message.count('Sumant') }" )       #or wordlist.count('Sumant')

#Get the output like -> Hello,*My*name*is.......

starmessage = '*'.join( wordlist )

print( starmessage )

#O/p -> "Gautam is teaching Python. Hello, My name is....

newmessage = ["Gautam", "is" ,"teaching", "python."]

newmessage =  " ".join( newmessage ) + ' '.join( wordlist )

print( newmessage )

vssindex1 = message.find('VSS')

vssindex2 = message.find( 'VSS', vssindex1+1 )

print( f"First index of VSS in Message = { vssindex1 }" )
print( f"Second index of VSS in Message = { vssindex2 }" )

wordlist.remove('VSS')
wordlist.remove('VSS')
wordlist.remove('(')
wordlist.remove( ')' )

message = ' '.join(wordlist)

print( message )