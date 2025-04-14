# 주문리스트 구현
# 주문생성 addOrder(x) 1 x
# 주문취소 removeOrder(x) 2 x
# 주문조회 getorder(x) 3 x

## 마찬가지 주문 노드가 필요하고 / 주문노드들이 연결된 리스트가 필요한 것

class order:
    def __init__(self, val, prev, nxt):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class orderManager:
    def __init__(self):
        self.start = None
        self.end = None
        self.orders = {}    # 딕셔너리 이용

    def addOrder(self, x):
        element = order(x,None, None)

        self.orders[x] = element

        if self.start is None:
            self.start = element
            self.end = element
        else:
            self.end.nxt = element
            element.prev = self.end
            self.end = element

    def removeOrder(self, x):
        if self.start == None and self.end == None: # 빈리스트인 경우 지울 수 없으므로 리턴
            return

        cur = self.orders[x]

        if self.start == cur and self.end == cur:  # 주문이 하나 들어 있는데, 그 주문을 지우려는 경우
            self.start = None
            self.end = None

        elif self.start == cur: # 가장 첫 노드를 지우려는 경우
            self.start = cur.nxt
            cur.nxt.prev = None

        elif self.end == cur: # 가장 마지막 노드가 지워지는 경우
            self.end = cur.prev
            cur.prev.nxt = None

        else: # 그냥 중간에 있는 무언가의 노드인 경우
            cur.prev.nxt = cur.nxt
            cur.nxt.prev = cur.prev

    def getOrder(self, x):
        cur = self.start
        index = 1

        while cur != None:
            if cur.val == x:
                return index

            cur = cur.nxt
            index += 1
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
