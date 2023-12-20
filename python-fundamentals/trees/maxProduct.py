# When you break an edge, you'll have two pieces: 
# (1) the tree that's made with the child, and (2) the rest.
# If you have total sum of entire tree, and total sum of child (for each child), 
# the product after edge break = (sum child) * (sum entire tree - sum child)

# So lets dfs starting at the root. The first time, we just get the Total Sum.
# Next time, we'll do comparisons of removing the edge 

# Time: O(n); Space: O(n) for calculating sums of the children of nodes

from math import inf 


def maxProduct(root):
    nodeSums = {}
    
    def dfsSum(node):
        res = node.val
        for child in [node.left, node.right]: 
            if child: res += dfsSum(child)
        nodeSums[node] = res
        return res

    maxProduct = [-inf]
    def dfsEdge(node):
        for child in [node.left, node.right]: 
            if child: 
                curRes = nodeSums[child] * (nodeSums[root] - nodeSums[child])
                maxProduct[0] = max(maxProduct[0], curRes)        
                dfsEdge(child)
        return 
    dfsSum(root)
    dfsEdge(root)
    return maxProduct[0] % (10 ** 9 + 7)