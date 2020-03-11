import re

def text_match( text ):
    pattern = '[a-z][A-Z][0-9]'

    if( re.search(pattern, text) ):
        return 'Found a Match'

    else:
        return 'Not Matched'

print( text_match("aab_cbbbc") )
print( text_match("aab_Abbbc") )
print( text_match("Aaab_abbbc") )
print( text_match("aabA1_abbbc") )