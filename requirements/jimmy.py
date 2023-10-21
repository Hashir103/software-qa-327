class Database:
    def __init__(self):
        self.restuarantDatabase = {}
    
    def getRestuarant(self, toFind):
        return self.restuaratDatabase[toFind]
        
    def createAndAdd(self, name, owner, paymentInformation, location, phone):
        testRestuarant = RestaurantAccount(name, owner, paymentInformation, location, phone)
        self.restuarantDatabase[testRestuarant.name] = testRestuarant
        
    def addRestuarant(self, restuarant):
        self.restuarantDatabase[restuarant.name] = restuarant

    def removeRestuarant(self, removee):
        self.restuarantDatabase.pop(removee.name)

        
class Order:
    global STATUS 
    STATUS = ('Order Cancelled','Order Finished', "In progress")
    def __init__(self, id,  restuarant, customer):
        self.restuarant = restuarant
        self.customer = customer
        self.id = id
        self.status = 2
        self.cancellationReason = ''
    
    def setStatus(self, num):
        self.status = num

    def setReason(self, message):
        self.cancellationReason = message

class MenuItem:
    def __init__(self, name, cost, custimization, id):
        self.name = name
        self.cost = cost
        self.custimization = custimization
        self.id - id
    
    #super sus, needs testing
    def changeInfo(self, varToChange, changeTo):
        #temp = vars()[varToChange] #this defintely needs to be tested but can be universal if sucessful, otherwise use a dict
        self.vars()[varToChange] = changeTo

class RestaurantAccount:
    def __init__(self, name, owner, paymentInformation, location, phone, menu = {}):
        self.name = name
        self.owner = owner
        self.paymentInformation = paymentInformation
        self.location = location
        self.phone = phone
        self.currentOrders = {}
        self.finishedOrders = {}
        self.menu = menu

    def addToOrders(self, order):
        self.currentOrders[order.id] = order

    def removeFromOrders(self, orderID, status, reason):
        if orderID in self.currentOrders:
            temp = self.currentOrders.pop(orderID)
            temp.setStatus(status)
            if status == 1:
                temp.setReason(reason)
            self.finishedOrders[orderID] = temp
        else:
            return "order not found"
    
    def getCurrentOrders(self):
        return self.currentOrders
        
    def addToMenu(self, menuItem):
        self.menu[menuItem.id] = menuItem

    def getMenu(self):
        return self.menu()

class jimmyReqs:
    def registerAsRestuarant(database: Database, restuarant):
        database.createAndAdd('macdonalds', 'me', '99996665543', 'canada', '1234567890')
    def getCurrentOrders(restuarant: RestaurantAccount):
        print(restuarant.getCurrentOrders())
    def restuarantCancelOrder(restuarant: RestaurantAccount, order: Order):
        restuarant.removeFromOrders(order.id, 0, "Too busy")




def main():

    ###
    #a = []
    #a.append(input('Name of Resturant: '))
    #a.append(input("Owner: "))
    #a.append(input("Money Depoist Info: "))
    #a.append(input("Location: "))
    #a.append(input("Phone: "))
    y = input("f")
    res = RestaurantAccount('macdonalds', 'me', 'asfsadf', 'canada', 'sadfsaf')
    print(res.location)###
    
main()

#dont add this part
def tests():
    reg = RestaurantAccount(input('Name of Resturant: ', input("Owner: "), input("Money Depoist Info: "), input("Location: "), input("Phone: ")))

        