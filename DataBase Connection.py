#import mysql.connector
import mysql.connector as connection
print( 'connection -> ', connection )

#Create Connection
conn = connection.connect( host = '127.0.0.1'
                           ,user = 'root'
                           ,password = 'gautam1234')

print( f"conn = { conn }" )
#Create Cursor
cursor = conn.cursor()

#Execute the Query using Cursor
cursor.execute("select * from employee limit 5")

#fetch the data from cursor
print( cursor )
data = cursor.fetchall()
print()
print()
print( data )
print()
print() 
#Get the data from data variable.
for i in data:
    for j in i:
        print(j, end ='->')

    print()
