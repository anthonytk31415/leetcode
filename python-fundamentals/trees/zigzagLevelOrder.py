# 222

# Time: O(n)
# Space: O(n) for the tree return value

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def zigzagLevelOrder(root):
    res = []
    q = deque()

    if not root: 
        return []

    q.append(([root], 0))
    while q: 
        cur, check = q.popleft()
        cur_res = [x.val for x in cur]
        cur_next = []
        for x in cur: 
            if x.left: cur_next.append(x.left)
            if x.right: cur_next.append(x.right)
        if check == 1: 
            cur_res = list(reversed(cur_res))
        res.append(cur_res)
                
        if cur_next: 
            q.append((cur_next, 1-check))
    return res


# [0,2,4,1,null,3,-1,5,1,null,6,null,8]

# [1,2,3,4,null,null,5]
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)



print(zigzagLevelOrder(root))
        #     if not root: 
        #     return res
        # else: 
        #     if check == 1: 
                
                
        #         root.left, root.right = root.right, root.left
        #     helper(root.left, 1 - check)
        #     helper(root.right, 1 - check)
        #     return root
