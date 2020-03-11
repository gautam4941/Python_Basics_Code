class A:
    a = 5            #Public Variable
    b = 6            #Public Variable
    __c = 9          #Private Variable
    _d = 4           #Protected Varaible

    def f1(self):
        return self.__c

    def f2(self, num):
        self.__c = num

ob = A()
ob2 = A()

print( f"ob.a = { ob.a }" )
print( f"ob.b = { ob.b }" )
#print( f"ob._c = { ob.c }" )
#print( f"ob.__c = { ob.__c }" )

# print( f"Before Change,ob get c = { ob.f1() }" )
# print( f"Before Change,ob2 get c = { ob2.f1() }" )
# ob.f2( 0 )
# print( f"After Change, ob get c = { ob.f1() }" )
# print( f"After Change, ob2 get c = { ob2.f1() }" )


class B( A ):

    def test(self):
        print( f"super().a = { super().a }" )
        print( f"super().b = { super().b }" )
        print( f"super()._d = { super()._d }" )
        #print( f"super().__c = { super().__c }" )

obb = B()
obb.test()

#print( f"obb.x = { obb.x }" )

#print( f"obb._d = { obb._d }" )

#Public :- Normal Class or Object Varaible are public varaiables
            #EX : a = 5
    #Public variables can be used in other classes and it can be used outside of class( es ).

#Proteted :- variable having single Underscore( _ )before name are protected variables.
            #EX : _a = 5
    #Protected variables cannot be used in other classes but it can be used outside of class( es ).

#Private :- variable having double Underscore( __ )before name are protected variables.
            #EX : __a = 5

    #Private variables cannot be used in other classes and it cannot be used outside of class( es ) also.