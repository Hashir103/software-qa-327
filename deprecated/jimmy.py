class Database:
    def __init__(self):
        self.restuarantDatabase = {}
    
    def getRestuarant(self, toFind):
        return self.restuarantDatabase[toFind]
        
    def createAndAdd(self, name, owner, paymentInformation, location, phone, menu):
        testRestuarant = RestaurantAccount(name, owner, paymentInformation, location, phone, menu)
        self.restuarantDatabase[testRestuarant.name] = testRestuarant
        
    def addRestuarant(self, restuarant):
        self.restuarantDatabase[restuarant.name] = restuarant

    def removeRestuarant(self, removee):
        self.restuarantDatabase.pop(removee.name)

        
# class Order:
#     global STATUS 
#     STATUS = ('Order Cancelled','Order Finished', "In progress")
#     def __init__(self, id,  restuarant, customer, menuItem):
#         self.restuarant = restuarant
#         self.customer = customer
#         self.id = id
#         self.status = 2
#         self.cancellationReason = ''
#         self.menuItem = menuItem
    
#     def setStatus(self, num):
#         self.status = num

#     def setReason(self, message):
#         self.cancellationReason = message

# class MenuItem:
#     def __init__(self, name, cost, custimization, id):
#         self.name = name
#         self.cost = cost
#         self.custimization = custimization
#         self.id - id
    
#     #super sus, needs testing
#     def changeInfo(self, varToChange, changeTo):
#         #temp = vars()[varToChange] #this defintely needs to be tested but can be universal if sucessful, otherwise use a dict
#         self.vars()[varToChange] = changeTo

class RestaurantAccount:
    def __init__(self, name, owner, paymentInformation, location, phone, menu={}):
        self.name = name
        self.owner = owner
        self.paymentInformation = paymentInformation
        self.location = location
        self.phone = phone
        self.currentOrders = {}
        self.finishedOrders = {}
        self.menu = menu

    def addToOrders(resturant, order):
        resturant.order_queue.current_orders[order.id] = order

    def removeFromOrders(resturant, orderID, status, reason):
        if orderID in resturant.order_queue.current_orders:
            temp = resturant.order_queue.current_orders.pop(orderID)
            temp.setStatus(status)
            if status == 1:
                temp.setReason(reason)
            resturant.order_queue.finished_orders[orderID] = temp
        else:
            return "order not found"
    
    def getCurrentOrders(resturant):
        return resturant.order_queue.current_orders
        
    def addToMenu(resturant, menuItem):
        resturant.menu[menuItem.id] = menuItem # could be menu item name instead of ID

    def getMenu(resturant):
        return resturant.menu

# class jimmyReqs:
#     def registerAsRestuarant(database: Database, restuarant):
#         database.createAndAdd('macdonalds', 'me', '99996665543', 'canada', '1234567890', {'1': MenuItem('burger', 5, 'none', '1')})
#     def getCurrentOrders(restuarant: RestaurantAccount):
#         print(restuarant.getCurrentOrders())
#     def restuarantCancelOrder(restuarant: RestaurantAccount, order: Order):
#         restuarant.removeFromOrders(order.id, 0, "Too busy")

# #dont add this part
# def tests():
#     reg = RestaurantAccount(input('Name of Resturant: ', input("Owner: "), input("Money Depoist Info: "), input("Location: "), input("Phone: ")))

        