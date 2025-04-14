# 구슬넣기 (배열)

# a, b가 입력값으로 주어졋을 때 b가 0이면 왼쪽, b가 1이면 오른쪽에 구슬(a)를 넣는다.
# 최종적으로 어떻게 구슬이 저장되어 있는지 리턴할 것
# 구슬을 넣는 연결리스트를 만들 것
## 배열과 달리, 연결리스트는 노드들의 연결로 이루어지므로 노드 클래스 / 연결리스트 클래스를 따로 지정해줘야함!!!

class LinkedListElement:
    def __init__(self, val, nextNode):
        self.val = val
        self.nextNode = nextNode

class LinkedListElement:
    def __init__(self, val, nextNode):
        self.val = val
        self.nextNode = nextNode

class LinkedListPipe:
    def __init__(self):
        self.start = None
        self.end = None

    def addRight(self, x):
        element = LinkedListElement(x, None)
        if self.start is None and self.end is None:
            self.start = element
            self.end = element
        else:
            self.end.nextNode = element
            self.end = element  # 🔥 꼭 필요!

    def addLeft(self, x):
        element = LinkedListElement(x, self.start)
        self.start = element
        if self.end is None:  # 리스트가 비어 있었던 경우
            self.end = element

    def getPipe(self):
        result = []
        cur = self.start
        while cur is not None:
            result.append(cur.val)
            cur = cur.nextNode
        return result

def processBeads(myInput):
    '''
    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0
    '''
    pipe = LinkedListPipe()

    for target in myInput:
        num = target[0]
        direction = target[1]

        if direction == 0:
            pipe.addLeft(num)
        else:
            pipe.addRight(num)

    result = pipe.getPipe()
    return result


def main():
    n = int(input())

    myList = []

    for i in range(n) :
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))

if __name__ == "__main__":
    main()