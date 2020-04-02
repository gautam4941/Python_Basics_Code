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

#We are going to delete data based on EMP_ID and SALARY

#DELETE by Emp_id
try:
  #Taking Emp_id input
  emp_id = int( input('Enter the EMP_ID = ') )

  #DELETE Query 1
  delete_by_EMP_ID = f"DELETE FROM EMPLOYEE WHERE EMP_ID = { emp_id }"

  #QUERY 2 -> COUNTING THE no. of Existing records for given EMP_ID which will be deleted for TABLE
  count_query = f"SELECT count(*) FROM EMPLOYEE WHERE EMP_ID = { emp_id }"

  #EXECUTING QUERY 2
  cursor.execute( count_query )
  for i in cursor:
    count_query = i[0]

  # EXECUTING QUERY 1
  cursor.execute( delete_by_EMP_ID )
  cursor.execute( 'commit' )

  print( f"{ i[0] } rows Deleted" )

except Exception as e:
  #Exception in case of any error
  print( f"Error in Delete by Emp Id, Exception is { e }" )

print()

#DELETE by Salary
try:
  # Taking Salary input
  salary = int( input('Enter the SALARY = ') )

  # DELETE Query 3
  delete_by_SALARY = f"DELETE FROM EMPLOYEE WHERE SALARY = { salary }"

  #QUERY 4 -> COUNTING THE no. of Existing records for given EMP_ID which will be deleted for TABLE
  count_query = f"SELECT count(*) FROM EMPLOYEE WHERE SALARY = { salary }"

  # EXECUTING QUERY 4
  cursor.execute(count_query)
  for i in cursor:
    count_query = i[0]

  # EXECUTING QUERY 3
  cursor.execute( delete_by_SALARY )
  cursor.execute( 'commit' )

  print(f"{i[0]} rows Deleted")

except Exception as e:
  # Exception in case of any error
  print( f"Error in Delete by SALARY, Exception is { e }" )