# 주문리스트 구현
# 주문생성 addOrder(x) 1 x
# 주문취소 removeOrder(x) 2 x
# 주문조회 getorder(x) 3 x

class orderManager:
    def __init__(self):
        self.orders = []

    def addOrder(self, x):
        self.orders.append(x)

    def removeOrder(self,x):
        if x in self.orders:
            self.orders.remove(x)

    def getOrder(self, x):
        if x in self.orders:
            return self.orders.index(x) + 1
        else:
            return -1


def main():
    line = [int(v) for v in input().split()]
    m = line[0]

    manager = orderManager()

    for i in range(m):
        line = [int(v) for v in input().split()]

        if line[0] == 1:
            manager.addOrder(line[1])

        elif line[0] == 2:
            manager.removeOrder(line[1])

        elif line[0] == 3:
            myOrder = manager.getOrder(line[1])

            if myOrder == -1:
                print("-1")
            else:
                print(str(manager.getOrder(line[1])))
if __name__ == "__main__":
    main()


