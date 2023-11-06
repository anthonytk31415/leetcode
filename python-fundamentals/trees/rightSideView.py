# rightSideView
# https://leetcode.com/problems/binary-tree-right-side-view/solutions/?envType=study-plan&id=level-2&orderBy=most_votes

# time: start 11:15; 11:42 end - 27 min
# a number of errors

# you're looking at the last node on each rank in breadth first search
# biuld a stack
# keep distance variable and previous distance
# if current dist > previous distance: update distance, append val into result

# dont forget that at the end, the last "end" won't trigger the cur dist > prev dist logic so append that last val to result
# time: O(N) since you're traversing all the nodes to find the last one 
# space: O(N) to track distance of each node (i.e. height) ; can be O(1) as we only track one distance and the last node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

def rightSideView(root):
    res = []
    dist = defaultdict()
    if not root: 
        return res
    q = deque()
    q.append(root)
    dist[root] = 0
    prevDist = 0
    prevVal = None
    while q: 
        cur = q.popleft()
        if dist[cur] > prevDist:
            res.append(prevVal)
        prevDist = dist[cur]
        prevVal = cur.val
        for child in [cur.left, cur.right]:
            if child: 
                dist[child] = dist[cur] + 1
                q.append(child)

    res.append(prevVal)
    return res   
        


# def rightSideView(root):
#     def helper(root):
#         res = []
#         if root: 
#             res.append(root.val)
#             return res + helper(root.right)
#         else: 
#             return res
#     return helper(root)



## there's a trick to more conveniently store height: 
## in BFS for a tree, you can initiate the queue and then only go through the queue the length of the queue times and then stop
## then refresh the queue once all the queued items are processed and their children are queued up to progress to the next level
## then at the end of the queued cycle, append the last val
## 
class Solution(object):
    def rightSideView(self, root):
        deque = deque()
        if root:
            deque.append(root)
        res = []
        while deque:
            size, val = len(deque), 0
            for _ in range(size):
                node = deque.popleft()
                val = node.val # store last value in each level
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(val)
        return res


## rewrite this: 