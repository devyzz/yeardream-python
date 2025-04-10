import heapq
class PriorityQueue:

    def __init__(self):
        self.data = []

    def push(self, value):
        heapq.heappush(self.data, (abs(value), value))  # 절대값, 원래값을 튜플형태로 입력함

    def pop(self):
        if len(self.data) > 0:
            heapq.heappop(self.data)

    def top(self):
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0][1]