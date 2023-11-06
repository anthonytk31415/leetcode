class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum1(root):
    
    def helper(root):
        if not root: 
            return [None, None]
        else: 
            left = helper(root.left)
            right = helper(root.right)

            res0, res1 = [root.val], [0]

            if left[0] != None: res0.append(left[0])            # left fork
            if right[0] != None: res0.append(right[0])          # right fork
            
            if left[1] != None: 
                res0.append(root.val + left[1])                 # fork root plus left single
                res1.append(left[1])                            # left single
            if right[1] != None: 
                res0.append(root.val + right[1])
                res1.append(right[1])          # right single

            
            if left[1] != None and right[1] != None:             
                res0.append(root.val + left[1] + right[1])      # fork: root + left_single + right_single

            res = [None, None]
            res[0] = max(res0)

            res[1] = root.val + max(res1)

            # [greatest fork; greatest leg]
            # return [max(root.val + left[1] + right[1], left[0], right[0], root.val), 
            #         max(root.val + max(left[1], right[1], 0)]
            print(root.val, res)
            return res

    return max(helper(root))


from math import inf

def maxPathSum(root):
    
    def helper(root):
        if not root:
            return [-inf, -inf]
        left = helper(root.left)
        right = helper(root.right)
        
        # max fork, max leg
        res = [max(root.val + left[1] + right[1], left[0], right[0], left[1], right[1]), 
                root.val + max(left[1], right[1], 0)] 

        # print(root.val, res)
        return res
    return max(helper(root))



# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# root = TreeNode(2)
# root.left = TreeNode(-1)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.left.left = TreeNode(5)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = TreeNode(-6)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
# root.left.left.left = TreeNode(4)
# root.left.left.left.left = TreeNode(5)


# [-6,null,3,2]


print(maxPathSum(root))

# [2,-1]
# [1,2,null,3,null,4,null,5]