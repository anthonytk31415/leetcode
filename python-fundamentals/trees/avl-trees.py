# AVL Trees



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:

    def insert(self, root, key):
        # 1) perform normal insertion
        if not root:
            return TreeNode(key)
        elif key < root.val: 
            root.left = self.insert(root.left, key)
        else: 
            root.right = self.insert(root.right, key)
        
        # 2) update the height of ancestor
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right))
        # 3) get the balanace factor
        balance = self.getBalance(root)

        # 4) if unbalanced: try the four cases LL, LR, RR, RL


        return root

    def leftRotate(self, root):
        return 
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        #perform rotation
        y.right = z
        z.left = T3
        #update heights
        


    def getHeight(self, root):      # note that when we do insertion and possibly deletion 
        if not root:                # we then update heights of the nodes
            return 0
        return root.height

    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if not root: 
            return []
        else: 
            res = []
            res.append(root.val)
            res = res +self.preOrder(root.left)
            return res + self.preOrder(root.right)