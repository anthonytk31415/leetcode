# invertTree
# intuition: at each step, if the root is not null, then swap the left and right and
# recursively call on left and right. 
# running time: O(n) as you will traverse all the nodes

# this one is clean and fast
def invertTree(root):
    def helper(root):
        if root: 
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            helper(root.left)
            helper(root.right)
    helper(root)
    return root

## rewrite using a stack:

