# 5:29 5:39 w/ submission and review of notes

# Time: O(height)
# Space: O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    if not root:         
        return TreeNode(val)
    
    node = root
    while True: 
        if val < node.val: 
            if node.left == None: 
                node.left = TreeNode(val)
                return root
            else: 
                node = node.left
        elif val > node.val:
            if node.right == None: 
                node.right = TreeNode(val)
                return root
            else: 
                node = node.right