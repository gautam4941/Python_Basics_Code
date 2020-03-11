#Ask the age of 3 persons and find who is eldest, youndest and middle aged person

p1 = int( input("Enter the age of person 1 = ") )
p2 = int( input("Enter the age of person 2 = ") )
p3 = int( input("Enter the age of person 3 = ") )

if( p1>p2 and p1>p3 ):
    print("Person1 is elder to person2 and person 3")

    if(p2>p3):
        print("Person2 is middle aged and youngest is Person3")
    else:
        print("Person3 is middle aged and youngest is Person2")

elif( p2>p1 and p2>p3 ):
    print("Person2 is elder to person1 and person 3")

    if (p1 > p3):
        print("Person1 is middle aged and youngest is Person3")
    else:
        print("Person3 is middle aged and youngest is Person1")

else:
    print("Person1 is elder to person2 and person 3")

    if (p1 > p2):
        print("Person2 is middle aged and youngest is Person1")
    else:
        print("Person1 is middle aged and youngest is Person2")