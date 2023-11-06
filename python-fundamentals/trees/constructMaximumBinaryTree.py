# 109; 1:19



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    
    if not nums: 
        return None
    else: 
        n_max = max(nums)
        n_max_index = nums.index(n_max)
        left_prefix = nums[:n_max_index]
        right_suffix = nums[n_max_index+1:]
        root = TreeNode(n_max)
        root.left = self.constructMaximumBinaryTree(left_prefix)
        root.right = self.constructMaximumBinaryTree(right_suffix)
        return root