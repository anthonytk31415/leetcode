## terminal state: 
# have a counter that's 2^0, 2^1, 2^2, ... 2^h for current height
# build a current level array as you iterate per the each height
# 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def isCompleteTree1(root):
    if not root: 
        return True

    height = 0
    queue = deque()
    queue.append(root)
    while queue:
        counter = 2**height
        e = 0 
        children = []
        cur_row = []
        count_nulls = 0
        count_nonNulls = 0
        count_childNonNulls = 0
        while queue and e < counter: 
            cur = queue.popleft()
            e +=1
            if cur: 
                if count_nulls >0: 
                    return False
                count_nonNulls +=1
                children.append(cur.left)
                if cur.left: 
                    count_childNonNulls +=1
                children.append(cur.right)
                if cur.right:
                    count_childNonNulls +=1
            else: 
                count_nulls +=1

        if count_nonNulls < counter and count_childNonNulls > 0: 
            return False

        if count_nonNulls == counter and count_childNonNulls > 0:
            height +=1
            for x in children: 
                queue.append(x)
        else: 
            # print('children: ', children)
            break

    if count_childNonNulls == 0: 
        # print('this')
        return True
    return False



def isCompleteTree(root):
    if not root:
        return True
    q = deque([(root, 1)])
    res = []
    while q: 
        cur, coord = q.popleft()
        res.append(coord)
        if cur.left: 
            q.append((cur.left, coord*2 ))
        if cur.right: 
            q.append((cur.right, coord*2 + 1))
    return len(res) == res[-1]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

print(isCompleteTree(root))