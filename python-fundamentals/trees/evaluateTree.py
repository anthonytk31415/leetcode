
# leaf: 0 = False, 1 = True
# non-leaf: 2 = or, 3 = and


# Time: O(n)
# Space: O(1)

def evaluateTree(root):
    # no children
    if root.val <= 1: 
        return bool(root.val)
    # children: 
    else: 
        if root.val == 2: 
            return evaluateTree(root.left) or evaluateTree(root.right)
        else: 
            return evaluateTree(root.left) and evaluateTree(root.right)