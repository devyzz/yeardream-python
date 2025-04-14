import heapq

class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, value):
        heapq.heappush(self.data, (abs(value),value))

    def pop(self):
        if self.data:
            heapq.heappop(self.data)

    def top(self):
        if self.data:
            return self.data[0][1]
        else:
            return -1