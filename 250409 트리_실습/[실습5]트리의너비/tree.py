class Tree:
    def __init__(self, index, left, right): #트리 생성자
        self.index = index  #현재 노드의 고유의 값
        self.left = left    # 왼쪽 자식 노드 (Node객체 또는 None)
        self.right = right  # 오른쪽 자식 노드

    def addNode(self, index, left, right):
        if self.index is None:      # 루트 노드가 존재하지 않는다면
            self.index = index      # 현재 노드에 index값을 할당하여 루트 노드 생성
            if left is not None:    # 왼쪽 노드가 있다면
                self.left = Tree(left, None, None)  # 새로만든 노드의 왼쪽 노드에 받아온 left할당
            if right is not None:   # 오른쪽 노드가 있다면
                self.right = Tree(right, None, None)    # 새로만든 노드의 오른쪽 노드에 받아온 right 할당
            return

        if self.index == index:     # 현재 노드가 찾고자 하는 노드인 경우 == 노드의 자식을 새로 연결하는 경우
            if left is not None:
                self.left = Tree(left, None, None)
            else:
                self.left = None

            if right is not None:
                self.right = Tree(right, None, None)
            else:
                self.right = None
            return

        # index가 현재 노드가 아니라면 노드의 왼쪽과 오른쪽을 탐색하며 내려가면서 addNode (재귀탐색)
        if self.left is not None:
            self.left.addNode(index, left, right)
        if self.right is not None:
            self.right.addNode(index, left, right)
