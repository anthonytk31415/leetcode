# isValidBST

# the intuition is that you create a helper function with a min and a max.
# When you call the function recursively on each node, you check that the node is betweem min and max.
# when you go left, you min = node.val so that when its checked on the child, parent.val child.val < parent.val
# when you go right, new max = node.val so child.val >  parent.val


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traversal(self, root):
        res = []
        if root: 
            res = res + self.traversal(root.left)
            res.append(root.val)
            return res + self.traversal(root.right)
        else: 
            return res

    # def isValidBST(self, root):

    #     def traversal(root):
    #         res = []
    #         if root: 
    #             res = res + traversal(root.left)
    #             res.append(root.val)
    #             return res + traversal(root.right)
    #         else: 
    #             return res
    #     if root:     
    #         left_test = True
    #         right_test = True
    #         left_children_all_test = True
    #         right_children_all_test = True
    #         if root.left:
    #             left_test = (root.val > root.left.val)
    #             left_children_all_test = (root.val > max(traversal(root.left)))
    #         if root.right: 
    #             right_test = (root.val < root.right.val)
    #             right_children_all_test = (root.val < min(traversal(root.right)))
    #         return all([left_test, right_test, left_children_all_test, right_children_all_test, 
    #                         self.isValidBST(root.left), self.isValidBST(root.right)])     
    #     else: 
    #         return True


def isValidBST(root):
    def helper(root, minVal, maxVal):
        if root == None:
            return True
        if root.val <= minVal or root.val >= maxVal:
            return False
        else: 
            return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)
    return helper(root, (-2**31), (2**31))


#[5,1,6,null, null, 3, 9] # false

root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.right.left = TreeNode(22)
root.right.right = TreeNode(40)

# print(root.val)
# print(root.left.val)

# print(root.traversal(root))
print(isValidBST(root))