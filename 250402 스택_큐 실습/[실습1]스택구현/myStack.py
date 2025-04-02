class Stack:
    def __init__(self) :
        self.myStack = []

    def push(self, n) :
        self.myStack.append(n)

    def pop(self) :
        if self.myStack:
            self.myStack.pop()

    def size(self) :
        return len(self.myStack)

    def empty(self) :
        if self.myStack:
            return 0
        else:
            return 1

    def top(self) :
        if self.myStack:
            return self.myStack[-1]
        else:
            return -1