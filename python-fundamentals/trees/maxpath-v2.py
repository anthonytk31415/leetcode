class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) time, 
# O(1) complexity? 

# The answer will require either a chain of left + right or a segment picked up from below the root
# so we'll gather those segments and compare using recursion from the root and build the comparison 
# as we traverse to the leaves


# return (1) and (2) 
# (1) chain of node (this can continue to build with parent values); max of:
# - root.val
# - root.val + chain of root.left
# - root.val + chain of root.right

# (2) broken nonchain of node (i.e. previous maxes that are carried up to the root but cannot be chained): 
# - broken nonchain of left
# - broken nonchain of right
# - root.val + chain of root.left + chain of root.right
# - chain left
# - chain right

# To Summarize: each node will have 2 values: 
# - (1) max chain = max (root.val, val + chain of left, val + chain of right)
# - (2) max broken = max(broken left, broken right, root.val + chain of left + chain of right, chainleft, chainright)

# a cleaner solution
# https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/39919/8-10-lines-two-solutions/?orderBy=most_votes

# try rewriting this: 
# a key note: 
# if the node is null, then it doesn't contribute anything to the sum; you can code it as -inf as you take max of other elements
# if it's negative, that negative could be a max, but you'll never want to sum it

# in that case, as you carry the values upward, you can define:
# (1) max chain = root.val + max(chain of left, chain of right, 0) // 0 to accomodate for negative chains prior
# (2) max brokens: max of [left chain, left broken] + [right chain, right broken] + [val + left chain + right chain]


def helper(node):
# result: res[0] = max chain; res[1] = max broken
    chain = [node.val]
    broken = []
    ## fill max broken + chain
    resLeft, resRight = None, None
    if node.left: 
        resLeft = helper(node.left)
        chain.append(resLeft[0] + node.val)
        broken.append(resLeft[0])
        if resLeft[1]: 
            broken.append(resLeft[1])
    if node.right: 
        resRight = helper(node.right)               
        chain.append(resRight[0] + node.val)                # val + chain of right
        broken.append(resRight[0])                          # chain right
        if resRight[1]: 
            broken.append(resRight[1])                      # broken right
    if resLeft and resRight:                        
        broken.append(node.val + resLeft[0] + resRight[0])  # chain left + val + chain right

    if broken:
        broken = max(broken)
    else: 
        broken = None
    chain = max(chain)
    return (chain, broken)


def maxPath(root):
    res = helper(root)
    if res[1]:
        return max(res[0], res[1])
    else: return res[0]

# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = TreeNode(-20)
root.left = TreeNode(5)
root.right = TreeNode(25)
root.right.right = TreeNode(-30)
root.left.left = TreeNode(3)
root.left.right = TreeNode(-10)


z = maxPath(root)
print(z)



