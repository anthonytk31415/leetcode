from math import inf 

# one pass DFS Time O(n), O(1) space


def lcaDeepestLeaves(root):
    def dfs(node, depth):
        deepestNode = node
        numChildren = 0
        depthChildren = -inf 
        if not node.left and not node.right: 
            return node, 1, depth 

        if node.left: leftDeepestNode, leftNumChildren, leftChildDepth = dfs(node.left, depth + 1)
        if node.right: rightDeepestNode, rightNumChildren, rightChildDepth = dfs(node.right, depth + 1)
        if node.left and node.right and leftChildDepth == rightChildDepth: 
            deepestNode = node
            numChildren = leftNumChildren + rightNumChildren
            depthChildren = leftChildDepth

        if (node.left and node.right and leftChildDepth > rightChildDepth) or (node.left and not node.right):
            numChildren = leftNumChildren
            depthChildren = leftChildDepth
            deepestNode = leftDeepestNode
        
        elif (node.left and node.right and leftChildDepth < rightChildDepth) or (not node.left and node.right):
            numChildren = rightNumChildren
            depthChildren = rightChildDepth
            deepestNode = rightDeepestNode
        return deepestNode, numChildren, depthChildren
    
    return dfs(root, 0)[0]