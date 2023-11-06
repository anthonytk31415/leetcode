## tree deletion


class Tree:
    def __init__(self, root):
        self.root = root


class Node: 
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def inorderTraversal(self, root):
        res = []
        if not root: 
            return res
        else: 
            res = res + self.inorderTraversal(root.left)
            res.append(root.val)
            return res + self.inorderTraversal(root.right)

    # return the node with the min
    def minimum(self, root): 
        if root.left: 
            return self.minimum(root.left)
        else: 
            return root

    def insertion(self, root, val):
        if root.val > val: 
            if not root.left: 
                root.left = Node(val)
            else: 
                return self.insertion(root.left, val)
        else: 
            if not root.right: 
                root.right = Node(val)
            else: 
                return self.insertion(root.right, val)
    

    # def deleteNode(self, root, val): 
    #     # first, traverse to the node that requires deletion
    #     if not root: 
    #         return root 
    #     if val < root.val: 
    #         root.left = self.deleteNode(root.left, val)
    #     elif val > root.val: 
    #         root.right = self.deleteNode(root.right, val)
    #     else:                       # the root is where deletion happens
    #         if not root.left:            
    #             temp = root.right
    #             root = None
    #             return temp
    #         elif not root.right: 
    #             temp = root.left
    #             root = None
    #             return temp
    #         # this is now a node with two smallest children 
    #         temp = self.minimum(root.right)
    #         root.val = temp.val
    #         root.right = self.deleteNode(root.right, temp.val)
    #     return root



    def deleteNode(self, root, key):
        parent = None
        cur = root
        while cur and cur.val != key: 
            parent = cur
            if key < cur.val: 
                cur = cur.left
            else: 
                cur = cur.right
        if not cur: 
            return root
        # Case 1 - node to be deleted has no children, i.e. leaf
        if not cur.left and not cur.right: 
            if cur != root: 
                if parent.left == cur: 
                    parent.left = None
                else: 
                    parent.right = None
            else: 
                root = None
        # Case 2: node to be deleted has 2 children
        elif cur.left and cur.right: 
            sucessor = self.minimum(cur.right)          # find sucessor 
            val = sucessor.val 
            self.deleteNode(root, sucessor.val)         # recursively delete successor node
            cur.val = val
        # Case 3: node to be deleted has one child
        else: 
            if cur.left: 
                child = cur.left
            else: 
                child = cur.right
            if cur != root: 
                if cur == parent.left: 
                    parent.left = child
                else: 
                    parent.right = child
            else:                                       # if node to be deleted is a root node then set root to child
                root = child
        return root




root = Node(10)
# root.left = Node(7)
# root.left.left = Node(3)
# root.left.right = Node(8)
# root.right = Node(13)
# root.right.left = Node(11)
# root.right.right = Node(15)

root.insertion(root, 7)
root.insertion(root, 3)
root.insertion(root, 8)

root.insertion(root, 13)
root.insertion(root, 9)
root.insertion(root, 12)
root.insertion(root, 20)
root.insertion(root, 22)
root.insertion(root, 14)
root.insertion(root, 11)
root.insertion(root, 15)
print(root.inorderTraversal(root))
print(root.minimum(root.right))


# print(root.right.left.left.val)

print(root.right.val)

root.deleteNode(root, 13)
print(root.right.val)