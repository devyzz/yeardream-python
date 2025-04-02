class Queue:
    def __init__(self):
        self.myQueue = []

    def push(self, n):
        self.myQueue.append(n)

    def pop(self):
        if self.myQueue:
            self.myQueue.pop(0)

    def size(self):
        return len(self.myQueue)

    def empty(self):
        if self.myQueue:
            return 0
        else:
            return 1

    def front(self):
        if self.myQueue:
            return self.myQueue[0]
        else:
            return -1

    def back(self):
        if self.myQueue:
            return self.myQueue[-1]
        else:
            return -1

