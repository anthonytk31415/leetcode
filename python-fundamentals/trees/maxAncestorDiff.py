def maxAncestorDiff(root):

    def dfs(node):
        nMin, nMax = node.val, node.val
        v = -1
        for child in [node.left, node.right]:
            if child: 
                cMin, cMax, cV= dfs(child)
                nMin = min(nMin, cMin)
                nMax = max(nMax, cMax)
                v = max(v, cV, abs(node.val - cMin), abs(node.val - cMax))
        return nMin, nMax, v
    return dfs(root)[2]