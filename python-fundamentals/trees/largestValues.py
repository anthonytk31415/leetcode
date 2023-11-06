from collections import deque
from math import inf 

# time: O(n)
# space: O(1) extra space; O(n) for the array you're returning 

def largestValues(root):
    res = []
    if not root: 
        return res
    queue = deque()
    queue.append(root)
    while queue:
        cur_largest = -inf 
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur.val > cur_largest: cur_largest = cur.val
            for child in [cur.left, cur.right]:
                if child: queue.append(child)
        res.append(cur_largest)
    return res