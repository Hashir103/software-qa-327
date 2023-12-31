import random

class Customer():
    '''
    Customer Class is for static methods used for database calls and setting up the user Card function
    '''
    def __init__(self) -> None:
        self.cart = UserCart({})

    def get_user_cart(self):
        return self.cart

    @staticmethod
    def register_customer():
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
            return None

        elif email and password and phone_number and delievery_address and payment_information:
            customer = {
                "account_info": {
                    "email": email,
                    "password": password
                },
                "personal_info": {
                    "phone_number": phone_number,
                    "home_address": delievery_address
                },
                "credit_card_info": {
                    "card_type": payment_information[0],
                    "card_numbers": payment_information[1],
                    "expiry_date": payment_information[2],
                    "cvv": payment_information[3]
                }
            }
            print("\n Successfully registered user!")
            return customer
        else:
            print("Invalid input. Please try again.")
            return None

class UserCart():
    """
    User Cart Class
    """
    def __init__(self, cart:dict):
        self.cart = cart

    def add_to_cart(self, item:str, quantity:int):
        """
        This function adds an item to the cart
        Input: Item name and quantity
        Output: None
        """
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity

    def remove_from_cart(self, item:str, quantity:int):
        """
        This function removes an item from the cart
        Input: Item name and quantity
        Output: None
        """
        if item in self.cart:
            if self.cart[item] > quantity:
                self.cart[item] -= quantity
                return 2
            else:
                del self.cart[item]
                return 1
        else:
            print("Item not found in cart")
            return 0

    def clear_cart(self):
        """
        This function clears the cart
        Input: None
        Output: None
        """
        self.cart = {}

    def checkout(self, user:dict):
        """
        This function checks out the user's current card
        Input: User Object
        Output: Returns the user's order object to be sent to vendor (or None)
        """
        payment_information = user["credit_card_info"]
        personal_information = user["personal_info"]
        cart = self.cart

        if self.cart == {}:
            print("Your cart is empty!")
            return None
        else:
            return {
                "payment_information": payment_information,
                "personal_information": personal_information,
                "order": cart
                }