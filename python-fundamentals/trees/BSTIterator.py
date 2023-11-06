# Binary Search Tree Iterator

# Definition for a binary tree node.
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.root = root
        self.pointer = -inf
        self.sortArr = self.traversal()

    def next(self) -> int:
        # call deletion, then change pointer to val
        if self.pointer == -inf: 
            self.pointer = 0
        ## delete the smallest number, return smallest nuumber
        else: 
            self.pointer +=1
        return self.sortArr[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.sortArr)
        # return if root is not null

    @staticmethod
    # return (root, parent)
    def minimum(root):
        node = root
        parent = None
        while node.left: 
            parent = node
            node = node.left
        return (node, parent)

    @staticmethod
    # return the node in the root of the parent
    def parent(root, nodeCheck):
        node = root
        parent = None
        while node: 
            if node.val == nodeCheck:
                return parent
            else: 
                parent = node
                if nodeCheck < node.val: 
                    node = node.left
                else: 
                    node = node.right
        print('node does not exist')
    
    def traversal(self):
        def helper(root):
            res = []
            if root: 
                res = res + helper(root.left)
                res.append(root.val)
                return res + helper(root.right)
            else: 
                return res
        return helper(self.root)


    @staticmethod
    def deletionMin(root):
        min = BSTIterator.minimum(root)[0]
        parent = BSTIterator.parent(root, min.val)
        if min.left == None: 
            parent.left == None
        else: 
            parent.left = min.right

        return min.val



root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.right = TreeNode(13)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)


# print(BSTIterator.parent(root, 15).val)
# print(BSTIterator.minimum(root)[0].val)

print(BSTIterator.deletionMin(root))
print(BSTIterator.deletionMin(root))


# root_c = BSTIterator(root)
# print(root_c.next())
# print(root_c.next())
# print(root_c.next())
# print(root_c.next())
# print(root_c.next())


# print(BSTIterator.minimum(root).val)