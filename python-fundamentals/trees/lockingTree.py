from collections import defaultdict

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = defaultdict(set)
        self.locked = defaultdict()             # 2 values: False (not locked); an id (locked)
        self.instantiate()

    def instantiate(self):
        for i in range(len(self.parent)):
            self.children[self.parent[i]].add(i)
            self.locked[i] = False

    def lock(self, num: int, user: int):
        if self.locked[num] == False:  
            self.locked[num] = user        
            return True
        else: 
            return False

    def unlock(self, num: int, user: int):
        if self.locked[num] == user: 
            self.locked[num] = False
            return True
        else: 
            return False

    def upgrade(self, num: int, user: int):
        if self.locked[num] == False and self.dfsParent(num): 
            self.lock(num, user)
            check = [False]
            for child in self.children[num]:
                self.dfsChild(child, check)
            return True
        else:
            return False

    def dfsParent(self, num): # traverse all its parents 
        # if parent(num) == -1: return True
        if num == -1: 
            return True
        # if nums parent is unlocked, dfs
        elif self.locked[num] == False: 
            return self.dfsParent(self.parent[num])
        # else: return false
        else: return False

    def dfsChild(self, num, check):
        if self.locked[num]==True: 
            check[0] = True 
            self.locked[num]==False
        for child in self.children[num]:
            self.dfsChild(child, check)