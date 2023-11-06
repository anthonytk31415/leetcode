def binaryTreePaths(root):
    res = []
    if not root: 
        return res
    
    def helper(root, path, res):
        if root: 
            if path == "": 
                path = path + str(root.val)
            else: 
                path = path + "->" + str(root.val) 
            if root.left: helper(root.left, path, res)
            if root.right: helper(root.right, path, res)
            if not root.left and not root.right: 
                res.append(path)
                return 
    helper(root, "", res)
    return res
