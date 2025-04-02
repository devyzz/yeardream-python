class maxMachine:
    def __init__(self):
        self.numbers = []

    def addNumber(self, n):
        self.numbers.append(n)

    def removeNumber(self, n):
        if n in self.numbers:
            self.numbers.remove(n)

    def getMax(self):
        if self.numbers:
            return max(self.numbers)
        return None