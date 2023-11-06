# kthSmallest

# return sorted tree in order (build an array), then take kth index
# beware! this is a 1-indexed k given 


def kthSmallest(root, k):
    def inorder(root):
        res = []
        if root:
            res = res + inorder(root.left)
            res.append(root.val)
            return res + inorder(root.right)
        else: 
            return res

    return inorder(root)[k-1]