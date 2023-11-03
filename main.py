"""
CISC 327 Assignment 3
Nov 2, 2023
Group 23

IMPORTANT, PLEASE RUN FROM THIS DIRECTORY. MAIN.PY IS IN THE ROOT DIRECTORY WITH A FOLDER OF REQUIREMENTS
"""
import random
import requirements.db
from requirements.customer import Customer
from requirements.restaurant import Restaurant

def main():
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
            selection = input("Options:\n1. Register Customer\n2. Login Customer\n3. Restaurant Actions\n4. Exit\n\nPress the number of the option you want: ")

            match selection:
                case "1":
                    # register a customer
                    customer = Customer.register_customer()
                    if customer is not None:
                        customers_db.insert_one(customer)
                        
                case "2":
                    # find customer in database
                    account_info = {
                        "account_info": {
                            "email": input("Enter your email: "),
                            "password": input("Enter your password: ")
                        }
                    }

                    loggedIn = customers_db.find_one(account_info)

                    # customer not found in database
                    if loggedIn is None:
                        print("\nAn account does not exist with that email and password combination.")
                    
                    else:
                        print("\nSuccessfully logged in!")
                        customer = Customer()

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
                selection = input("Options\n1. Register Restaurant\n2. Get Restaurant Orders\n3. Cancel Customer Order\n4. Exit\n\nPress the number of the option you want: ")
                match selection:
                    case "1":
                        # register a restaurant
                        restaurant = Restaurant.register_restaurant()
                        if restaurant is not None:
                            restaurants_db.insert_one(restaurant)
                    case "2":
                        # find a restaurant in database
                        restaurant = restaurants_db.find_one({"restaurant_name": input("Enter the name of the restaurant: ")})

                        # if restaurant not found
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            # get restaurant order queue
                            Restaurant.get_restaurant_order_queue(restaurant)
                    case "3":
                        # find a restaurant in database
                        name = input("Enter the name of the restaurant: ")
                        restaurant = restaurants_db.find_one({"restaurant_name": name})
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            id = input("Enter the order ID: ")
                            if id.isnumeric():
                                id = int(id)
                                reason = input("Enter the reason for cancellation: ")

                                # remove order from order queue
                                if Restaurant.remove_restaurant_order(restaurant, id, reason):
                                    restaurants_db.update_one({"restaurant_name": name}, {"$set": {f"order_queue.current_orders.{str(id)}": {"cancelled_order": True, "reason": reason}}})
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
                selection = input("Options:\n1. View Available Restaurants\n2. View Restaurant Menu\n3. Manage Cart\n4. Exit\n\nPress the number of the option you want: ")
                
                match selection:
                    case "1":
                        restaurants = restaurants_db.find({"restaurant_name": {"$exists": True}})
                        Restaurant.get_restaurants(restaurants)
                    case "2":
                        restaurant = restaurants_db.find_one({"restaurant_name":input("Enter the name of the restaurant: ")})
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            Restaurant.get_restauraunt_menu(restaurant)
                        
                    case "3":
                        name = input("Select a restaurant to manage your cart for: ")
                        restaurant = restaurants_db.find_one({"restaurant_name": name})
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            # made cart created per session
                            cart = customer.get_user_cart() # type: ignore
                            cartMenu = True
                            while cartMenu:
                                selection = input("Options:\n1. Add to Cart\n2. Remove from Cart\n3. Clear Cart\n4. Checkout\n5. Back to Menu\n6. Exit\n\nPress the number of the option you want: ")
                                
                                match selection:
                                    case "1":
                                        item = input("Enter the name of the item: ")
                                        quantity = int(input("Enter the quantity of the item: "))
                                        cart.add_to_cart(item, quantity)
                                    case "2":
                                        item = input("Enter the name of the item: ")
                                        quantity = int(input("Enter the quantity of the item: "))
                                        cart.remove_from_cart(item, quantity)
                                    case "3":
                                        cart.clear_cart()
                                    case "4":
                                        order = cart.checkout(loggedIn)
                                        if order is not None:
                                            id = str(random.randint(100000, 999999))
                                            check = restaurants_db.find_one({
                                                "restaurant_name":name,
                                                "order_queue.current_orders.id": id
                                            })
                                            while check:
                                                id = str(random.randint(100000, 999999))
                                                check = restaurants_db.find_one({
                                                "restaurant_name":name,
                                                "order_queue.current_orders.id": id
                                            })
                                            restaurants_db.update_one({"restaurant_name": name}, {"$set": {f"order_queue.current_orders.{str(id)}": {"order":order ,"cancelled_order": False, "reason": ""}}})
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
    main()