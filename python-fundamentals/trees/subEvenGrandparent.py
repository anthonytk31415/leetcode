# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 512; 519

# Time: O(n)
# Space: O(1)


def sumEvenGrandparent(root):

    if not root: 
        return 0

    # check for current's node's grandchildren the root is even: 
    res = 0
    if root.val %2 == 0: 
        if root.left: 
            if root.left.left: 
                res += root.left.left.val    
            if root.left.right: 
                res += root.left.right.val
        if root.right: 
            if root.right.left: 
                res += root.right.left.val    
            if root.right.right: 
                res += root.right.right.val
    # call the function recursively to root's children
    return res + sumEvenGrandparent(root.left) + sumEvenGrandparent(root.right)

