def longestUnivaluePath(root):
    if not root:
        return 0
    res = [0]
    if root.left:
        if root.left.val == root.val:
            res.append(1 + longestUnivaluePath(root.left))
        else: 
            res.append(longestUnivaluePath(root.left))
    if root.right:
        if root.right.val == root.val:
            res.append(1 + longestUnivaluePath(root.right))
        else: 
            res.append(longestUnivaluePath(root.right))
    return max(res)