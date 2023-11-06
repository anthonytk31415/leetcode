
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


## use classic traversal with added conditions
def isSameTree(p, q):
    def traversal(p,q):
        if p==None and q== None:
            return True
        elif p == None or q == None:
            return False
        else: 
            return p.val == q.val and traversal(p.left, q.left) and traversal(p.right, q.right) 
    return traversal(p,q)

# simpler:
class Solution:
    def isSameTree(self, p,q) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

p = Node(30)
p.left = Node(10)
# p.left.left = Node(5)
# p.right = Node(50)
# p.right.right = Node(60)

q = Node(30)
# q.left = Node(10)
# q.left.left = Node(5)
q.right = Node(10)
# q.right.right = Node(60)
# q.right.right.right = Node(70)


print(isSameTree(p,q))