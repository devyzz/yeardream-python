class Tree:
    def __init__(self, index, left, right): #트리 생성자
        self.index = index  #현재 노드의 고유의 값
        self.left = left    # 왼쪽 자식 노드 (Node객체 또는 None)
        self.right = right  # 오른쪽 자식 노드

    def addNode(self, index, left, right):
        if self.index is None:
            self.index = index
            if left is not None:
                self.left = Tree(left, None, None)
            if right is not None:
                self.right = Tree(right, None, None)
            return

        if self.index == index:
            if left is not None:
                self.left = Tree(left, None, None)
            else:
                self.left = None

            if right is not None:
                self.right = Tree(right, None, None)
            else:
                self.right = None
            return

        if self.left is not None:
            self.left.addNode(index, left, right)
        if self.right is not None:
            self.right.addNode(index, left, right)



'''
## 테스트용 ##
myTree = Tree(None, None, None)
n = int(input())

for i in range(n) :
    myList = [int(v) for v in input().split()]
    if myList[1] == -1 :
        myList[1] = None
    if myList[2] == -1 :
        myList[2] = None
    myTree.addNode(myList[0], myList[1], myList[2])
'''