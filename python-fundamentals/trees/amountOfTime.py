from math import inf 

# One fell swoop Time = O(N) with single traversal and Space O(1). 
# Be careful and deliberate with the recursion and the base cases. 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def amountOfTime(root, start):

    def dfs(node):
        maxDepth = -1
        distToStart = inf       
        time = inf           
        if not node: return maxDepth, distToStart, time

        mdLeft, dsLeft, timeLeft = dfs(node.left)
        mdRight, dsRight, timeRight = dfs(node.right)

        maxDepth = max(1+mdLeft, 1+mdRight, 0)
        distToStart = min(1+dsLeft, 1+dsRight, distToStart)

        if dsLeft != inf: 
            time = max(mdRight + 1 + 1 + dsLeft, timeLeft)
        else: 
            time = max(mdLeft + 1 + 1 + dsRight, timeRight)

        if node.val == start: 
            distToStart = 0
            time = maxDepth 
        return maxDepth, distToStart, time
    
    res = dfs(root)
    return res[2]



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)

start = 4
print(amountOfTime(root, start))