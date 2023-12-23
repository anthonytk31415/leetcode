class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtreeWithAllDeepest(root):
    deepestNodes = [0,0]        # depth, count of nodes

    def dfs(node, depth):
        if not node: return 
        if not node.left and not node.right:
            if depth > deepestNodes[0]: 
                deepestNodes[0] = depth
                deepestNodes[1] = 1
            elif depth == deepestNodes[0]:
                deepestNodes[1] += 1
        else: 
            for child in [node.left, node.right]:
                dfs(child, depth + 1)

    dfs(root, 0)
    deepestParent = [root, 0]       # node, depth
    
    def dfs1(node, depth):
        if not node: return 0
        countDeepestChildren = 0
        if not node.left and not node.right and depth == deepestNodes[0]:
            countDeepestChildren += 1
        else: 
            for child in [node.left, node.right]:
                countDeepestChildren += dfs1(child, depth + 1)
        if countDeepestChildren == deepestNodes[1] and depth > deepestParent[1]:
            deepestParent[0] = node
            deepestParent[1] = depth
        return countDeepestChildren

    dfs1(root,0)
    return deepestParent[0]



root = TreeNode(0)
root.left = TreeNode(1)


print(subtreeWithAllDeepest(root))