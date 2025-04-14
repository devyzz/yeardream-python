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

def inorder(node, depth, result=None):
    if result is None:
        result = []

    if node is None:
        return result

    inorder(node.left, depth+1, result)
    result.append(node)
    node.depth = depth
    inorder(node.right, depth+1, result)

    return result

def getWidth(myTree):
    result = inorder(myTree, 1)
    n = len(result)

    left = [1001] * n
    right = [-1] * n
    maxDepth = 0

    for i in range(n):
        d = result[i].depth
        left[d] = min(left[d], i)
        right[d] = max(right[d], i)
        maxDepth = max(maxDepth, d)

    answerD = 0
    answerW = 0

    for i in range(1, maxDepth+1):
        temp = right[i] - left[i] + 1

        if answerW < temp:
            answerW = temp
            answerD = i

    return (answerD, answerW)


def main():
    myTree = Tree(None, None, None)

    n = int(input())

    for i in range(n) :
        myList = [int(v) for v in input().split()]

        if myList[1] == -1 :
            myList[1] = None

        if myList[2] == -1 :
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*getWidth(myTree))


if __name__ == "__main__":
    main()
