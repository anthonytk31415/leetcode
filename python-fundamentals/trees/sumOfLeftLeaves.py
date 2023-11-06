

def sumOfLeftLeaves(root):
    
    if not root: 
        return 0

    res = 0
    # has children 
    if root and root.left and not root.left.left and not root.left.right: 
        res += root.left.val

    # recurisvely call
    return res + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)