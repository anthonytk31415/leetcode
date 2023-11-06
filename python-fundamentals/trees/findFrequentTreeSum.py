# Time + Space: O(n) solution
# use a hash map to traverse and keep track of the frequency of sums
# use recursion to capture the current total result and add that to the hash


# can use counter!

from collections import Counter
from math import inf 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findFrequentTreeSum(root):
    counter = Counter()

    def helper(root, counter):
        res = root.val
        if root.left: res += helper(root.left, counter)
        if root.right: res += helper(root.right, counter)
        counter[res] +=1
        return res

    helper(root, counter)
    max_freq = max(counter.values())
    return [x for x in counter if counter[x] == max_freq]

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)

print(findFrequentTreeSum(root))