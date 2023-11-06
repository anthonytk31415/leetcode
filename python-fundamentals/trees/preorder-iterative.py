from collections import deque
def preorder(root):
    stack = deque()
    res = []
    if not root:
        return res
    stack.append(root)
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right: stack.append(cur.right)
        if cur.left: stack.append(cur.left)
    return res

def inorder(root):
    stack = deque()
    res = []
    if not root:
        return res
    cur = root
    while cur != None or stack: 
        ## go left
        if cur != None:
            stack.append(cur)
            cur = cur.left
        ## can't go left, so 
        else: 
            curRoot = stack.pop()
            res.append(curRoot.val)
            cur = curRoot.right
    return res



## smae as preorder but left right reversed and then reverse the result
def postorder(root):
    stack = deque()
    res = []
    if not root:
        return res
    stack.append(root)
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.left: stack.append(cur.left)
        if cur.right: stack.append(cur.right)
    return res[::-1]
    