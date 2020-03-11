age = int( input("Enter the Age of person = ") )
gender = input("Male or Female(M/F) = ")
marital_status = input("Y/N = ")

if( gender == 'F' ):
    print("Urban Area")

elif( gender == 'M' ):
    if( age>=20 and age <=40 ):
        print("Anywhere")

    elif( age >40 and age <=60 ):
        print("Urban Area")

    else:
        print("Error")
