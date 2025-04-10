class PriorityQueue:
    def __init__(self):
        self.data = [0]

    def push(self, value):

        self.data.append(value)
        index = len(self.data) - 1

        while index != 1: # 마지막으로 삽입한 값이 루트 노드가 되면 반복문 종료
            if self.data[index//2] > self.data[index] : # 부모의 value가 자신보다 크다면
                tmp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = tmp

                index = index // 2 # 부모 노드로 올라갔으므로, index를 바꿈
            else:
                break #완전 이진 트리 조건을 만족하므로 그냥 break

    def top(self):
        if len(self.data) == 1:
            return -1 # 아무것도 없는 빈 트리이므로 -1 반환
        else:
            return self.data[1]

    def pop(self):
        if len(self.data) == 1:
            return # pop을 처리하지 않고 return

        # 마지막 노드를 루트 노드 자리로 이동한다.
        self.data[1] = self.data[-1]
        self.data.pop()

        index = 1

        while True:
            '''
            priority 현재 노드(index)가 두 자식 중 누구랑 자리를 바꿔야할 지 선택하기 위해 사용하는 변수
            자식이 없다면 바꿀 필요 없으므로 break
            왼쪽 자식만 있다면 왼쪽 자식과 자리를 바꿔야하므로 priority = 왼쪽자식
            자식이 모두 있다면 둘 중 더 작은 자식과 자리를 바꿔야 하므로, 작은쪽의 인덱스를 priority에 저장
            --> 자식과 루트가 자리를 바꿔야하므로, 더 작은 자식과 루트가 바뀌어야 나머지 자식도 루트와 비교했을 때 힙조건을 만족하므로!!!
            '''
            priority = -1
            # 1. 자식이 없는 경우
            if len(self.data) - 1 < index * 2: # 전체 길이가 왼쪽자식보다 작으면 왼쪽자식이 없다는 거임
                break
            # 2. 왼쪽 자식만 있는 경우
            elif len(self.data) - 1 < index * 2 + 1: # 왼쪽 자식에 대한 분기는 통과 / 오른쪽 자식의 인덱스보다 작음 == 왼쪽 자식만 존재
                priority = index * 2
            # 3. 왼/오 자식이 다 있는 경우
            else:
                if self.data[index*2] < self.data[index*2 + 1]: #왼쪽 자식이 오른쪽 자식보다 값이 작다면
                    priority = index * 2            # prioirty를 왼쪽으로 옮겨줌
                else:
                    priority = index * 2 + 1        # 왼쪽 자식이 오른쪽 자식보다 크다면 priority를 오른쪽으로 옮김


            if self.data[index] > self.data[priority]:
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp
                index = priority
            else:
                break

