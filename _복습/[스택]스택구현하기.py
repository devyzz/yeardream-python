# 스택 구현하기
# 1 x : 스택에서 정수 x를 입력
# 2 : 스택에서 정수를 제거
# 3 : 스택의 size 출력
# 4 : 스택이 비어있는지 여부 출력
# 5 : 스택의 꼭대기값 출력

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


def main():
    stack = Stack()
    n = int(input())

    for i in range(n):
        temp = [int(v) for v in input().split()]

        x = temp[0]

        if x == 1:
            stack.push(temp[1])
        elif x == 2:
            stack.pop()
        elif x == 3:
            print(stack.size())
        elif x == 4:
            print(stack.empty())
        elif x == 5:
            print(stack.top())


if __name__ == "__main__":
    main()