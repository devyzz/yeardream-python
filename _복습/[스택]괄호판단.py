class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        if self.s:
            self.s.pop()

    def size(self):
        if self.s:
            return len(self.s)

    def empty(self):
        return (0 if self.s else 1)

    def top(self):
        if self.s:
            return self.s[-1]
        else:
            return -1

def checkParen(x):
    stack = Stack()
    for char in x:
        if char == '(':
            stack.push(char)
        else:
            if stack.empty():
                return "NO"
            stack.pop()

    return "YES" if stack.empty() else "NO"


def main():
    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()