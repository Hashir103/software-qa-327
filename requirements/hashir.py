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


"""
Test Main
"""
def main():
    exit = False
    db = CustomerList()
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
            print("Logged in")
            exit = True
        
        print()

    db.save_customers()
    

if __name__ == '__main__':
    main()