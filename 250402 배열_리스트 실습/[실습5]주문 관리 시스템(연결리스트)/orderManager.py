class LinkedListElement:
    def __init__(self, data, myPrev=None, myNext=None):
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext


class orderManager:
    def __init__(self):
        self.start = None  # 리스트의 첫 번째 노드
        self.end = None  # 리스트의 마지막 노드

    def addOrder(self, orderId):
        new_order = LinkedListElement(orderId)

        if self.end is None:  # 첫 번째 노드 추가
            self.start = new_order
            self.end = new_order
        else:
            self.end.myNext = new_order
            new_order.myPrev = self.end
            self.end = new_order

    def removeOrder(self, orderId):
        current = self.start

        while current:
            if current.data == orderId:
                if current.myPrev:
                    current.myPrev.myNext = current.myNext
                else:
                    self.start = current.myNext

                if current.myNext:
                    current.myNext.myPrev = current.myPrev
                else:
                    self.end = current.myPrev

                del current
                return
            current = current.myNext

    def getOrder(self, orderId):
        current = self.start
        index = 1  # 1부터 시작하여 카운트를 위한 변수
        while current:
            if current.data == orderId:
                return index  # 몇 번째인지 반환
            current = current.myNext
            index += 1
        return -1
