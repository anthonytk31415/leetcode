# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 733 758; 
# 25 min; poorly worded part - if the root contians 
# 0 and children do not contain 1, does that get removed? apparently yes!

# Time: O(n) (traverse all the nodes once)
# Space: O(1)

def pruneTree(root):

    # this will remove the node if node is nonzero and has no children of 1
    def helper(root):
        if not root: 
            return None
        # base case: no children 
        root.left = helper(root.left)
        root.right = helper(root.right)
        if not root.left and not root.right and root.val !=1: 
            return None
        else: 
            return root
    return helper(root) 
