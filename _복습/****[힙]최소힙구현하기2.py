class PriorityQueue:
    def __init__(self):
        self.heap = [0]

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 1:
            parent = i // 2
            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def top(self):
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]

    def pop(self):
        if len(self.heap) <= 1:
            return

        self.heap[1] = self.heap[-1]
        self.heap.pop()

        i = 1
        size = len(self.heap)

        while True:
            left = i * 2
            right = i * 2 + 1
            min_child = i

            if left < size and self.heap[left] < self.heap[min_child]:
                min_child = left
            if right < size and self.heap[right] < self.heap[min_child]:
                min_child = right

            if min_child == i:
                break

            self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
            i = min_child
