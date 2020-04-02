#To Import mysql.connector
import mysql.connector as conn

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

#We are Updating our data by Emp ID.
emp_id = int( input('Enter the Existing EMP_ID = ') )

#we are counting existing records for that emp_id to understand the total number of future update
query = f"SELECT COUNT(*) FROM EMPLOYEE WHERE emp_id = { emp_id }"

try:
  #Executing the query 1
  cursor.execute( query )
  for i in cursor:
    record_count = i[0]

  # Output of Query 1 and 2
  print(f"record_count = {record_count}")

  try:
    # Want to store value of existing proj_id as we will change it later
    query = f"SELECT proj_id FROM EMPLOYEE WHERE emp_id = {emp_id}"

    # Executing the query 2
    cursor.execute(query)
    for i in cursor:
      old_proj_id = i

    print(f"proj_id = {old_proj_id}")

    # Taking Input of new Project ID
    new_proj_id = input(f"Enter the new Project ID for Emp( {emp_id} ) :- ")

    # Updating the records by new Proj_id
    update_proj_id_query = f"UPDATE EMPLOYEE SET proj_id = %s WHERE EMP_ID = %s"

    # Executing the query 3
    cursor.execute(update_proj_id_query, (new_proj_id, emp_id))
    cursor.execute('commit')

    # Again Fetching the project id( Same as Query 2 ) for the validation Purpose
    query = f"SELECT proj_id FROM EMPLOYEE WHERE emp_id = {emp_id}"

    # Executing the query 4
    cursor.execute(query)
    for i in cursor:
      new_proj_id = i

    # Printing the old and changed one
    print(f"Project has been changed from {old_proj_id} to {new_proj_id} for EMP ID : {emp_id}")


  except Exception as e:
    # Exception in case of any error
    print(f"Error in Select by emp_id, Exception is {e}")

except Exception as e:
  # Exception in case of any error
  print(f"Error in Select by emp_id, Exception is {e}")
