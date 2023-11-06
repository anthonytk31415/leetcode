# Time: O(n)
# Space: O(1)

# the trick is to keep track of your previous direction
# reset your counter every time you go the same direction as your prev direction 
# increment counter when you alternate 
# keep a global variable and update your max every iteration of the function

def longestZigZag(root):

    curMax = [0]    
    def helper(root, prevDir, cur):          # prevDir can be None, left, right
        curMax[0] = max(cur, curMax[0])
        if not root: 
            return
        if prevDir == None: 
            if root.left: helper(root.left, 'left', 1)
            if root.right: helper(root.right, 'right', 1)
        elif prevDir == 'left': 
            if root.left: helper(root.left, 'left', 1)
            if root.right: helper(root.right, 'right', cur + 1)
            
        elif prevDir == 'right': 
            if root.left: helper(root.left, 'left', cur + 1)
            if root.right: helper(root.right, 'right', 1)
        
    helper(root, None, 0)
    return curMax[0]