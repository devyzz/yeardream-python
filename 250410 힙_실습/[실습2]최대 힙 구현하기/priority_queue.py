import heapq

class PriorityQueue:
    def __init__(self):
        self.data = [0]

    def push(self,value):
        heapq.heappush(self.data, -value)   # 부호를 반전시켜 넣음

    def pop(self):
        if self.data:
            return -heapq.heappop(self.data)  # 다시 부호 반전하여 반환

    def top(self):
        if self.data:
            return -self.data[0]
        return -1
