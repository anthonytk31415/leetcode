# binary trees 



# balanced binary tree
# -- diff between left and right subtree is not more than 1
# -- left subtree is balanced
# -- right is balanced


# complete binary tree: 
# -- a binary tree where all the nodes are filled in the 2nd to last row and in the last row, they are filled left to right

# full binary tree: 
# - a binary tree where each node has 2 children or no children 


class Node: 
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

root = Node(30)
arr = [0,1,2,3,4,5,6,7]

# given an array, turn to a balanced binary tree
# O(n) time
def balancedBinaryTree(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return Node(arr[0])
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = balancedBinaryTree(arr[:mid])
    root.right = balancedBinaryTree(arr[mid+1:])
    return root

root = balancedBinaryTree(arr)

# traversal 
# - preorder
# - in order 
# - post order
# O(n) time

def inordertraversal(node):
    res = []
    if node: 
        res = res + inordertraversal(node.left)
        res.append(node.val)
        return res + inordertraversal(node.right)
    else: 
        return res

print(inordertraversal(root))

def preordertraversal(node):
    res = []
    if node: 
        res.append(node.val)
        res = res + preordertraversal(node.left)
        return res + preordertraversal(node.right)
    else: 
        return res


# 4 2 1 0 3 6 5 7
# print(preordertraversal(root))

def postordertraversal(node):
    res = []
    if node: 
        res = res + postordertraversal(node.left)
        res = res + postordertraversal(node.right)
        res.append(node.val)
        return res
    else: 
        return res

# 0, 1, 3, 2, 5, 7, 6, 4
print(postordertraversal(root))

# breadth first traversal 

# tree min
# O(log n) time
def treemin(root):
    node = root
    while node.left: 
        node = node.left
    return node.val

# print(treemin(root))
# print(root.val)


# tree max
# O(log n) time
def treemax(root):
    node = root
    while node.right:
        node = node.right
    return node.val

# print(treemax(root))

# search 
# O(log n) time
def treesearch(root, val):
    if root: 
        if root.val == val: 
            return True
        elif root.val > val:
            return treesearch(root.left, val)
        else: 
            return treesearch(root.right, val)
    else: 
        return False

# print(treesearch(root, 9))
# print(treesearch(root, 3))

# insert; assumes that the root is not null
def treeinsert(root, val):
    node = root
    parent = None
    while node:
        parent = node
        if node.val > val:
            node = node.left
            
        else: 
            node = node.right
    if parent.val > val:
        parent.left = Node(val)
    else: 
        parent.right = Node(val)


treeinsert(root, 1.5)
print(inordertraversal(root))


def treesuccessor(root, node):
    




# deletion 

def treedelete(root, node)
