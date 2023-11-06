def lowestCommonAncestor(root, p, q):
    # base case: 
    if not root: 
        return False
    if root == p or root == q: 
        return root
    
    else: 
        left = lowestCommonAncestor(root.left, p, q)
        right = lowestCommonAncestor(root.right, p, q)
        if left == False and right != False:
            return right

        elif right == False and left != False:
            return left

        elif left != False and right != False: ## left and rigth both are not false
            return root
        
        else: # both are false 
            return False





