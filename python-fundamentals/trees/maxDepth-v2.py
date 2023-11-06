# max depth 

# program recursively in each parent: 
# if node: return 1 + max(fn(root.left), fn(root.right))
# else: return 0

#Time: O(n)
# space: O(1)

def maxDepth(root): 
    if not root: 
        return 0
    else: 
        return 1 + max(maxDepth(root.left), maxDepth(root.right))