"""
Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess.
If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess,
    user will get a "Well guessed!" message, and the program will exit.
"""

lucky_num = 2

num = -1

count = 0

while( num != lucky_num ):

    num = int( input("Enter a number = ") )  # num = ?, ? = int( ? ), ? = input() -> ?, 5 -> input() -> '5'
                                                # '5' -> int() -> 5 -> num

    if( num == lucky_num ):
        print( f"Congrats, You have choosen the lucky number in { count + 1} attempts" )

    else:
        count = count + 1
        print( "Wrong Selection, Try Again" )

    print( f"Count = { count }" )