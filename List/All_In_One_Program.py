"""
1. Data Insertion
2.Data Deletion
3. Data Update
4. count()
5. copy()
6. reverse()
7. Index
"""
import random

l = [ [8, 9, 9, 1, 0, 8], [2, 3, 5, 0, 9, 2, 2, 1] ]

while( True ):

    op = input("""1. Create List, 2. Insert Data, 3. Delete Data, 4. Update list, 5. Copy List,
    6. Count any data, 7. Reverse, 8. Find index of value, 9. Print, 10. Sort 11. Exit = """)

    if( op.isdigit() ):
        op = int( op )

        if( op == 1 ):
            l.append( [] )
            print( "List Created" )

        elif( op == 2 ):

            for i in range(len(l)):
                print(f"{i + 1}. {l[i]}")

            choose_list = int(input("Enter the List number = ")) - 1

            l[choose_list].append( random.randrange( 1, 10, 1 ) )

            """
            data = input("\nEnter data to be inserted = ")
            while( True ):
                index = input("Enter index where data has to be inserted = ")

                if( index.isdigit() ):
                    index = int( index )

                    choose_list = int( input("Enter the List number = ") ) - 1

                    l[ choose_list ].insert( index, data )
                    print( f"Data has been inserted to list { choose_list + 1 }" )
                    break

                else:
                    print( "Error, Enter the integer Index" )
            """

        elif( op == 3 ):
            for i in range(len(l)):
                print(f"{i + 1}. {l[i]}")

            choose_list = int(input("Enter the List number = ")) - 1

            del_op = input("Delete by 1.Index , 2. Value = " )

            if( del_op.isdigit() ):
                del_op = int( del_op )

                if( del_op == 1 ):
                    index = input("Enter index at which data has to be deleted = ")

                    if (index.isdigit() ):
                        index = int(index)

                        if( index < len( l[choose_list] ) and index > 0  ):
                            print( f"Deleted Data from List { choose_list + 1 } is { l[choose_list].pop( index ) }" )

                    else:
                        print( f"Choose, Correct Index" )

                else:
                    print(f"Choose Correct Option")

            else:
                print(f"Error, Please enter integer option")

        elif( op == 4 ):

            for i in range( len( l ) ):
                print( f"{ i+1 }. { l[i] }" )

            choose_list = int(input("Enter the List number = ")) - 1

            update_op = int(input("Update by, 1.Index 2. Value = "))

            if (update_op == 1):

                while (True):
                    index = int(input("Enter the Index Value = "))

                    if (index < len(l[choose_list])):
                        l[choose_list][index] = input("Etner the new data = ")
                        print("Update Done")
                        break
                    else:
                        print("Entered Index is not in Range")

            elif( update_op == 2 ):
                curr_data = input("Enter the data has to be update( Old Data ) = ")
                new_data = input("Enter the New Data = ")

                update_count = 0

                for i in range( len( l[choose_list] ) ):
                    if( curr_data == str( l[choose_list][i] ) ):
                        l[choose_list][i] = new_data
                        update_count = update_count + 1

                print( f"{ update_count } times { curr_data } has been updated to { new_data }" )

        elif( op == 5 ):
            for i in range( len( l ) ):
                print( f"{i+1}. { l[i] }" )

            copy_op = input("Enter existing list = ")

            if( copy_op.isdigit() == True ):
                copy_op = int( copy_op ) - 1

                if( copy_op < len(l) ):
                    l.append( l[copy_op].copy() )
                    print( f"Your List no . { copy_op + 1 } copied" )

        elif( op == 6 ):
            count_op = input("Enter data to be counted = ")

            count_list = []
            for i in range( len( l ) ):
                count = 0

                for j in range( len( l[i] ) ):
                    if( count_op == str( l[i][j] ) ):
                        count = count + 1

                count_list.append( count )

            print(  f"{ count_op } found in following list")

            for i in range( len( count_list ) ):
                print( f"List{i+1} -> { count_list[i] }")

        elif( op == 7 ):
            print()
            for i in  range( len( l ) ):
                print( f"Reverse of { l[i] } = { l[i][ : : -1 ] }" )
            print()

        elif( op == 8 ):
            for i in range( len(l) ):
                print( f"{i+1}. { l[i] }" )

            value = input( "Enter data for which index to be found = " )

            index_list = []

            for i in  range( len( l ) ):
                temp = []

                for j in range( len( l[i] ) ):
                    if( value == str( l[i][j] ) ):
                        temp.append( j )

                index_list.append( temp )

            for i in range( len( index_list ) ):
                if( len( index_list[i] ) > 0 ):
                    print( f"List{i+1} has indexes at positions -> { index_list[i] }" )
                else:
                    print( f"No index found in List{i+1} for data = { value }" )

        elif (op == 9):
            print()
            for i in range( len(l) ):
                print( f"{i+1}. { l[i] }" )
            print()

        elif( op == 10 ):
            print()
            for i in range( len(l) ):
                print( f"{i+1}. { l[i] }" )

            sort_op = int( input("Enter the List number to be sorted = ") ) - 1

            if( sort_op < len(l) ):
                temp = l[ sort_op ].copy()
                temp.sort()

                print( temp )
                #l.append( temp )
            else:
                print( f"{ sort_op } is more than exisitng length of Main List" )

            print()

        elif( op == 11 ):
            break

        else:
            print( f"Please, Choose correct option" )

    else:
        print( "Please, Enter Digit" )