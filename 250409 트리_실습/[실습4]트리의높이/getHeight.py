def getHeight(myTree) :
    if myTree == None :
        return 0
    else :
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))