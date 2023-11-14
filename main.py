"""
CISC 327 Assignment 3
Nov 2, 2023
Group 23

IMPORTANT, PLEASE READ README.TXT
"""
import random
import requirements.db
from requirements.customer import Customer
from requirements.restaurant import Restaurant

def run_program(testRun = False, init_selection = None, account_info = None, rest_selection = None, cust_selection = None, cart_selection = None, item = None, quantity = None, rest_name = None, reason = None, u_id = None):
    exit = False

    # new database setup
    databases = requirements.db.run_cluster()
    if len(databases) == 0:
        print("An Error occurred when getting the Customer and restaurant databases")
        return
    else:
        customers_db = databases[0]
        restaurants_db = databases[1]

    loggedIn = None
    customer = None

    while not(exit):
        if loggedIn is None:
            init_selection = input("Options:\n1. Register Customer\n2. Login Customer\n3. Restaurant Actions\n4. Exit\n\nPress the number of the option you want: ") if init_selection is None else init_selection

            match init_selection:
                case "1":
                    # register a customer
                    customer = Customer.register_customer()
                    if customer is not None:
                        customers_db.insert_one(customer)
                        
                case "2":
                    # find customer in database
                    account_info = {
                        "account_info": {
                            "email": input("Enter your email: ") if testRun == False else account_info[0], # type: ignore
                            "password": input("Enter your password: ") if testRun == False else account_info[1] # type: ignore
                        }
                    }

                    loggedIn = customers_db.find_one(account_info)

                    # customer not found in database
                    if loggedIn is None:
                        print("\nAn account does not exist with that email and password combination.")
                        if testRun and (cust_selection is None and rest_selection is None):
                            return False
                    
                    else:
                        print("\nSuccessfully logged in!")
                        customer = Customer()
                        if testRun and (cust_selection is None and rest_selection is None):
                            return True

                case "3":
                    # set log in type as restaurant
                    loggedIn = "Restaurant"

                case "4":
                    print("Exiting..")
                    exit = True

                case _:
                    print("Invalid option. Please try again.")
        
        else:
            if loggedIn == "Restaurant":
                rest_selection = input("Options\n1. Register Restaurant\n2. Get Restaurant Orders\n3. Cancel Customer Order\n4. Exit\n\nPress the number of the option you want: ") if testRun == False else rest_selection
                match rest_selection:
                    case "1":
                        # register a restaurant
                        restaurant = Restaurant.register_restaurant()
                        if restaurant is not None:
                            restaurants_db.insert_one(restaurant)
                    case "2":
                        # find a restaurant in database
                        rest_name = input("Enter the name of the restaurant: ") if testRun == False else rest_name
                        restaurant = restaurants_db.find_one({"restaurant_name": rest_name})

                        # if restaurant not found
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            # get restaurant order queue
                            Restaurant.get_restaurant_order_queue(restaurant)
                    case "3":
                        # find a restaurant in database
                        rest_name = input("Enter the name of the restaurant: ") if testRun == False else rest_name
                        restaurant = restaurants_db.find_one({"restaurant_name": rest_name})
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            u_id = input("Enter the order ID: ") if testRun == False else u_id
                            if u_id.isnumeric():
                                u_id = int(u_id)
                                reason = input("Enter the reason for cancellation: ") if testRun == False else reason

                                # remove order from order queue
                                if Restaurant.remove_restaurant_order(restaurant, u_id):
                                    restaurants_db.update_one({"restaurant_name": rest_name}, {"$set": {f"order_queue.current_orders.{str(u_id)}": {"cancelled_order": True, "reason": reason}}})
                                else:
                                    print("Order ID not found")
                            else:
                                print("Invalid ID!")
                    case "4":
                        print("Exiting..")
                        exit = True
                    case _:
                        print("Invalid option. Please try again.")
            else:
                # logged in as customer
                cust_selection = input("Options:\n1. View Available Restaurants\n2. View Restaurant Menu\n3. Manage Cart\n4. Exit\n\nPress the number of the option you want: ") if testRun == False else cust_selection
                
                match cust_selection:
                    case "1":
                        restaurants = restaurants_db.find({"restaurant_name": {"$exists": True}})
                        info = Restaurant.get_restaurants(restaurants)
                        if testRun:
                            return info[1]
                    case "2":
                        rest_name = input("Enter the name of the restaurant: ") if testRun == False else rest_name
                        restaurant = restaurants_db.find_one({"restaurant_name": rest_name})
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            print(Restaurant.get_restauraunt_menu(restaurant)[0])
                            if testRun:
                                return Restaurant.get_restauraunt_menu(restaurant)[1]
                        
                    case "3":
                        rest_name = input("Select a restaurant to manage your cart for: ") if testRun == False else rest_name
                        restaurant = restaurants_db.find_one({"restaurant_name": rest_name})
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            # made cart created per session
                            cart = customer.get_user_cart() # type: ignore
                            cartMenu = True
                            while cartMenu:
                                cart_selection = input("Options:\n1. Add to Cart\n2. Remove from Cart\n3. Clear Cart\n4. Checkout\n5. Back to Menu\n6. Exit\n\nPress the number of the option you want: ") if testRun == False else cart_selection
                                
                                match cart_selection:
                                    case "1":
                                        item = input("Enter the name of the item: ") if testRun == False else item
                                        quantity = int(input("Enter the quantity of the item: ")) if testRun == False else quantity
                                        cart.add_to_cart(item, quantity) # type: ignore
                                    case "2":
                                        item = input("Enter the name of the item: ") if testRun == False else item
                                        quantity = int(input("Enter the quantity of the item: ")) if testRun == False else quantity
                                        cart.remove_from_cart(item, quantity) # type: ignore
                                    case "3":
                                        cart.clear_cart()
                                    case "4":
                                        order = cart.checkout(loggedIn)
                                        if order is not None:
                                            u_id = str(random.randint(100000, 999999))
                                            check = restaurants_db.find_one({
                                                "restaurant_name":rest_name,
                                                "order_queue.current_orders.id": u_id
                                            })
                                            while check:
                                                u_id = str(random.randint(100000, 999999))
                                                check = restaurants_db.find_one({
                                                "restaurant_name":rest_name,
                                                "order_queue.current_orders.id": u_id
                                            })
                                            restaurants_db.update_one({"restaurant_name": rest_name}, {"$set": {f"order_queue.current_orders.{str(u_id)}": {"order":order ,"cancelled_order": False, "reason": ""}}})
                                            print("Order Succesfully sent to Vendor")
                                            cartMenu = False
                                    case "5":
                                        print("Back to menu..")
                                        cartMenu = False
                                    case "6":
                                        print("Exiting..")
                                        cartMenu = False
                                        exit = True
                                    case _:
                                        print("Invalid option. Please try again.")
                                print()
                    case "4":
                        print("Exiting..")
                        exit = True
                    case _:
                        print("Invalid option. Please try again.")
        print()
 

if __name__ == '__main__':
    run_program()