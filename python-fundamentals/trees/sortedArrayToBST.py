# sortedArrayToBST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    if len(nums) == 0: 
        return None
    if len(nums) == 1: 
        return TreeNode(nums[0])
    q = len(nums)//2
    root = TreeNode(nums[q])
    root.left = sortedArrayToBST(nums[:q])
    root.right = sortedArrayToBST(nums[q+1:])
    return root


[0,1,2,3,4,5,6,7,]