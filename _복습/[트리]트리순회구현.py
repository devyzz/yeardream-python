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

def preorder(tree): # 뿌 - 왼 - 오
    result = [tree.val]
    if tree.left:
        result.extend(preorder(tree.left))
    if tree.right:
        result.extend(preorder(tree.right))
    return result

def inorder(tree): # 왼 - 뿌 - 오
    result = []
    if tree.left:
        result.extend(inorder(tree.left))
    result.append(tree.val)
    if tree.right:
        result.extend(inorder(tree.right))
    return result

def postorder(tree): # 왼 - 오 - 뿌
    result = []

    if tree.left:
        result.extend(postorder(tree.left))
    if tree.right:
        result.extend(postorder(tree.right))
    result.append(tree.val)

    return result


def main():
    myTree = Tree(None, None, None)

    n = int(input())

    for i in range(n):
        myList = [int(v) for v in input().split()]

        if myList[1] == -1:
            myList[1] = None

        if myList[2] == -1:
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))

if __name__ == "__main__":
    main()
