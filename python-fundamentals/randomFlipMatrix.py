from random import randint 

# keep a hash table that maps 

# 
## apparently this takes too much space... it's still O(n)
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.items = []
        self.itemToPos = {}
        self.resetOnce()
        self.removedItems = []

    def flip(self):
        idx = randint(0, len(self.items) - 1 )
        itemToRemove = self.items[idx]
        self.removedItems.append(itemToRemove)
        lastItem = self.items.pop()
        # swap idx with the last element of items to preserve its length; 
        if idx != len(self.items):
            self.items[idx] = lastItem
            self.itemToPos[lastItem] = idx
        del self.itemToPos[itemToRemove]
        return itemToRemove

    def resetOnce(self):
        self.items = []
        self.itemToPos = {}
        idx = 0
        for i in range(self.m):
            for j in range(self.n):
                pair = (i, j)
                self.items.append(pair)
                self.itemToPos[pair] = idx
                idx += 1

    def reset(self):
        idx = len(self.items)
        for x in self.removedItems:
            self.items.append(x)
            self.itemToPos[x] = idx
            idx += 1
        self.removedItems = []
        
# this solution is a bit cleaner

# - We choose a random integer from start = 0 to end = m*n - 1
# - Each removal, we'll increment start += 1. 
# - We keep a hash table of our removals. Since we increment start, we will swap 
#   the random integer we remove with start. So the next time we choose the random
#   integer, since we already removed it, we'll remove that cycle's start.
#   if we choose the random integer multiple times we'll still map it to start, the
#   one that's removed from the random integer call.


# divmod returns a X mod Y as a tuple: (number of times Y goes into X, the remainder of X/Y)

class Solution:

    def __init__(self, n_rows: int, n_cols: int):
        self.c = n_cols
        self.start = 0
        self.end = n_rows * n_cols - 1
        self.removals = {}                                                  # keep track of removals and its mapped value
        
    def flip(self):
        rand = randint(self.start, self.end)
        res = self.removals.get(rand, rand)                                 # return random, or the removal and remapped value
        self.removals[rand] = self.removals.get(self.start, self.start)     # bind removals to start if it was removed; or to start itself
        self.start += 1
        return divmod(res, self.c)
    
    def reset(self):
        self.removals= {}
        self.start = 0


x = Solution(4,1)
print(x.flip())
print(x.flip())
print(x.flip())
print(x.flip())
print(x.reset())
print(x.flip())
print(x.flip())
print(x.flip())
print(x.flip())