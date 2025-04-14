# 0 x : 정수 x를 힙에 입력
# 1 : 힙의 우선순위가 가장 높은 원소 제거
# 2 : 힙의 우선순위가 가장 높은 원소 조회

from collections import deque
import heapq

class PriorityQueue: #최소힙 기반 우선순위 큐
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)

    def top(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0


class PriorityQueue: # 우선순위 큐 클래스 (덱으로 구현) - 틀리진않음. 이진트리같은 재정렬은 안되지만 최대값인 큐를 뽑는다는 의미에서 동일한 거임.. 근데 왜 최대원소?
    def __init__(self):
        self.queue = deque()

    def push(self, item): # 원소 추가
        self.queue.append(item)

    def pop(self): # 가장 큰 원소 제거
        if not self.queue:
            return None
        min_item = min(self.queue) # 가장 큰 원소 찾기
        self.queue.remove(min_item) # 가장 큰 원소 제거
        return min_item

    def is_empty(self): # 큐가 비어있는지 확인
        return len(self.queue) == 0


class PriorityQueue:    # 우선순위 큐 덱없이 구현
    def __init__(self):
        self.heap = [0] # 내부적으로 최소 힙을 저장할 리스트를 만든다. / 연산이 용이하도록 0번 인덱스는 사용하지 않고 비워둔다 -> 실제 인덱스는 1부터 시작

    def push(self, value):
        self.heap.append(value) # 새 값을 힙의 가장 마지막자리에 삽입. 완전 이진트리의 가장 오른쪽 아래
        i = len(self.heap) - 1  # 방금 추가된 인덱스를 변수 i로 저장한다 ( 가장 앞은 0으로 빈인덱스로 사용하지 않는데이므로 실제 index는 -1로 구함)

        while i > 1:            # 현재 노드가 루트 노드가 아닐동안 반복
            parent = i // 2     # 부모노드 = 현재 인덱스의 절반
            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent      # i는 다시 부모노드로 저장 / 부모노드의 부모노드로 다시재탐색을 위해 while문을 돔
            else:               # 부모노드에 도달하면 다시 검사할 것이 없으므로 종료
                break

    def top(self):              # 우선순위가 가장 높은 원소 self.heap[1] / 가장 앞 0번 인덱스는 사용하지 않으므로
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]

    def pop(self):              # 우선순위가 가장 높은 원소 제거 pop
        if len(self.heap) <= 1:
            return

        self.heap[1] = self.heap[-1]    # 일단 우선순위가 가장 높은 원소 자리에 가장 뒷 원소를 갖다 넣고
        self.heap.pop()                 # 마지막 원소는 젤 위로 올려놨으니 일단 중복이므로 맨뒤에거 제거

        i = 1                           # 다시 힙구조를 정렬하기 위해서 인덱스지정 (하향식 재정렬, 현재 바꿔놓았기 때문에 맨위에 노드가 가장 크다)
        size = len(self.heap)

        while True:
            left = i * 2                # 왼쪽 자식의 인덱스
            right = i * 2 + 1           # 오른쪽 자식의 인덱스
            min_child = i               # 최소 노드 후보 = 자기자신

            if left < size and self.heap[left] < self.heap[min_child]:  # 전체사이즈보다 왼쪽인덱스가 작음 (왼쪽자식존재) / 왼쪽자식의 값 < 나의값
                min_child = left                                        # 최소인덱스 = 왼쪽으로 바꿈
            if right < size and self.heap[right] < self.heap[min_child]:# 전체사이즈보다 오른쪽 인덱스가 작음 (오른쪽 존재) / 오른쪽자식의 값 < 나의값 // 위에서 왼쪽을 돌고 오른쪽을 온거임
                min_child = right                                       # 최소 인덱스 = 오른쪽으로 바꿈

            if min_child == i:                                          # 최소인덱스가 이미 지금 인덱스다 돌필요없음 break
                break

            self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]     # 최소인덱스의 값과 현재 인덱스의 값 교환
            i = min_child                                                               # 인덱스를 최소 인덱스로 교환
