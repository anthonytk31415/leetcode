# Nodes and Trees

# node values are distinct

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    
class Tree:
    def insert(self, root, node):
        if node.value < root.value:
            if root.left== None:
                root.left = node
            else:
                self.insert(root.left, node) 
        else: 
            if root.right == None:
                root.right = node
            else: 
                self.insert(root.right, node) 

    def preorder_traversal(self, root):
        res = []
        if (root):
            res.append(root.value)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res
    
    def inorder_traversal(self, root):
        res = []
        if (root):
            res = res + self.inorder_traversal(root.left)
            res.append(root.value)
            res = res + self.inorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        res = []
        if (root):
            res = res + self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.value)
        return res



tree = Tree()
# root = Node(4)
# tree.insert(root, Node(1))
# tree.insert(root, Node(2))
# tree.insert(root, Node(3))
# tree.insert(root, Node(9))
# tree.insert(root, Node(8))
# tree.insert(root, Node(12))
# tree.insert(root, Node(5))
# tree.insert(root, Node(7))

root = Node(27)
tree.insert(root, Node(14))
tree.insert(root, Node(35))
tree.insert(root, Node(10))
tree.insert(root, Node(19))
tree.insert(root, Node(31))
tree.insert(root, Node(42))



# print(root.left.value)
# print(root.left.right.value)
# print(root.left.right.right.value)


print(tree.preorder_traversal(root))
print(tree.inorder_traversal(root))
print(tree.postorder_traversal(root))