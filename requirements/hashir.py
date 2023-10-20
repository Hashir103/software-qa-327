import json

class Customer:
  def __init__(self, email: str, password: str, phone_number: str, delievery_address: str, payment_information: list):
    self.email = email
    self.password = password
    self.phone_number = phone_number
    self.delievery_address = delievery_address
    self.payment_information = payment_information

class CustomerList:
    def __init__(self):
        self.customers = self.load_customers()

    def load_customers(self):
        with open('requirements/customers.json') as f:
            data = json.load(f)
        return data

    def save_customers(self):
        data = self.load_customers()
        with open('requirements/customers.json', 'w') as f:
            if len(data) <= len(self.customers):
                json.dump(self.customers, f)

    def add_customer(self, customer: Customer):
        if customer.email in self.customers:
            print("Customer already exists")
        else:
            self.customers[customer.email] = [customer.password, customer.phone_number, customer.delievery_address, customer.payment_information]
            print("Customer added successfully")

    def get_customer(self, email: str, password: str):
        account = self.customers.get(email, None)
        if account is not None:
            if account[0] == password:
                print("Login successful")
                return account
            else:
                print("Incorrect password")
                return None
        else:
            print("Account not found")
            return None

    def remove_customer(self, email: str):
        if email in self.customers:
            del self.customers[email]
        else:
            print("Customer not found")

class Restaurants:
    def __init__(self, menu:dict, address:str):
        self.menu = menu
        self.address = address

class UserCart():
    def __init__(self, cart:dict):
        self.cart = cart

    def add_to_cart(self, item:str, quantity:int):
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity

    def remove_from_cart(self, item:str, quantity:int):
        if item in self.cart:
            if self.cart[item] > quantity:
                self.cart[item] -= quantity
            else:
                del self.cart[item]
        else:
            print("Item not found in cart")

    def clear_cart(self):
        self.cart = {}

    def checkout(self):
        pass

"""
Test Main
"""
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