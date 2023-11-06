## tree traversal 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def left_traversal(node):
#     res = []
#     if node:
#         res = left_traversal(node.left)
#         res.append(node.val)
#         res = res + left_traversal(node.right)
#     else:
#         res.append(None)
#     return res


# def right_traversal(node):
#     res = []
#     if node:
#         res = right_traversal(node.right)
#         res.append(node.val)
#         res = res + right_traversal(node.left)
#     else:
#         res.append(None)
#     return res

# root = TreeNode(1)
# root.left= TreeNode(2)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(2)
# root.right= TreeNode(2)
# root.right.left = TreeNode(2)
# # root.right.right = TreeNode(2)



# print(root.val)
# print(root.left.val)
# print(root.right.val)
# # print(traversal(root))

# left = left_traversal(root)
# right = right_traversal(root)

# print(left)
# print(right)

# def isSymmetric(root):
#     left = left_traversal(root.left)
#     right = right_traversal(root.right)
#     # print(f'{left}')
#     # print(f'{right}')
#     if left==right:
#         return True
#     else:
#         return False

# left = [3, 2, 4]
# right = [4, 2, 3]

# x2 = [1,2,2,2,None,2]

# print(isSymmetric(root))




def isSymmetric(root):
    def traversal(x, y):
        #if both null 
        if not x and not y: 
            return True

        # of either are null but not both (since we checked condition above)
        if not x or not y:
            return False
        
        #recursively call when both nodes are equal 
        if x.val == y.val: 
            return traversal(x.left, y.right) and traversal(x.right, y.left)

        # if they're not equal (because of condition above), then return false
        return False
    
    if not root:
        return True
    
    else:
        return traversal(root.left, root.right)
