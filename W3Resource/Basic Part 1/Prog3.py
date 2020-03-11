import datetime
now = datetime.datetime.now()

print( f"now = { now }" )

date_and_time = now.strftime("%Y-%m-%d %H::%M::%S")

print( f"date_and_time = { date_and_time } and type( date_and_time ) = { type( date_and_time ) }" )

print( date_and_time[ 7: 9 ] )
print( date_and_time[ 4: 6 ] )

# D
# M
# Y
# H
# M
# S