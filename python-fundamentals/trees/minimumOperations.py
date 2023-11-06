
# first create an array of array of each level 
# then for each "level", make a copy, sort the copied array
# then start a counter at 0; if 

# at each level, create a dictionary with key:value ==> val, position; 
# if position = actual --> do nothing


# Time: O(NlogN) - we are sorting at each level 
# Space: O(N) - storing the position of the sorted items

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def bfs(root):
    res = []

    q = deque()
    if root: 
        q.append(root)
    while q: 
        cur = []
        for _ in range(len(q)):         # do this iteration for each "level"; each level is the length of the queue starting with the first
            node = q.popleft()
            cur.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right: 
                q.append(node.right)
        res.append(cur)
    return res




def minimumOperations(root):
    counter = 0
    if not root: 
        return counter  

    levels = bfs(root)
    for level in levels: 
        sort_level = sorted(level)
        if level == sort_level:
            continue
        else:
            pos = {}
            for i in range(len(level)):
                pos[level[i]] = i                   # key = val : value = position
            i = 0
            while i < len(level):
                if level[i] != sort_level[i]:       # swap is required! we start at i = 0 and increment up; once a bottom element is swapped, no need to go back
                    counter +=1
                    j = pos[sort_level[i]]          # j is where the current ith value is currently; we'll put the old ith value there
                    a, b = level[i], sort_level[i]  
                    level[i], level[j] = b, a       # swap where the values should be 
                    pos[a], pos[b] = j, i           # update the pos hash table
                i+=1

    return counter 

## some test cases

# root = TreeNode(1)
# root.left = TreeNode(4)
# root.right = TreeNode(3)
# root.left.left = TreeNode(7)
# root.left.right = TreeNode(6)

# root.right.left = TreeNode(8)
# root.right.right = TreeNode(5)

# root.right.left.left = TreeNode(9)
# root.right.right.left = TreeNode(10)

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)

root.right.left = TreeNode(5)
root.right.right = TreeNode(4)


print(minimumOperations(root))