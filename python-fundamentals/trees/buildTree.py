from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree1(preorder, inorder):
    head = TreeNode(preorder[0])
    
    idxLookup = {}
    for i, num in enumerate(inorder):
        idxLookup[num] = i

    for i, num in enumerate(preorder[1:]):
        node = head
        while True: 
            if idxLookup[num] > idxLookup[node.val]: 
                if node.right: 
                    node = node.right
                else: 
                    node.right = TreeNode(num)
                    break
            else: 
                if node.left:     
                    node = node.left
                else: 
                    node.left = TreeNode(num)
                    break 
    return head

# lets build this recursively
# def buildTree(preorder, inorder):
#     head = preorder[0]

#     preOrderLeft = 
#     preOrderRight = 


#     return head




preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

x = buildTree(preorder, inorder)

def inorderPrint(node):
    res = []
    if not node: 
        return res
    res = res + inorderPrint(node.left)
    res.append(node.val)
    return res + inorderPrint(node.right)

def preorderPrint(node):
    res = []
    queue = deque([node])
    while queue: 
        cur = queue.popleft()
        res.append(cur.val)
        if cur.left: 
            queue.append(cur.left)
        if cur.right: 
            queue.append(cur.right)
    return res

def postorder


print(inorderPrint(x))
print(preorderPrint(x))