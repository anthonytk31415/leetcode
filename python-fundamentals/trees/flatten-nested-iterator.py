# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.nest = self.flatten(nestedList)
        self.index = 0

    def flatten(self, nested):
        res = []
        for x in nested: 
            if isinstance(x, int):
                res.append(x)
            else: 
                y = self.flatten(x)
                res = res + y
        return res

    def next(self):
        idx = self.index
        self.index +=1
        return self.nest[idx]
    
    def hasNext(self):
        return 0 <= self.index < len(self.nest)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# nestedList = [[1,1],2,[1,1]]
nestedList = [1,[4,[6]]]

i, v = NestedIterator(nestedList), []
print(i.nest)
while i.hasNext(): 
    print(i.index)
    v.append(i.next())
print(v)