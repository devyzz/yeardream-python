# 구슬넣기 (배열)

# a, b가 입력값으로 주어졋을 때 b가 0이면 왼쪽, b가 1이면 오른쪽에 구슬(a)를 넣는다.
# 최종적으로 어떻게 구슬이 저장되어 있는지 리턴할 것
# 구슬을 넣는 배열을 만들 것

class ListPipe:
    def __init__(self):
        self.beads = []

    def addLeft(self,x):
        self.beads.insert(0,x)

    def addRight(self, x):
        self.beads.append(x)

    def getPipe(self):
        return(self.beads)


def processBeads(myInput):

    # myInput[i][0] : i번째에 넣는 구슬의 번호
    # myInput[i][1] : i번째에 넣는 방향
    #
    # 예를 들어, 예제의 경우
    #
    # myInput[0][0] = 1, myInput[0][1] = 0,
    # myInput[1][0] = 2, myInput[1][1] = 1,
    # myInput[2][0] = 3, myInput[2][1] = 0

    pipe = ListPipe()

    for target in myInput:
        num = target[0]
        direction = target[1]

        if direction == 0:
            pipe.addLeft(num)
        else:
            pipe.addRight(num)

    return pipe.getPipe()


def main():
    n = int(input())

    myList = []

    for i in range(n) :
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))

if __name__ == "__main__":
    main()
