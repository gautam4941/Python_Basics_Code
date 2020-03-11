menu = [ 'coffee', 'tea', 'buiscuit', 'juice', 'snacks' ]
coffee = [ 'Filter Coffee', 'With Boost', 'Cappucicino', 'Black Coffe', 'Milk Coffee' ]
tea = [ 'Milk Tea', 'Black Tea', 'With Boost' ]
juice = [ 'Mango', 'Apple', 'Grape', 'Pine Apple' ]

print("welcome To out Restraunt")
print("Our Menu, Order Please, ")
l = []

while( True ):
    order_done = input("Do you want to place few more orders ? y:yes, n:no = ")
    print()

    if( order_done == 'y' ):

        print(f"Menu = {menu}")
        print(f"Your Orders = {l}")

        order = input("Enter any Item from the Menu = ")

        if( order in menu ):

            if( order == 'coffee' ):

                print("we have following Coffee varieties, ")
                print( coffee )

                order_coffee = input("Enter you coffee order = ")

                if( order_coffee in coffee ):
                    l.append( order_coffee )

                else:
                    print( f"Sorry, We don't have this { order_coffee } coffee but we are going to add it soon, Please Order someother Coffee" )

            elif( order == 'tea' ):
                print("we have following tea varieties, ")
                print(tea)

                order_tea = input("Enter you tea order = ")

                if (order_tea in tea):
                    l.append( order_tea )

                else:
                    print(
                        f"Sorry, We don't have this {order_tea} tea but we are going to add it soon, Please Order someother tea")

            elif (order == 'juice'):
                print("we have following juice varieties, ")
                print(juice)

                order_juice = input("Enter you juice order = ")

                if (order_juice in juice):
                    l.append( order_juice )

                else:
                    print(
                        f"Sorry, We don't have this {order_juice} juice but we are going to add it soon, Please Order someother juice")

            elif( order == 'buiscuit' ):
                l.append( order )

            else:
                l.append( order )

        else:
            print("Sorry, We don't have this item but we are going to add it soon, Please Order something else")

        print()

    else:
        break

order_count = len( l )

print( f"Your Final Order is { l } and it will ready in { order_count * 3 } minutes " )
print( "Thanks for Coming, See you soon again :-)" )