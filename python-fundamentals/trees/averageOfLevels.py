from collections import deque

# Time: O(n)
# Space: O(n/2) for max space of the values of each level

def averageOfLevels(root):
    res = []
    q = deque()
    q.append(root)
    while q: 
        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val) 
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)

        res.append(sum(level)/len(level))
    return res