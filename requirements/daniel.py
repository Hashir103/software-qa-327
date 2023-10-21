class MenuItem:
    """
    MenuItem Class
    """
    def __init__(self, name=None, price=None, menuItem=None):
        if menuItem is not None:
            self.name = menuItem.name
            self.price = menuItem.price
        else:
            self.name = name
            self.price = price


class Cart:
    """
    Cart Class
    """
    def __init__(self, restaurant, cart={}):
        self.restaurant = restaurant
        self.cart = cart

    def getTotal(self):
        """
        This function gest the total value of a Cart
        Input: None
        Output: double
        """
        sum = 0
        for item in self.cart:
            sum += self.cart[item]
        return sum
    
    def checkout(self, user):
        """
        This function requests Customer preferences and finalzies Customer orders
        Input: Cart, Customer
        Output: Order
        """
        address = input("Please enter your address: ")

        tip = int(input("Please specify your tip amount (in $)"))

        pickupMethod = input("Please enter your preferred pickup method: \n 1 - Leave at Door \n 2 - Meet at Door \n 3 - Other")
        other = ''
        if (pickupMethod == "Other"):
            other = input("Please specify")

        total = self.getTotal()

        # Change this line as necessary
        DanielsRequirements.makePayment(user, total + tip)

        if other == '': newOrder = Order(self.cart, self.restaurant, address, pickupMethod)
        else : newOrder = Order(self.cart, self.restaurant, address, pickupMethod, other)

        return newOrder

class Order:
    """
    Order Class
    """
    global STATUS 
    STATUS = ('Order Cancelled','Preparing Order', 'On the Way', 'Outside', 'Delivered')
    pickup = ('Leave at Door, Meet at Door, Other')

    def __init__(self, cart, restaurant, address, pickupMethod = None, other = None):
        """
        Initialize order using customer Cart
        """
        self.items = cart
        self.restaurant = restaurant
        self.deliverAdd = address
        self.pickupMethod = pickupMethod
        self.status = 1
        self.expTime = 20  
        self.other = other

    def updateStatus(self):
        """
        This function updates Order Status
        Input: None
        Output: bool
        """
        self.status += 1
        return True

    def cancelOrder(self, user):
        """
        This function updates Order Status to cancelled
        Input: Customer
        Output: bool
        """
        valid = user.getMoney(user, 12)
        if valid: self.status = 0
        return valid
    
    def getInfo(self):
        """
        This function updates Order Status
        Input: None
        Output: bool
        """
        print(f"Expected Delivery Time: {self.expTime}")
        print(f"Order Status: {STATUS[self.status]}")
        return True

    def printReceipt(self):
        """
        This function prints the Order receipt
        Input: None
        Output: bool
        """
        print(f"Restaurant: {self.restaurant}")
        sum = 0
        for item in self.items:
            sum += self.items[item]
            print(f"{item}: {self.items[item]}")
        print(f"Total: {sum}")

class DanielsRequirements:
    @staticmethod
    def checkout(cart: Cart, user):
        cart.checkout(user)
    
    @staticmethod
    def getReceipt(order: Order):
        order.printReceipt()

    @staticmethod
    def cancelOrder(order, user):
        return order.cancelOrder(user)
    
    @staticmethod
    def getOrderInfo(order: Order):
        order.getInfo() 

    @staticmethod
    def makePayment(user, price) -> bool:    # Place holder function to signify bank transaction
        #valid = user.getMoney(user, price)
        if len(user) < 4:
            print("Account error")
            return False
        else:
            print(f"Payment of {price} successful")
            return True
    
    

# def main():
#     inp = None
#     cart = None
#     user = None
#     print("Press Enter to checkout")
#     input("__")
#     order = DanielsRequirements.checkout(cart, user)

#     DanielsRequirements.getOrderInfo(order)

#     while not (choice == '2'):
#         choice = input("1 - View Receipt \n 2 - Cancel Order")
#         if choice == '1': DanielsRequirements.getReceipt(order)
    
#     valid = DanielsRequirements.cancelOrder(order)
#     if valid: print("Order successfully cancelled")

