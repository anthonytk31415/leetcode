# Time: O(log(n))
# Space: O(1)

def searchBST(root, val):
    if not root: 
        return None
    elif root.val == val: 
        return root
    elif root.val > val: 
        return searchBST(root.left, val)
    else: 
        return searchBST(root.right, val)