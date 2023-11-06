# diameterOfBinaryTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(44)
root.left.left.left.left = TreeNode(12)
root.left.right = TreeNode(4)
# root.left.right.right = TreeNode(4)
# root.left.right.right.right = TreeNode(14)
# root.right.right = TreeNode(5)
# root.right.right.left = TreeNode(6)
# root.right.right.left.left = TreeNode(7)

def maxEdges(root):
    if root: 
        if root.left or root.right: 
            return 1 + max(maxEdges(root.left), maxEdges(root.right))
    return 0


# 2 numbers: 
# (a) max of: (1) max edges from left and right, (2) max of left, (3) max of right
# (b) 

def diameterOfBinaryTree(root):
    def helper(root):
        if not root: 
            return 0
        else: 
            left_max, right_max = 0, 0
            if root.left: left_max = 1 + maxEdges(root.left)
            if root.right: right_max = 1 + maxEdges(root.right)
            v = left_max + right_max
            return max(helper(root.left), helper(root.right), v)
    return helper(root)
    


print(diameterOfBinaryTree(root))


# max edges left + max edges right, depth 
#
#


# print(maxEdges(root.left))