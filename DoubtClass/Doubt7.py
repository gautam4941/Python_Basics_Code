class ABCD:

    def get(self):
        return self

ob = ABCD()

a = str( ob.get() )
print( a )
print( a[10 : len(a) ].split(' ')[0] )