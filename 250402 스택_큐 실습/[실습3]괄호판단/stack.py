class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, n):
        self.myStack.append(n)

    def pop(self):
        if self.myStack:
            self.myStack.pop()

    def size(self):
        return len(self.myStack)

    def empty(self):
        if self.myStack:
            return 0
        else:
            return 1

    def top(self):
        return self.myStack[-1] if self.myStack else -1


def checkParen(p):
    stack = Stack()
    for char in p:
        if char == '(':
            stack.push(char)
        else:
            if stack.empty():
                return "NO"
            stack.pop()

    return "NO" if stack.empty() == 0 else "YES"
