
# Time: O(n); traverse once through the tree
# Space: O(n); store the target-k value in a hash set

def findTarget(root, k):
    target = set()
    true_cond = [False]
    def traversal(root, target, k, true_cond):
        if true_cond[0]: 
            return 
        elif not root:
            return
        else: 
            if root.val in target: 
                true_cond[0] = True
                return
            else: 
                target.add(k - root.val)
                traversal(root.left, target, k, true_cond)
                traversal(root.right, target, k, true_cond)
    traversal(root, target, k, true_cond)
    return true_cond[0]
    