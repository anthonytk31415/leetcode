# pathsum
# https://leetcode.com/problems/path-sum/

class Node:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, targetSum):
        if root: 
            targetSum = targetSum - root.val
            if root.right == None and root.left == None:
                if targetSum == 0: 
                    return True
                else:
                    return False
            # elif targetSum <= 0: 
            #     return False
            else: 
                return (Solution.hasPathSum(self, root.left, targetSum) or 
                        Solution.hasPathSum(self, root.right, targetSum))
        else: 
            return False  