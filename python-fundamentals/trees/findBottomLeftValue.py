from collections import deque

# Time: O(n) --> traverse all the nodes
# space: constant
def findBottomLeftValue(root):
    cur_left = None
    q = deque()
    q.append(root)
    while q: 
        for i in range(len(q)):
            cur = q.popleft()
            if i == 0: 
                cur_left = cur.val
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
    return cur_left