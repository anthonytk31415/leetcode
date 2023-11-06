### is isValidBST

def isValidBST(root):
    def validBSThelper(root, min, max):
        if root:            
            return (root.val > min and root.val < max) and validBSThelper(root.left, min, root.val) and validBSThelper(root.right, root.val, max) 
        else: 
            return True
    return validBSThelper(root, -2 ** 34, 2 ** 34 - 1)

