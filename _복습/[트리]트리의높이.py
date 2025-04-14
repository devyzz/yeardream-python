class Tree:
    def __init__ (self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addNode(self, v, l, r):
        if self.val is None or self.val == v:
            self.val = v
            self.left = Tree(l, None, None) if l is not None else None
            self.right = Tree(r, None, None) if r is not None else None
            return True

        else:
            flag = False
            if self.left is not None:
                flag = self.left.addNode(v,l,r)
            if flag is False and self.right is not None:
                flag = self.right.addNode(v,l,r)
            return flag


def getHeight(myTree):
    if myTree is None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))