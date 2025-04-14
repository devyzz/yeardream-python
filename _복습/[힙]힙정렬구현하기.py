import heapq

class PriorityQueue:    # 최소힙 기반 큐
    def __init__(self):
        self.data = []

    def push(self, value):
        heapq.heappush(self.data, value)

    def pop(self):
        if self.data:
            heapq.heappop(self.data)

    def top(self):
        if self.data:
            return self.data[0]
        else:
            return -1

def heapSort(items):

    result = []
    pq = PriorityQueue()

    for item in items:
        pq.push(item)

    for i in range(len(items)):
        result.append(pq.top())
        pq.pop()

    return result


def main():
    line = [int(x) for x in input().split()]
    print(*heapSort(line))

if __name__ == "__main__":
    main()





