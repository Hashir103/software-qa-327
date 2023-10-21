import json
from requirements.daniel import Cart

class Customer:
  """
  Customer Class
  """
  def __init__(self, email: str, password: str, phone_number: str, delievery_address: str, payment_information: list):
    self.email = email
    self.password = password
    self.phone_number = phone_number
    self.delievery_address = delievery_address
    self.payment_information = payment_information

class CustomerList:
    """
    Customer Database Class
    """
    def __init__(self):
        self.customers = self.load_customers()

    def load_customers(self):
        """
        This function loads the customers from the json file
        Input: None
        Output: A dictionary of customers
        """
        with open('requirements/customers.json') as f:
            data = json.load(f)
        return data

    def save_customers(self):
        """
        This function saves the customers to the json file
        Input: None
        Output: None
        """
        data = self.load_customers()
        with open('requirements/customers.json', 'w') as f:
            # if there are changes to the database, save it
            if len(data) <= len(self.customers):
                json.dump(self.customers, f)

    def add_customer(self, customer: Customer):
        """
        This function adds a customer to the database
        Input: Customer object
        Output: None
        """
        if customer.email in self.customers:
            print("Customer already exists")
        else:
            self.customers[customer.email] = [customer.password, customer.phone_number, customer.delievery_address, customer.payment_information]
            print("Customer added successfully")

    def get_customer(self, email: str, password: str):
        """
        This function gets a customer from the database
        Input: Email and password
        Output: Customer object
        """
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
        """
        This function removes a customer from the database
        Input: Email
        Output: None
        """
        if email in self.customers:
            del self.customers[email]
        else:
            print("Customer not found")

class Restaurants:
    """
    Restaurant Class -> Testing class for now, will be replaced with Jimmy's in main implementation
    """
    def __init__(self, menu:dict, address:str):
        self.menu = menu
        self.address = address

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
            else:
                del self.cart[item]
        else:
            print("Item not found in cart")

    def clear_cart(self):
        """
        This function clears the cart
        Input: None
        Output: None
        """
        self.cart = {}

    def checkout(self, user:Customer):
        """Taken from Daniel's Method"""
        d_cart = Cart(self.cart)
        d_cart.checkout(user)