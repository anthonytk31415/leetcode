class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) Time and Space
# create a memo for when you traverse a node and keep track of when that node returns something 

def rob(root):
    memo = {}
    def helper(node, prev, memo):               
        if not node:
            return 0
        else: 
            if (node, prev) in memo:
                return memo[(node, prev)]

            else: 
                res = None
                if prev == 1: 
                    res = helper(node.left, 1-prev, memo) + helper(node.right, 1-prev, memo) 
                else: 
                    res = max(node.val + helper(node.left, 1-prev, memo) + helper(node.right, 1-prev, memo), 
                            helper(node.left, 0, memo) + helper(node.right, 0, memo))
                memo[(node, prev)] = res
                return res

    return helper(root, 0, memo)


root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(3)

print(rob(root))