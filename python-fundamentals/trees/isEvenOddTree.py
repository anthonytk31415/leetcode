# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 12:28 - 1247!
# Time: O(N)
# Space: O(logN) check max logN nodes at each step


# 

from collections import deque

## takes an array, returns for even indexed levels, if each element is odd and strictly increasing
def even_cond(arr):
    if not arr:
        return True 
    prev = arr[0]
    if prev % 2 != 1: 
        return False
    for i in range(1, len(arr)):
        if arr[i] % 2 !=1:
            return False
        if arr[i] <= prev: 
            return False
        prev = arr[i]
    return True

# even integer values in strictly decreasing order (from left to right).
def odd_cond(arr):
    if not arr:
        return True 
    prev = arr[0]
    if prev % 2 != 0: 
        return False
    for i in range(1, len(arr)):
        if arr[i] % 2 !=0:
            return False
        if arr[i] >= prev: 
            return False
        prev = arr[i]
    return True

def isEvenOddTree(root):
    if not root: 
        return True
    level = 0
    q = deque()
    q.append(root)

    while q:
        check = [] 
        for _ in range(len(q)):
            cur = q.popleft()
            check.append(cur.val)
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        if level %2 == 0 and not even_cond(check):
            return False
        elif level % 2 == 1 and not odd_cond(check):
            return False

        level +=1

    return True