from collections import deque
# Time: O(n)
# Space: O(1)

def connect(root):
    if not root: 
        return root
    queue = deque()
    queue.appendleft(root)
    while queue: 
        prior = None
        for _ in range(len(queue)):
            cur = queue.popleft()
            if prior: 
                prior.next = cur
                
            for child in [cur.left, cur.right]: 
                if child: 
                    queue.append(child)
            prior = cur
        cur.next = None
