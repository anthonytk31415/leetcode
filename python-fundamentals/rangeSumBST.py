# Range Sum of BST
def rangeSumBST(root, low, high):
    if root == None:
        return 0
    elif root.val >= low and root.val <= high:
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
    elif root.val < low:
        return self.rangeSumBST(root.right, low, high)
    elif root.val > high:
        return self.rangeSumBST(root.left, low, high)


# worst case: O(n) where we have to traverse all nodes