from random import randInt

class RandomizedSet:

    # next idx to insert; curIdx - 1 is the last idx to be used
    def __init__(self):
        self.curIdx = 0             
        self.tracker = {}
        self.idx = {}

    # insert at curIdx; increment curIdx + 1
    def insert(self, val: int) -> bool:
        if val not in self.tracker: 
            self.tracker[val] = self.curIdx
            self.idx[self.curIdx] = val
            self.curIdx += 1
            return True
        else: 
            return False


    # replace the largest index with removed. 
    def remove(self, val: int) -> bool:
        if val in self.tracker:




            return True
        else: 
            return False

    def getRandom(self) -> int:
        randIdx = randInt(0, self.curIdx - 1); 
        return self.idx[randIdx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()