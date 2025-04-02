class orderManager :

    def __init__(self) :
        self.data = []

    def addOrder(self, orderId) :
        self.data.append(orderId)

    def removeOrder(self, orderId) :
        self.data.remove(orderId)

    def getOrder(self, orderId) :
        if orderId in self.data:
            order =  self.data.index(orderId)+1
            return order
        else:
            return -1