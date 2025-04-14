# 자신만의 배열을 가진 클래스를 구성할 것
# addNumber - 정수추가
# removeNumber - 정수제거
# getMax - 배열의 최대값 반환

class maxMachine:
    def __init__(self):
        self.numbers = []

    def addNumber(self, x):
        self.numbers.append(x)

    def removeNumber(self, x):
        if x in self.numbers:
            self.numbers.remove(x)

    def getMax(self):
        return (max(self.numbers))