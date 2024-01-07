def sumNumbers(root):

    res = [0]
    def dfs(node, curSum):
        curRes = curSum + node.val
        if node.left == None and node.right == None: 
            res[0] += curRes
            return curSum + node.val
        for child in [node.left, node.right]: 
            if child: dfs(child, curRes*10)
    
    dfs(root, 0)
    return res[0]


x = None
print(x == None)