from collections import deque

class Tree:
    def __init__ (self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def addNode(self, v, l, r):
        if self.value is None or self.value == v:
            self.value = v
            self.left = Tree(l, None, None) if l is not None else None
            self.right = Tree(r, None, None) if r is not None else None
            return True

        else:
            flag = False
            if self.left is not None:
                flag = self.left.addNode(v, l, r)

            if flag == False and self.right is not None:
                flag = self.right.addNode(v,l,r)

            return flag


def BFS(tree):
    result = []
    dq = deque()
    dq.append(tree)

    while dq:
        cur = dq.popleft()
        if cur is None:
            continue
        result.append(cur.value)

        dq.append(cur.left)
        dq.append(cur.right)

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

    print(*BFS(myTree))

if __name__ == "__main__":
    main()
