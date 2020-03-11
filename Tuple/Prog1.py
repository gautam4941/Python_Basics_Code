s = (3, 5, 9, 5, 1, 3, 3, 6, 3)
print(s)

print( s.count(1) )

oneindex = s.index( 3 )

print(f"1st Index = {oneindex}")

secondindex = s.index( 3 , oneindex+1)

print(f"2nd Index = {secondindex}")

thirdindex = s.index( 3, secondindex+1 )

print(f"3rd Index = {thirdindex}")

fourindex = s.index( 3, thirdindex+1 )

print(f"4th Index = {fourindex}")

fifthindex = s.index( 3, fourindex+1 )

print(f"5th Index = {fifthindex}")