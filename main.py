from requirements.hashir import *

def main():
    exit = False
    db = CustomerList()
    restaurants = {
        "McDonalds": Restaurants({"Big Mac": 5.99, "McChicken": 4.99, "McNuggets": 6.99}, "1234 McDonalds St."),
        "Burger King": Restaurants({"Whopper": 6.99, "Chicken Sandwich": 5.99, "Fries": 3.99}, "1234 Burger King St."),
        "Wendys": Restaurants({"Baconator": 7.99, "Spicy Chicken Sandwich": 6.99, "Frosty": 2.99}, "1234 Wendys St.")
    }
    loggedIn = None

    while not(exit):
        
        if loggedIn is None:
            selection = input("Options:\n1. Register Customer\n2. Login Customer\n3. Exit\n\nPress the number of the option you want: ")

            match selection:
                case "1":
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")
                    phone_number = input("Enter your phone number: ")
                    delievery_address = input("Enter your delievery address: ")
                    payment_information = []
                    payment_information.append(input("Enter credit card type: "))
                    payment_information.append(input("Enter credit card number: "))
                    payment_information.append(input("Enter credit card expiration date: "))
                    payment_information.append(input("Enter credit card security code: "))
                    print()

                    if len(payment_information) != 4:
                        print("Invalid input. Please try again.")

                    if email and password and phone_number and delievery_address and payment_information:
                        db.add_customer(Customer(email, password, phone_number, delievery_address, payment_information))
                    else:
                        print("Invalid input. Please try again.")
                        
                case "2":
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")

                    loggedIn = db.get_customer(email, password)
                case "3":
                    print("Exiting..")
                    exit = True
                case _:
                    print("Invalid option. Please try again.")
        
        else:
            # made cart created per session
            cart = UserCart({})
            selection = input("Options:\n1. View Restaurant Menu\n2. Manage Cart\n3. Exit\n\nPress the number of the option you want: ")
            
            match selection:
                case "1":
                    restaurantName = input("Enter the name of the restaurant: ")
                    print(restaurants[restaurantName].menu)
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
                            # not implemented here
                            cart.checkout()
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

    db.save_customers()
 

if __name__ == '__main__':
    main()