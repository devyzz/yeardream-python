class ListPipe:

    def __init__(self):
        self.myPipe = []

    def addLeft(self, n):
        self.myPipe.insert(0, n)

    def addRight(self, n):
        self.myPipe.append(n)

    def getBeads(self):
        return self.myPipe


def processBeads(myInput):
    myPipe = ListPipe()

    for bead, direction in myInput:
        if direction == 0:
            myPipe.addLeft(bead)  # 왼쪽에 추가
        else:
            myPipe.addRight(bead)  # 오른쪽에 추가

    result = myPipe.getBeads()

    return result