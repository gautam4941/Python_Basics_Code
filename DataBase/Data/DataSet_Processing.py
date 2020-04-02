import pandas as pd
import random

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\Python Concept - Gautam\DataBase\Data\HR_NEW_DATA.csv" )
print( data.head() )

salary_list = []
for i in range( len( data.index ) ):
    salary_list.append( random.randrange( 10000, 100000, 5000 ) )

data['salary' ] = pd.Series( salary_list )

proj_id_list = []
for i in range( len( data.index ) ):
    proj_id_list.append( random.choice( ('ABC', 'DEF', 'GHI' ) ) )

data['Proj_id' ] = pd.Series( proj_id_list )

data.to_csv( r"C:\Users\gauta\PycharmProjects\Python Concept - Gautam\DataBase\Data\Data_To_Be_Inserted.csv" )