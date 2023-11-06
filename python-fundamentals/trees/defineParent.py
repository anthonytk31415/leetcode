## my brute force method doesn't work fast enough

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node(TreeNode):
    def __init__(self, val=0, left=None, right=None, p=None):
        super().__init__(val, left, right)
        self.p = p

    #turns a TreeNode and it's nodes into Nodes with parent pointers
    @staticmethod
    def defineParent(root, parent = None):
        if root: 
            node = Node(root.val)
            node.left = Node.defineParent(root.left)
            node.right = Node.defineParent(root.right)
            if node.left: 
                node.left.p = node
            if node.right: 
                node.right.p = node
            return node
        else: 
            return None

class Solution:
    def maxPathSum(self, root):
        def dfs(root):

            node = root
            currentSum = 0
            visited = {}
            for x in allNodes: 
                visited[x] = False
            values = []               ## initialize with the 'zero' path
            stack = [(node, currentSum)]        ## load with the first node if node is not null
            visited[node] = True
            while stack: 
                # print([x[0].val for x in stack])
                node, currentSum = stack.pop()
                # print(currentSum)
                values.append(currentSum + node.val)
                for x in [node.p, node.left, node.right]:
                    if (x) and visited[x] == False: 
                        stack.append((x, currentSum + node.val))
                        visited[x] = True
            return max(values)

        def traversal(root):
.            if root: 
            res = []
                res.append(root)
                res = res + traversal(root.left)
                return res + traversal(root.right)
            else: 
                return res

        ## begin function
        updatedRoot = Node.defineParent(root)
        allNodes = traversal(updatedRoot)
        maxFromDFS = []
        for x in allNodes:
            if x:
                y = dfs(x)
                maxFromDFS.append(y)
        return max(maxFromDFS)
        # x = allNodes[0]
        # return dfs(x)




root = TreeNode(-4)
# root.left = TreeNode(3)
# root.right = TreeNode(8)
# root.right.right = TreeNode(10)

node = Node.defineParent(root)

# print(node.left.p.val)
# print(node.right.p.val)
# print(node.right.right.p.val)
# parent = Node(10)
# leftNode = Node(5)
# leftNode.p = parent
# parent.left = leftNode

# print(parent.val)
# print(parent.left.val)
# print(leftNode.p.val)

z = Solution.maxPathSum('a', root)
# print([zz.p.val for zz in z if zz if zz.p])

print(z)