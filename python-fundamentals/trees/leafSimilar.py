def leafSimilar(root1, root2):

    def dfs(root):
        res = []
        if not root: return res
        if not root.left and not root.right: return [root.val]
        if root.left: res += dfs(root.left)
        if root.right: res += dfs(root.right)
        return res
    
    r1, r2 = dfs(root1), dfs(root2)
    if len(r1) != len(r2): return False
    for i in range(len(r1)):
        if r1[i] != r2[i] : return False
    return True
