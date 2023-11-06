def minDepth(root):
    if not root: 
        return 0
    else: 
        return min(1 + minDepth(root.left), 1 + minDepth(root.right))

def minDepth(root):
    if root and not root.left and not root.right: 
        return 0
    elif root and not root.left:
        return (1 + self.minDepth(root.right))
    elif root and not root.right: 
        return (1 + self.minDepth(root.left))
    else: 
        return min(1+self.minDepth(root.left), 1+self.minDepth(root.right))