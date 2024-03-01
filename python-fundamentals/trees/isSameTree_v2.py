def isSameTree(p, q):
    if not p and not q: return True
    return p != None and q != None and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)