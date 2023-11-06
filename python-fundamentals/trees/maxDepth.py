# maxDepth


def maxDepth(root):

    def traversal(root, curDepth):
        res = []
        if root:
            res = res + traversal(root.left, curDepth + 1)
            res.append(curDepth)
            return res + traversal(root.right, curDepth + 1)
        else: 
            res.append(curDepth)
            return res
    return max(traversal(root, 0))

