
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
        cur = self.start

        while cur is not None:
            result.append(cur.value)
            cur = cur.myNext

        return result


def processBeads(myInput):
    myPipe = LinkedListPipe()

    for num, directoin in myInput:
        if directoin == 0:
            myPipe.addLeft(num)
        else:
            myPipe.addRight(num)

    result = myPipe.getBeads()

    return result