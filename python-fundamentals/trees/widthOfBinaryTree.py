# Definition for a binary tree node.

## acceptable but fucking ugly bfs

## the trick is to use indeces. if you had a complete tree, 
## then each node ordered by breadth is: left child = 2*p, right child = 2*p + 1
## for p = parent index
## if you have nulls, your complete tree order is still maintained; 
## your depth is simply the last index - first index + 1
## keep track of the max; keep popping the queue until it's empty

# Time: O(n) for each node
# Space: O(d) for the max width of the tree for the queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def widthOfBinaryTree(root):
    if not root: 
        return 0
    queue = deque([[root, 1]])
    max_depth = 0
    while queue: 
        cur_depth = 0
        first, last = None, None
        cur_len_queue = len(queue)
        for i in range(len(queue)):
            cur, pos = queue.popleft()
            if i == 0: 
                first = pos
            if i == cur_len_queue - 1:
                last = pos
            if cur.left: queue.append([cur.left, pos*2])
            if cur.right: queue.append([cur.right, pos*2 + 1])
        cur_depth = last - first + 1
        max_depth = max(max_depth, cur_depth)
    return max_depth



# def widthOfBinaryTree(node):
#     if not node: 
#         return 0

#     queue = deque([node])
#     max_depth = 0
#     while queue:
#         count_nonNulls = 0
#         chain_nulls = 0         # used for cur_depth
#         cur_depth = 0
#         child_chain_nulls = 0
        
#         for i in range(len(queue)):
#             cur = queue.popleft()
#             # print(cur)
#             if isinstance(cur, TreeNode):
#                 if count_nonNulls > 0:
#                     cur_depth += chain_nulls
#                     chain_nulls = 0
                
#                 count_nonNulls +=1
#                 cur_depth +=1 
#                 for child in [cur.left, cur.right]:
#                     if child != None: 
#                         if child_chain_nulls > 0: 
#                             print('appending child chains: ', child_chain_nulls)
#                             queue.append(child_chain_nulls)
#                             child_chain_nulls = 0
#                         queue.append(child)
#                     elif child == None: 
#                         print('child chain nodes before adding', child_chain_nulls)
#                         child_chain_nulls +=1

#             elif isinstance(cur, int) and count_nonNulls > 0:
#                 print('nonnode: ', cur)
#                 chain_nulls += cur 
#                 child_chain_nulls += cur * 2

#         max_depth = max(max_depth, cur_depth)
#         print(max_depth, queue)
#         if count_nonNulls == 0:
#             break
#     return max_depth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

print(widthOfBinaryTree(root))

########################################################################################
# Too Slow below
########################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root: 
#             return 0

#         queue = deque([root])
#         max_depth = 0
#         while queue:
#             count_nonNulls = 0
#             cur_depth = deque()
#             for _ in range(len(queue)):
#                 cur = queue.popleft()
#                 if cur != None:
#                     count_nonNulls +=1
#                     queue.append(cur.left)
#                     queue.append(cur.right)
#                     cur_depth.append(cur.val)
#                 else: 
#                     cur_depth.append(None)
#                     queue.append(None)
#                     queue.append(None)
#             # calculate height of current depth; find the left side; then find the right side
#             while cur_depth:            # remove until you find a node from the left
#                 if cur_depth[0] == None:
#                     cur_depth.popleft()
#                 else: break
#             while cur_depth: 
#                 if cur_depth[-1] == None: 
#                     cur_depth.pop()
#                 else: break 

#             max_depth = max(max_depth, len(cur_depth))
#             if count_nonNulls == 0:
#                 break
#         return max_depth