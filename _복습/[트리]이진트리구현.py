class Tree:
    def __init__(self, val, left, right) :
        self.val = val
        self.left = left
        self.right = right

    def addNode(self, v, l, r) :
        if self.val is None or self.val == v :
            self.val = v
            self.left = Tree(l, None, None) if l is not None else None
            self.right = Tree(r, None, None) if r is not None else None
            return True

        else :
            flag = False
            if self.left is not None :
                flag = self.left.addNode(v, l, r)

            if flag == False and self.right is not None :    # 왼쪽 노드를 돌았다면 오른쪽은 안돌기 위해
                flag = self.right.addNode(v, l, r)

            return flag