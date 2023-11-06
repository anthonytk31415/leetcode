# traverse all the nodes 
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def traverse(root, parent, lookup):
    if not root: 
        return 
    all_desc = []
    for desc in [parent, root.left, root.right]:
        if desc:
            all_desc.append(desc.val)
    lookup[root.val] = all_desc
    for child in [root.left, root.right]:
        if child: 
            traverse(child, root, lookup)
        

def distanceK(root, target, k):    
    def traverse(root, parent, lookup):
            if not root: 
                return 
            all_desc = []
            for desc in [parent, root.left, root.right]:
                if desc:
                    all_desc.append(desc.val)
            lookup[root.val] = all_desc
            for child in [root.left, root.right]:
                if child: 
                    traverse(child, root, lookup)

    lookup = {}
    traverse(root, None, lookup)
    print(lookup)

    start = None
    for x in lookup:
        if x == target: 
            start = x
            break

    # print(start.val)

    queue = deque()
    queue.append(start)
    visited = set()
    for _ in range(k):
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur not in visited: 
                visited.add(cur)
                if cur in lookup:
                    for x in lookup[cur]:
                        queue.append(x)
    
    res = []
    for x in queue:
        if x not in visited:
            res.append(x)
    return res                
         


# root = TreeNode(1)

# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)

# root.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)


root = TreeNode(3)

root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)


print(distanceK(root, 5, 2))

