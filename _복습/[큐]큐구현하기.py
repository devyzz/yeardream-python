from collections import deque

# 1 x : 큐에 정수 x를 입력
# 2 : 큐에서 정수를 제거
# 3 : 큐의 size 출력
# 4 : 큐가 비어있는지 여부 출력
# 5 : 큐의 head 값 출력
# 6 : 큐의 rear 값 출력


class Queue:
    def __init__(self):
        self.q = deque()

    def push(self,x):
        self.q.append(x)

    def pop(self):
        if self.q:
            self.q.popleft()

    def size(self):
        return len(self.q)

    def empty(self):
        return (0 if self.q else 1)

    def front(self):
        if self.q:
            return self.q[0]
        else:
            return -1

    def back(self):
        if self.q:
            return self.q[-1]
        else:
            return -1


def main():
    queue = Queue()

    n = int(input())

    for i in range(n):
        temp = [int(v) for v in input().split()]
        x = int(temp[0])
        if x == 1:
            queue.push(temp[1])
        elif x == 2:
            queue.pop()
        elif x == 3:
            print(queue.size())
        elif x == 4:
            print(queue.empty())
        elif x == 5:
            print(queue.front())
        elif x == 6:
            print(queue.back())

if __name__ == "__main__":
    main()