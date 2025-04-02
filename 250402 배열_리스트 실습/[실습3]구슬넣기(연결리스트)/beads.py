class LinkedListElement:
    def __init__(self, val, ptr):
        self.value = val
        self.myNext = ptr


class LinkedListPipe:

    def __init__(self):
        self.start = None
        self.end = None

    def addLeft(self, n):

        if self.start is None and self.end is None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else:
            element = LinkedListElement(n, self.start)
            self.start = element

    def addRight(self, n):

        if self.start is None and self.end is None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else:
            element = LinkedListElement(n, None)
            self.end.myNext = element
            self.end = element

    def getBeads(self):

        result = []
        current = self.start

        while current is not None:
            result.append(current.value)
            current = current.myNext

        return result


def processBeads(myInput):
    myPipe = LinkedListPipe()

    for bead, direction in myInput:
        if direction == 0:
            myPipe.addLeft(bead)  # 왼쪽에 추가
        else:
            myPipe.addRight(bead)  # 오른쪽에 추가

    result = myPipe.getBeads()

    return result