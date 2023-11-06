# 11:26 11:42; can we do this with O(1) space? 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n) for n nodes
# Space: O(n) as we create an array and use that array to build the new tree
def flatten2(root): 
    """
    Do not return anything, modify root in-place instead.
    """
    if not root: 
        return root
    pre = preorder(root)[1:]
    node = root
    node.left = node.right = None
    while pre:
        node.right = TreeNode(pre.pop(0))
        node = node.right
        

def preorder(root): 
    res = []
    if not root: 
        return res
    else: 
        res.append(root.val)
        res = res + preorder(root.left)
        return res + preorder(root.right)


# doing this in O(1) space: 
# trick: flatten the left, then make root.right = root.left and what was root.right, append it all the way to 
#   the right most  node of what was root.left

def flatten(root):
    while root: 
        if root.left: 
            flatten(root.left)
            tail = root.left
            while tail.right: 
                tail = tail.right
            tail.right = root.right
            root.right = root.left
            root.left = None
        root = root.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)



flatten(root)
print(preorder(root))
