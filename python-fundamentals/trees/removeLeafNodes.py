def removeLeafNodes(root, target):
    if not root: 
        return root

    left = removeLeafNodes(root.left, target)
    right = removeLeafNodes(root.right, target)

    if root.val == target: 
        if not left and not right:
            return None

    root.left = left
    root.right = right
    return root