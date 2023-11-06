# do bfs to traverse
# at each bfs level, evalulate to see if the sum of that level is larger, if so replace

## Complexity
# O(n) for time for the traversal
# O(1) for space to store the level, curmax

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from math import inf 
from collections import deque
def maxLevelSum(root):

    queue = deque()
    queue.append(root)

    level = 1
    curMax = -inf
    curLevel = 0

    while queue: 
        curLevel +=1
        levelSum = 0
        nextQueue = deque()
        for _ in range(len(queue)):
            curNode = queue.popleft()
            levelSum += curNode.val
            if curNode.left: nextQueue.append(curNode.left)
            if curNode.right: nextQueue.append(curNode.right)
        if levelSum > curMax: 
            curMax = levelSum
            level = curLevel
        queue = nextQueue
    
    return level


# Example

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(2)


x = maxLevelSum(root)
print(x)