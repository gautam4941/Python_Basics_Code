'''
Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
'''

'''
while( True ):
    unit = input("Enter the unit of temperature, celsius : c or C and fahrenheit : f or F, Exit e or E = ")

    if( unit == 'e' or unit == 'E' ):
        break

    elif (unit != 'c' and unit != 'C' and unit != 'f' and unit != 'F'):
        print(f"""unit != 'c' = { unit != 'c' }  or unit != 'C' = {unit != 'C'}
                or unit != 'f' = { unit != 'f' } or unit != 'F' = { unit != 'F' } """)

        print("Wrong Unit, Try Again")
        continue

    else:
        temp = float( input("Enter the temperature = ") )

        if( unit == 'c' or unit == 'C' ):
            print( f"Fahrenheit Temperature = { ( (temp*9)/5 ) + 32  }" )   #8 +

        elif( unit == 'f'  or unit == 'F' ):
            print(f"Celsius Temperature = { ( (temp-32) * 5 )/9 }")

        else:
            print("Error, Wrong Input")
'''


temp = float( input("Enter the temperature Value = ") ) #36.2 -> input() -> '36.2' -> float() -> 36.2 -> temp

unit = input("Enter the Unit( F : Fahrenheit and C : Fahrenheit ) = ")

if( unit == 'F' ):
    new_temp = ( ( temp-32 ) / 9 ) * 5

    print(f"Celsius Temperature is { new_temp } and Fahrenheit Temperature is { temp }")

elif( unit == 'C' ):
    new_temp = ( ( 9*temp ) / 5 ) + 32

    print(f"Fahrenheit Temperature is { new_temp } and Celsius Temperature is { temp }")















