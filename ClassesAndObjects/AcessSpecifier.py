#public :-
#Syntax :- variable_name = value
#Ex ->   a = 5

#protected :-
#Syntax :-  underscore variable_name = value -->  _variable_name = value
#Ex ->   _b = 9

#private :
#Syntax :-  Underscore Underscore variable_name = value -->  __variable_name = value
#Ex ->   __c = 2

class A:
    a = 5               #public
    _b = 6              #protected
    __c = 7             #private

    def set_c(self):
         self.__c = int( input("Enter the value for c = ") )

    def get_c(self):
        return self.__c

ob = A()
ob2 = A()

print( f"ob.a = {ob.a}" )
print( f"ob._b = {ob._b}" )
print( f"ob.get_c() = { ob.get_c() }" )    #get_c() is the Function Name to set/update the private values
print()

print( f"ob2.a = {ob2.a}" )
print( f"ob2._b = {ob2._b}" )
print( f"ob2.get_c() = { ob2.get_c() }" )
print()

ob.a = 15
ob._b = 16
ob.set_c()

ob2.a = 25
ob2._b = 26
ob2.set_c()
print()
print( f"ob.a = {ob.a}" )
print( f"ob._b = {ob._b}" )
print( f"ob.get_c() = { ob.get_c() }" )    #get_c() is the Function Name to set/update the private values
print()

print( f"ob2.a = {ob2.a}" )
print( f"ob2._b = {ob2._b}" )
print( f"ob2.get_c() = { ob2.get_c() }" )
print()
#ob.set_c()    #Set_c() is the Function Name to set/update the private values