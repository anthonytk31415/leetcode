# Trees 
# node - a thing in the tree 
# root - top node of a tree; only one in a tree
# parent - nodes with child nodes
# child nodes - node that belongs to another node (a parent)
# leaf nodes - nodes with no children
# siblings - shares the same parent
# subtree - each node is a subtree and a tree is a recursive object










# traversing trees: 
# Breadth first: start at each level (think horizontal orientation)
# depth first: go deep in a tree; 

# Generic (N-ary) Tree
# operations: (1) insert child of, (2) remove, (3) has? (4) get subtree for

# binary tree (2-ary)
# 2 children per parent
# key property: left chiild < parent; right child < parent
# depth: log n (for n element tree)
# operations: (1) add, (2) has, (3) remove

# remove (2 child): go to the right of the deleted node, go all the way down on the 
# left path (to take the min of the elements just largeer than that deleted
#  node and then swap

# remove (1 child): go to the deleted node; that child of deleted node is now the new "parent"
# and is attached to the parent of the formerly deleted node

# remove (0 child): just remove; order is OK

# adding: recursively put it in the root where if adding > root --> right, else left; if there's a slot,
# put it there, else, call the add function again on the node where it belongs (L or R)



# Make the binary tree class

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val < val:  #traverse right:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)
        elif self.val > val: #traverse left
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            self.val = val

    # print the tree inorder traversal
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.val)
        if self.right:
            self.right.printTree()

    # Preorder traversal
    # Root -> Left -> Right
    def preorderTraversal(self):
        print(self.val)
        if self.left:
            self.left.preorderTraversal()
        if self.right:
            self.right.preorderTraversal()


    # postorder traversal
    # Root -> Left -> Right
    def postorderTraversal(self):
        if self.left:
            self.left.postorderTraversal()
        if self.right:
            self.right.postorderTraversal()
        print(self.val)


    #return the minimum given the node; the value or the node? in this case, it's built as the value
    def minimum(self):
        if self.left:
            return self.left.minimum()
        else: 
            return self.val

    def maximum(self):
        if self.right:
            return self.right.maximum()
        else:
            return self.val

    


### need to do breadth  first traversal 


## pretty print printing
def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)

root = Node(20)
root.insert(10)
root.insert(15)
root.insert(25)
root.insert(30)
root.insert(22)
root.insert(2)
# root.printTree()

print(root.postorderTraversal())

print_tree(root)
y = root.minimum()
print(y)
print(root.maximum())


