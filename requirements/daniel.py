class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self, restaurant, items: MenuItem = []):
        self.restaurant = restaurant
        self.items = items

class Order:
    global STATUS 
    STATUS = ('Order Cancelled','Preparing Order', 'On the Way', 'Outside', 'Delivered')
    pickup = ('Leave at Door, Meet at Door, Other')

    def __init__(self, cart: Cart, restaurant, address, pickupMethod, other = None):
        self.items = []
        for item in cart.items:
            self.items.append(item)

        self.restaurant = restaurant
        self.status = 1
        self.expTime = 20  
        self.other = other

    def updateStatus(self):
        self.status += 1

    def cancelOrder(self, user):
        valid = user.getMoney(user, 12)
        if valid: self.status = 0
        return valid
    
    def getInfo(self):
        print(f"Expected Delivery Time: {self.expTime}")
        print(f"Order Status: {STATUS[self.status]}")

    def printReceipt(self):
        print(f"Restaurant: {self.restaurant}")
        sum = 0
        for item in self.items:
            sum += item.price
            print(f"{item.name}: {item.price}")
        print(f"Total: {sum}")

class DanielsRequirements:
    def checkout(cart: Cart, user):
        address = input("Please enter your address: ")

        tip = int(input("Please specify your tip amount (in $)"))

        pickupMethod = input("Please enter your preferred pickup method: \n 1 - Leave at Door \n 2 - Meet at Door \n 3 - Other")
        other = ''
        if (pickupMethod == "Other"):
            other = input("Please specify")

        total = DanielsRequirements.getTotal(cart)

        DanielsRequirements.makePayment(user, total + tip)

        if other == '': newOrder = Order(cart, address, pickupMethod)
        else : newOrder = Order(cart, address, pickupMethod, other)

        return newOrder
    
    def getReceipt(order: Order):
        order.printReceipt()

    def cancelOrder(order, user):
        return order.cancelOrder(user)
    
    def getOrderInfo(order: Order):
        order.getInfo()

    def getTotal(cart: Cart):
        sum = 0
        for item in cart:
            sum += item.price
        return sum

    def makePayment(user, price) -> bool:    # Place holder function to signify bank transaction
        valid = user.getMoney(user, price)
        return valid
    
    

    def main():
        inp = None
        cart = None
        user = None
        print("Press Enter to checkout")
        input("__")
        order = DanielsRequirements.checkout(cart, user)

        DanielsRequirements.getOrderInfo(order)

        while not (choice == '2'):
            choice = input("1 - View Receipt \n 2 - Cancel Order")
            if choice == '1': DanielsRequirements.getReceipt(order)
        
        valid = DanielsRequirements.cancelOrder(order)
        if valid: print("Order successfully cancelled")
