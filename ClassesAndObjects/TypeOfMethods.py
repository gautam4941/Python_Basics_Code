"""
Types of Method in class,

i) Instance/Object Methods
ii) Class Methods
iii) Static Methods
"""

class Person:
    def __init__(self, message ):
        print(f"Inside __init__(), Message :- {message} and self = { self }\n")
        self.message = message

        # a class method to create a Person object by birth year.

    @classmethod
    def a(cls, message):
        print( f"Inside a(), Message :- { message } and cls = { cls }" )
        return cls( message )

        # a static method to check if a Person is adult or not.

    @staticmethod
    def b( message ):
        print( f"Inside b(), Message :- { message }" )


person1 = Person( 'MESSAGE :- PERSON1' )
person2 = Person.a('MESSAGE :- PERSON2')

print( f"Outside person1 = { person1 }" )
print( f"Outside person2 = { person2 }\n" )

print( f"person1.message = { person1.message }" )
print( f"person2.message = { person2.message }" )

# print the result
print()
Person.b(22)
person1.b( 22 )
person2.b( 22 )

"""
1) A class method takes cls as first parameter while a static method needs no specific parameters.
2) A class method can access or modify class state while a static method can’t access or modify it.
3) In general, static methods know nothing about class state. 
    They are utility type methods that take some parameters and work upon those parameters. 
    On the other hand class methods must have class as parameter.

4) We use @classmethod decorator in python to create a class method and we use @staticmethod decorator
    to create a static method in python.
"""