# kthSmallest
# do minimum root, then delete that root. Do that k - 1 times. then 
# find the minimum root. 



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traversal(root):
    res = []
    if root: 
        res = res + traversal(root.left)
        res.append(root.val)
        return res + traversal(root.right)
    else: 
        return res

def sortedArrayToBST(nums):
    if len(nums) == 0: 
        return None
    if len(nums) == 1: 
        return TreeNode(nums[0])
    q = len(nums)//2
    root = TreeNode(nums[q])
    root.left = sortedArrayToBST(nums[:q])
    root.right = sortedArrayToBST(nums[q+1:])
    return root


z = [0,1,2,3,4,5,6,7,]



root = sortedArrayToBST(z)
# print(traversal(root))

def minimum(root):
    parent = None
    node = root
    while node: 
        parent = node
        node = node.left
    return parent

def parent(root, node):
    parent = None
    curNode = root
    while curNode != node: 
        parent = curNode
        if node.val < curNode.val:   
            curNode = curNode.left
        else: 
            curNode = curNode.right
    return parent

single = TreeNode(1)
print(parent(single, single))

# minNode = minimum(root)
# parentMinNode = parent(root, minNode)

# def searchNode(root, node):
#     curNode = root
#     while curNode != node: 
#         if node.val < curNode.val:   
#             curNode = curNode.left
#         else: 
#             curNode = curNode.right
#     return curNode

def deletion(root, node):
    parentNode = parent(root, node)
    # left is null
    if node.left == None: 
        print('this')
        newNode = node.right
    elif node.right == None: 
        newNode = node.left
    ## find the min on the right
    ## has children; does not have children
    else: 
        minRight = minimum(node.right)
        if minRight != node.right: 
            parent(minRight).left = None
            newNode = minRight
            newNode.right = node.right
        else: 
            newNode = node.right
        newNode.left = node.left
    # parent > node --> attach to left; else attach to parent right
    if parentNode == None: 
        root = newNode        
    else: 
        if parentNode.val > node.val:
            parentNode.left = newNode
        else:
            parentNode.right = newNode
    return root


# deletion(root, minimum(root))
# # print(minimum(root).val)
# deletion(root, minimum(root))
# # print(minimum(root).val)
# deletion(root, minimum(root))
# deletion(root, minimum(root))



def kthSmallest(root, k):
    for _ in range(k-1):
        root = deletion(root, minimum(root))
    return minimum(root).val


# print(kthSmallest(root,8))
# print(traversal(root))
# print(root.val)

# logic for stack: 
# 

# exact logic for stack: 
# loop: 
# if current: 
#     - stack current
#     - go left
# elif stack:
#     - current = pop stack 
#     - print current
#     - go right
# else: 
#     stop
# return res

#time: O(logn + k)

def inorder(root):
    current = root
    stack = []
    res = []
    while True:
        if current != None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            res.append(current.val)
            current = current.right
        else:
            break
    return res 


#using a stack: do the stack method until the length of result is = k 

def inorderK(root, k):
    current = root
    stack = []
    res = []
    while True and len(res) < k:
        if current != None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            res.append(current.val)
            current = current.right
        else:
            break
    return res[len(res) - 1]


trav = inorderK(root, 7)
print(trav)