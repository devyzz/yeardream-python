import heapq

class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self,value):
        heapq.heappush(self.data, value)

    def pop(self):
        if self.data:
            return heapq.heappop(self.data)

    def top(self):
        if self.data:
            return self.data[0]
        return -1

def heapSort(items):
    result = []

    pq = PriorityQueue()

    for item in items:
        pq.push(item)

    for i in range(len(items)):
        result.append(pq.pop())

    return result

