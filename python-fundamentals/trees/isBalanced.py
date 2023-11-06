# isBalanced
# time: O(N) - need to check all nodes for verifying depth and if it's balanced
# space: O(1) -     

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
# root.left.right.left = TreeNode(6)

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        else: 
            return ((abs(depth(root.left) - depth(root.right)) <=1) and 
                    self.isBalanced(root.left) and 
                    self.isBalanced(root.right)
                   )
# conditions for balanced binary tree:

# max depth for each child between -1 and 1



# each child has to be balanced



def depth(root):
    if root: 
        return 1 + max(depth(root.left), depth(root.right))
    else:
        return 0


# def hello(num)
#     if num > 3: return 1, 0


# print(depth(root))

print(Solution.isBalanced('a', root))


# print(hello(9))