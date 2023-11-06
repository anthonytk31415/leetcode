class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def invertTree(root):
    def helper(root):
        if root:
            newNode = TreeNode(root.val)
            newNode.left = helper(root.right)
            newNode.right = helper(root.left) 
            return newNode
        else:
            return None
    return helper(root)



def inordertraversal(root):
    res = []
    if root:
        res = res + inordertraversal(root.left)
        res.append(root.val)
        return res + inordertraversal(root.right)
    else: 
        return res

print(inordertraversal(root))

x = invertTree(root)
print(inordertraversal(x))