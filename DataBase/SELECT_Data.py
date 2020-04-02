#To Import mysql.connector
import mysql.connector as conn

#To Setup the Connection
conn = conn.connect(
  host="localhost",
  user="root",
  password="gautam1234"
)

#Printing Connection for th validation purpose that it is not giving error
print( f"connection = { conn }" )
# Creating the Cursor
cursor = conn.cursor()

#To see the databases
print( f"Inside select_database cursor = { cursor } and id( cursor ) = { id( cursor ) }" )
cursor.execute("SHOW DATABASES")
print( "SHOW DATABASES :- " )
count = 0
for i in cursor:
  count = count + 1
  print( f"{count}. {i}" )
print()

#To use Database
#cursor.execute( f"USE {input('Enter the data base name = ') }" )
cursor.execute( f"USE mamta" )

#To see the Table in selected database
cursor.execute( "SHOW TABLES" )
print( "SHOW TABLES :- " )
count = 0
for i in cursor:
  count = count + 1
  print( f"{count}. {i}" )
print()
#table_name = input("Enter the table_name = ")
table_name = 'EMPLOYEE'

#information_schema.columns is the table name where all the table of all database information exist
#Excute following code for more detail,


# cursor.execute("desc information_schema.columns")
# for i in cursor:
#   print( i )


#Why are we doing it ?
#Ans :- We are doing it because we want to display our table data with columns for good look
#If we will do select * from table_name then, it will give only table data . It will not
#give columns names

#Now Fetching data from table,
query = """select COLUMN_NAME from information_schema.columns 
            where TABLE_NAME = (%s) order by TABLE_NAME,COLUMN_NAME"""

cursor.execute( query, ( table_name, ) )

col_names = []
count = 0
for i in cursor:
  count = count + 1
  print(f"Column {count}. {i} ")
  col_names.append( i[0] )

print()
cursor.execute(f"SELECT * FROM { table_name } ")
print("DATA INSIDE TABLE :- ")

###########See the Following query first to proceed further,

# count = 0
# for i in cursor:
#   print( i )

columns_head = ""
for i in col_names:
  columns_head = columns_head + i + ', '

print( columns_head )

count = 0
for i in cursor:
  for j in i:
    print( j, end=',' )

  count = count + 1
  print()

print( f"\n{count} rows selected" )