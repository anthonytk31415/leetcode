# next, hasnext 
# Time: O(1)
# Space: O(1)

# init: 
# Time: O(n!)
# Space: O(n!)


# Trick for combinations: 
# each "call" interates over the ranges

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.length = combinationLength
        self.str = characters
        self.combo = self.buildCombo()
        self.index = -1

    def buildCombo(self):
        res = []
        
        def helper(str, length, path, i, res):
            if length == 0: 
                res.append(path)
                return 
            for j in range(i, len(str) - length + 1):
                helper(str, length - 1, path + str[j], j + 1, res)

        helper(self.str, self.length, '', 0, res)
        return res

    def next(self) -> str:
        self.index +=1
        return self.combo[self.index]

    def hasNext(self) -> bool:
        index = self.index + 1
        return 0 <= index < len(self.combo)

# itr = CombinationIterator('abcde', 3)
itr = CombinationIterator('abc', 2)
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
print(itr.next())
print(itr.hasNext())
print(itr.combo)


# len of str = 5
# len = 3
# abcde 3

# abc         j = 2, 3, 4
# abd


# abc
# abd
# abe
# bcd
# bce
# cde


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()