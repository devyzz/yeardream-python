def preorder(tree) :
    result = []

    result.append(tree.index)

    if tree.left != None :
        result = result + preorder(tree.left)

    if tree.right != None :
        result = result + preorder(tree.right)

    return result

def inorder(tree) :
    result = []

    if tree.left != None :
        result = result + inorder(tree.left)

    result.append(tree.index)

    if tree.right != None :
        result = result + inorder(tree.right)

    return result

def postorder(tree) :
    result = []

    if tree.left != None :
        result = result + postorder(tree.left)

    if tree.right != None :
        result = result + postorder(tree.right)

    result.append(tree.index)

    return result