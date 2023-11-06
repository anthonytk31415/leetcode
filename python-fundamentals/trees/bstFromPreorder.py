# Trick: find the index that's greater than the root and then recursively call the function on two arrays: 
# - left = values < root, and right= values > root


# Time: O(Nlogn) - do it N times, then each Nth time, you split it in half 
# Space: O(N) for the tree itself? 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# uses O(1) space but O(nlogn) time; most intuitive?
def bstFromPreorder(preorder): 

    # base case: if preorder is empty, return None
    if not preorder: 
        return None
    else: 
        root = TreeNode(preorder[0])
        # find index where the first x > root.val exists
        if preorder[1:]:
            r_idx = None
            for i in range(1, len(preorder)):
                if preorder[i] > preorder[0]:
                    r_idx = i
                    break
            if r_idx: 
                left = preorder[1:r_idx]
                right = preorder[r_idx:]
            else: 
                left = preorder[1:]
                right = None
            root.left = bstFromPreorder(left)
            root.right = bstFromPreorder(right)
        return root


from math import inf

# this is a O(n) solution since you know the order you need to traverse; 
# the function is called exactly n times
def bstFromPreorder1(preorder): 
    index=[0]

    def bst_helper(arr, upp_bound, index):
        if index[0] >= len(arr) or arr[index[0]] > upp_bound:
            return 
        root = TreeNode(arr[index[0]])
        index[0] +=1
        root.left = bst_helper(arr, root.val, index)
        root.right = bst_helper(arr, upp_bound, index)
        return root

    return bst_helper(preorder, inf, index)