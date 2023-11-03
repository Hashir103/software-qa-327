"""
CISC 327 Assignment 3
Nov 2, 2023
Group 23

IMPORTANT, PLEASE RUN FROM THIS DIRECTORY. MAIN.PY IS IN THE ROOT DIRECTORY WITH A FOLDER OF REQUIREMENTS
"""
import requirements.db
from requirements.customer import UserCart, Customer
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
                                    restaurants_db.update_one({"restaurant_name": name}, {"$set": {str(id): {"cancelled_order": True}}})
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

                # made cart created per session
                cart = UserCart({})
                selection = input("Options:\n1. View Restaurant Menu\n2. Manage Cart\n3. Exit\n\nPress the number of the option you want: ")
                
                match selection:
                    case "1":
                        restaurant = restaurants_db.find_one({"restaurant_name":input("Enter the name of the restaurant: ")})
                        if restaurant is None:
                            print("Restaurant not found!")
                        else:
                            Restaurant.get_restauraunt_menu(restaurant)
                        
                    case "2":
                        selection = input("Options:\n1. Add to Cart\n2. Remove from Cart\n3. Clear Cart\n4. Checkout\n5. Exit\n\nPress the number of the option you want: ")
                        
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
                                    pass
                            case "5":
                                print("Exiting..")
                                exit = True
                            case _:
                                print("Invalid option. Please try again.")
                    case "3":
                        print("Exiting..")
                        exit = True
                    case _:
                        print("Invalid option. Please try again.")
        print()
 

if __name__ == '__main__':
    main()