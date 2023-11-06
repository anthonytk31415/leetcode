## binary search tree

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else: 
            parent = None
            node = self.root
            while node: 
                parent = node
                if val < node.val:
                    node = node.left
                else: 
                    node = node.right        
            if val < parent.val:
                parent.left = TreeNode(val)
            else: 
                parent.right = TreeNode(val)
        
    def inOrderTraversal(self):
        def helper(root):
            res = []
            if root: 
                res = res + helper(root.left)
                res.append(root.val)
                return res + helper(root.right)
            else: 
                return res
        return helper(self.root)
    
    def bfs(self):
        res = []
        q = deque()
        q.append(self.root)
        while q: 
            cur = q.popleft()
            if cur: 
                res.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
        return res

    def dfs(self):
        res = []
        def helper(root, res):
            if root: 
                helper(root.left, res)
                helper(root.right, res)
                res.append(root.val)
        helper(self.root, res)
        return res

    def dfs_stack(self):
        res, discovered, processed, stack = [], set(), set(), deque()
        stack.append(self.root)
        while stack: 
            cur = stack.pop()
            if cur: 
                if cur.val not in discovered:
                    discovered.add(cur.val)
                    stack.append(cur)
                    stack.append(cur.right)
                    stack.append(cur.left)
                elif cur.val not in processed:
                    res.append(cur.val)
                    processed.add(cur.val)
        return res

    def preOrderTraversal(self):
        def helper(root):
            res = []
            if root: 
                res.append(root.val)
                res = res + helper(root.left)
                return res + helper(root.right)
            else: 
                return res
        return helper(self.root)

    def postOrderTraversal(self):
        def helper(root):
            res = []
            if root: 
                res = res + helper(root.right)
                res.append(root.val)
                return res + helper(root.left)
            else: 
                return res
        return helper(self.root)

    @staticmethod
    def minTree(root):
        node = root
        while node.left:
            node = node.left
        return node.val


    def search(self, val):
        def helper(root, val):
            if root: 
                if root.val == val:
                    return True
                elif val < root.val:
                    return helper(root.left, val)
                else: 
                    return helper(root.right, val) 
            else: 
                return False    
        return helper(self.root, val)

    @staticmethod
    def height(root):
        if not root: 
            return 0 
        else: 
            return max(BinarySearchTree.height(root.left), BinarySearchTree.height(root.right)) + 1

    @staticmethod
    def isBalanced(root):
        if not root:
            return True
        left_h, right_h = BinarySearchTree.height(root.left), BinarySearchTree.height(root.right)
        return abs(left_h - right_h) <= 1 and BinarySearchTree.isBalanced(root.left) and BinarySearchTree.isBalanced(root.right)

        
    def delete(self, val):
        pass


x = TreeNode(1)
x.left = TreeNode(2)
x.left.left = TreeNode(2)
x.left.left.left = TreeNode(2)
x.right = TreeNode(3)
x.right.right = TreeNode(3)
x.right.right.right = TreeNode(3)

print(BinarySearchTree.isBalanced(x))


root = BinarySearchTree()
root.insert(10)
root.insert(1)
root.insert(11)
root.insert(12)
root.insert(4)
root.insert(3)
root.insert(0)
root.insert(-11)
# # print(root)
# x = root.inOrderTraversal()
# print(x)

# print(root.root.val)

# print(root.search(3))
# print(root.search(12))

# print(root.preOrderTraversal())
# print(root.postOrderTraversal())
# print(root.bfs())
# print(root.dfs())

# print(root.dfs_stack())

# print(BinarySearchTree.minTree(root.root))

# print(BinarySearchTree.height(root.root))

print(BinarySearchTree.isBalanced(root.root))


## need to do: 
# delete 