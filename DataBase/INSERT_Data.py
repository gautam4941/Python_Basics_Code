#To Import mysql.connector
import mysql.connector as conn
import pandas as pd

#To Setup the Connection
conn = conn.connect(
  host="localhost",
  user="root",
  password="gautam1234"
)

#print( f"connection = { conn }" )
# Creating the Cursor
cursor = conn.cursor()

cursor.execute( f"USE mamta" )
#cursor.execute( f"USE { input("Enter the database name = ) }" )

table_name = 'EMPLOYEE'
#table_name = input("Enter the table name = ")

##################Insert into Table#########################
#To insert data into table we need to know atleast 3 things,
#a) column names, b) data type, c) length of data type

#Plan :- We will be inserting some data and if our data will get inserted then it's fine otherwise
#in case of error, it should given reason of error also

#This will give column name, data type, length
query = """select COLUMN_NAME from information_schema.columns where TABLE_NAME = (%s)"""
cursor.execute( query, ( table_name, ) )

col_details = []

for i in cursor:
  #Adding all the col_names as key
  col_details.append( i[0] )

#print( f"col_details = { col_details }" )

# data_to_be_inserted = []
# for i in col_names:
#   data_to_be_inserted.append( input( f"Enter {i} = " ) )

#print( f"col_details = { col_details }" )

query = "INSERT INTO employee("
for i in col_details:
  query = query + i + ', '

query = query[ : len( query ) - 2 ]

query = query + ') VALUES ('

for i in col_details:
  query = query + '%s, '

query = query[ : len( query ) - 2 ] + ' )'

#print( f"insert query = { query }" )

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\Python Concept - Gautam\DataBase\Data_To_Be_Inserted.csv" )
#print( f"data.columns = { data.columns }" )

count = 0
for i in range( len( data.index ) ):
  row_data = ( str( data['EmpID'][i] )
             , str( data['Employee_Name'][i] )
             , str( data['Manager'][i] )
             , str( data['salary'][i] )
             , str( data['Proj_id'][i] ) )

  print( f"row_data = { row_data }" )
  print()
  cursor.execute( query, row_data )
  count = count + 1

cursor.execute( 'COMMIT' )
print( f"{ count + 1 } Record Inserted" )

#cursor.execute( "TRUNCATE TABLE employee" )