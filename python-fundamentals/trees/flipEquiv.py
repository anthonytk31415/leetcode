def flipEquiv(root1, root2):
    if not root1 and not root2: 
        return True
    elif (root1 and not root2) or (not root1 and root2):
        return False
    elif root1.val != root2.val: 
        return False
    else: # values equal
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or 
                self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right))
        
